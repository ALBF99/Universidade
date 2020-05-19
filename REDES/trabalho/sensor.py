import sys
import socket
import select
import time
import random

HOST = 'localhost'
PORT = 40011
TIMEOUT = 10
RECV_BUFFER = 4096
SOCK_TIMEOUT = 2

'''Interpret message from the broker'''
def decode_message(message, sock, firm):
	data = message.split()

	if data[0] == "SENSORSET":
		print("SENSOR SET")

	'''If a sensor with the same id is running or if an admin client requests it, the sensor
	closes'''
	if data[0] == "DELETESENSOR":
			print("disconnected")
			sys.exit()

	'''If requested by the admin, an update to the firmware is received from the broker'''
	if data[0] == "UPDATE_FIRMWARE":
		print("Receiving...")
		try:
			file_firm = open("firmware_sensor.txt", 'r+')
		
		except FileNotFoundError:
			file_firm = open("firmware_sensor.txt", 'w+')

		data = sock.recv(RECV_BUFFER)
		data = data.decode()
		print(data)
		get_firm = data.split("\n")
		firm = get_firm[0]

		file_firm.write(data)

		print("Updated")
		file_firm.close()

'''Initializes the socket'''
def start_connection():
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientsocket.settimeout(SOCK_TIMEOUT)

	servaddr = (HOST, PORT)
	clientsocket.connect(servaddr)

	return clientsocket

'''Get random values for the polluant readings'''
def random_values(type_sensor):
	if type_sensor == "CO2":
		return str(random.randint(0, 12))

	if type_sensor == "NO2":
		return str(random.randint(0, 12))

	else:
		return str(random.randint(0, 4))



if __name__ == "__main__":
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientsocket.settimeout(SOCK_TIMEOUT)

	servaddr = (HOST, PORT)
	clientsocket.connect(servaddr)

	'''Initialization of the sensor'''
	id_sensor = input("ID: ")
	type_sensor = input("TYPE: ")
	place = input("PLACE: ")

	'''Gets the firmware version of the sensor'''
	try:
		file_firm = open("firmware_sensor.txt", 'r+')
		firm = file_firm.read(1)
		
	except FileNotFoundError:
		file_firm = open("firmware_sensor.txt", 'w+')
		firm = "1"
		file_firm.write(firm)

	file_firm.close()

	'''Initial reading sent to the broker'''
	init_sensor = "SETSENSOR " + id_sensor + " " + type_sensor + " " + place + " " + firm
	clientsocket.send(init_sensor.encode())

	'''Receives confirmation if the sensor was registered or if a sensor with the same id
	is already running, in case of the latter, the sensor closes'''
	mes = clientsocket.recv(RECV_BUFFER)
	decode_message(mes, clientsocket, id_sensor)

	while True:
		sock_list = [clientsocket]

		rsocks,wsocks,esocks = select.select(sock_list,[],[],TIMEOUT)

		if len(rsocks) != 0:
			for sock in sock_list:
				if sock == clientsocket:
					data = sock.recv(RECV_BUFFER)
					data = data.decode()
					if not data:
						print("here")
						print("disconnected")
						sys.exit()
					else:
						decode_message(data, sock, firm)

		else:

			reading = "READING " + id_sensor + " " + time.asctime( time.localtime(time.time()) ) + " " + random_values(type_sensor) + "gm " + firm 
			clientsocket.send(reading.encode())

	clientsocket.close()