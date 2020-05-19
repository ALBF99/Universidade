import socket 
import select
import time
import traceback 
import pickle

SOCKET_LIST = []    # Open socket list
RECV_BUFFER = 4096  # Recomended value in python's documentation
HOST = "0.0.0.0"
PORT = 40011
TIMEOUT = 10
MAX_CLIENTS = 30


list_sensors={} #key = id_sensor; data[0] = type; data[1] = location; data[2] to data[11] = readings 
list_firmware={} #key = id_sensor; data = firmware version
list_sock={} #key = id_sensor; data = sensor socket
list_publish={} #key = public client socket; data = subscribed location

'''Load data structure as pickle file saved on disk or create a new file if not found'''
def pickle_read(dic, filename):
    count=0
    try:
        pickle_in = open(filename,'rb')
        return pickle.load(pickle_in)
    except:
        count+=1

    if count==1:
        return dic

'''Save data structure as pickle file saved on disk'''
def pickle_write(list, filename):
    pickle_out = open(filename,'wb')
    pickle.dump(list, pickle_out)


'''Register sensor '''
def set_sensor(info, sock):
    new_list_sensor = pickle_read(list_sensors, "sensores.pickle")
    list_firm = pickle_read(list_firmware, "ver_firmware.pickle")
    
    sensor_id = info[1]
    type_sensor = info[2]
    location = info[3]

    space = " "

    if sensor_id in list_sock:
        string = "DELETESENSOR " + sensor_id

    else:
        new_list_sensor[sensor_id] = info[2:4]
        list_sock[sensor_id] = sock
        list_firm[sensor_id] = 1

        for i in range(10):
            new_list_sensor[sensor_id].append(space)

        string = "SENSORSET "+ sensor_id +" "+ type_sensor +" "+ location
        pickle_write(new_list_sensor, "sensores.pickle")
        pickle_write(list_firm, "ver_firmware.pickle")
       

    sock.sendall(string.encode())

'''Get last reading of a sensor with a certain id'''
def get_reading(id_sensor):
    new_list_sensor = pickle_read(list_sensors, "sensores.pickle")
    
    if id_sensor in new_list_sensor:
        string = "Last reading is "+ new_list_sensor[id_sensor][2]
    else:
        string = "id not atributted"

    sock.sendall(string.encode())

'''Get list of active sensors'''
def get_list():
    string = "Sensor List:\n"
    new_list_sensor = pickle_read(list_sensors, "sensores.pickle")
    
    for i in new_list_sensor:
        if i in list_sock:
            string = string + i + ": " + ', '.join(new_list_sensor[i][:2])+"\n"
    
    sock.sendall(string.encode())

'''Delete a sensor with a certain id as requested by an admin client'''
def del_sensor(id_sensor):
    old_list = pickle_read(list_sensors, "sensores.pickle")

    if id_sensor in old_list:
        new_list = old_list
        del new_list[id_sensor]
        
        kill = "DELETESENSOR"
        list_sock[id_sensor].sendall(kill.encode())
        del list_sock[id_sensor]
        
        pickle_write(new_list, "sensores.pickle")
        string = "Sensor deleted with id " + id_sensor

    else:
        string = "Sensor with id " + id_sensor + " not found"

    sock.sendall(string.encode())

'''Get a list of all sensors for the requested type'''
def get_list_type(type_sensor):
    string = "List of locations with sensors of type " + type_sensor + "\n"
    curr_list = pickle_read(list_sensors, "sensores.pickle")
    flag = 0

    for i in curr_list:
        if i in list_sock:
            if (curr_list[i][0] == type_sensor):
                #Isto devia verificar que os sensores estão abertos
                location = curr_list[i][1]
                string = string + location + '\n'
                flag = 1

    if (flag == 0):
        string = "Sensors of type " + type_sensor + " not found" 

    sock.sendall(string.encode())

'''Get the last reading for the requested location'''
def get_reading_place(location):
    string = "Last reading for " + location + "\n"
    curr_list = pickle_read(list_sensors, "sensores.pickle")
    flag = 0

    for i in curr_list:
        if (curr_list[i][1] == location):
            type_sensor = curr_list[i][0]
            reading = curr_list[i][2]
            string = string + type_sensor + ": "+ reading + '\n'
            flag = 1

    if (flag == 0):
        string = "No readings for this location" 

    sock.sendall(string.encode())

'''Get a reading for the requested date and time'''
def get_reading_date(location, date, time):
    string = "Reading for " + location + " on "+ date + " " + time +"\n"
    curr_list = pickle_read(list_sensors, "sensores.pickle")
    flag = 0
    date = date.split('/')

    for i in curr_list:
        if (curr_list[i][1] == location):
            type_sensor = curr_list[i][0]

            for j in range(2, 12):
                if (curr_list[i][j] == " "):
                    break

                reading = curr_list[i][j].split()

                if(reading[1]==date[0] and reading[2]==date[1] and reading[3]==time and reading[4]==date[2]):
                    string = string + type_sensor + ": "+ reading[5] + '\n'
                    flag = 1



    if (flag == 0):
        string = "No readings for this location or date and time" 

    sock.sendall(string.encode())

'''Add a new reading received from a sensor'''
def add_reading(id_sensor, value):
    curr_list = pickle_read(list_sensors, "sensores.pickle")
    
    if (curr_list[id_sensor][2] != " "):

        i = 11
        while(i>2):
            curr_list[id_sensor][i] = curr_list[id_sensor][i-1]
            i = i-1

    curr_list[id_sensor][2] = value
    string = "New reading: "+ value
    
    pickle_write(curr_list, "sensores.pickle")
    sock.sendall(string.encode())

    if len(list_publish)>0:
        notify_changes()

'''Set a certain location as to receive notification on fluctuations of readings'''
def set_notification(sock, location):
    if sock in list_publish:
        string = "Already subscribed"
        sock.sendall(string.encode())

    else:
        list_publish[sock] = location
        string = "Subscribed"
        sock.sendall(string.encode())

'''Check if the subscribed location as had any fluctuations in the corresponding readings'''
def notify_changes():
    new_list = pickle_read(list_sensors, "sensores.pickle")

    for sock in list_publish:
        for sensor in list_sock:
                
            if new_list[sensor][3] != " ":
                
                if new_list[sensor][1] == list_publish[sock]:
                    
                    new_reading = new_list[sensor][2].split(" ")
                    last_reading = new_list[sensor][3].split(" ")

                    if new_reading[5] != last_reading[5]:
                        string = "Sensor in " + list_publish[sock] + " changed"
                        sock.sendall(string.encode())

'''Receive firmware update from admin client'''
def save_file_firm(sock):
    string = "READY"
    sock.sendall(string.encode())
    
    time.sleep(1)
    
    data = sock.recv(RECV_BUFFER)
    data = data.decode()
    file = data

    return file

'''Send firmware update to a sensor'''
def send_file_firm(sock, file):
    string = "UPDATE_FIRMWARE"
    sock.sendall(string.encode())
    print("SENDING")

    time.sleep(1)

    sock.sendall(file.encode())

    time.sleep(1)

'''Receives firmware update from admin client and forwards it to the corresponding type sensors'''
def update_firmware(sock):
    file = save_file_firm(sock)
    get_version = file.split("\n")

    list_sensor = pickle_read(list_sensors, "sensores.pickle")
    list_firm = pickle_read(list_firmware, "ver_firmware.pickle")

    for iD in list_firm:
        if iD in list_sock:
            if list_firm[iD] < int(get_version[0]):
                if list_sensor[iD][0] == get_version[1]:
                    list_firm[iD] = int(get_version[0])
                    sockToUpdate = list_sock[iD]
                    send_file_firm(sockToUpdate, file)

    pickle_write(list_firm, "ver_firmware.pickle")
   

def array_to_string(array):
    string = ""

    for i in array:
        string = string + i + ' '

    return string


# função que trata dados do cliente
def data_treatment(data, sock):
    print("Client %s\n\tMessage: '%s'" % (sock, data))

    data = data.split()
    tarefa = data[0]

    if tarefa == "SETSENSOR":
        set_sensor(data, sock)

    if tarefa == "GETLEITURA_BY_ID":
        get_reading(data[1])

    if tarefa == "GETLISTA_SENSORES":
        get_list()

    if tarefa == "UPDATE_FIRMWARE":
        update_firmware(sock)       

    if tarefa == "DELETESENSOR":
        del_sensor(data[1])

    if tarefa == "GETLISTA_BY_TIPO":
        get_list_type(data[1])

    if tarefa == "GETLEITURA_BY_LOCAL":
        get_reading_place(data[1])

    if tarefa == "GETLEITURA_BY_DATA":
        get_reading_date(data[1], data[2], data[3])

    if tarefa == "SETLOCAL_INTERESSE":
        set_notification(sock, data[1])

    if tarefa == "READING":
        add_reading(data[1], array_to_string(data[2:8]))
          
if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Sets up socket
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))  #Accepts connections from anywhere
    server_socket.listen(MAX_CLIENTS) #Can only monitor the defined max sockets
    server_socket.setblocking(0) #The socket is non blocking
    
    #Appends server socket to the monotoring list
    SOCKET_LIST.append(server_socket)
    
    print("Server started on port %d" % (PORT,))


    while True:
        #Sockets that were disconnected are removed from monotoring list
        for sock in SOCKET_LIST:
            if sock.fileno() < 0:
                SOCKET_LIST.remove(sock)

        #Waits for data to be received until timeout
        rsocks,_,_ = select.select(SOCKET_LIST,[],[], TIMEOUT)
        
        for sock in rsocks:  #Cycles trough the sockets with data to be received
             
            if sock == server_socket: #There is a new connection
                newsock, addr = server_socket.accept()
                newsock.setblocking(0)
                SOCKET_LIST.append(newsock)
                
                print("New client - %s" % (addr,))
                 
            else: #There is new data to be received
                try:
                    data = sock.recv(RECV_BUFFER)
                    data = data.decode()
                    if data:
                        data_treatment(data, sock)
                        
                    else: #There is no data from a client because it has disconnected
                        print("no data")
                        print("Client disconnected [" + str(sock.getpeername()) + "]")
                        sock.close()
                        SOCKET_LIST.remove(sock)
                        
                except Exception as e: #Exceptions
                    print("Client disconnected")
                    print("Exception -> %s" % (e,))
                    print(traceback.format_exc())
                    
                    sock.close()
                    SOCKET_LIST.remove(sock)
