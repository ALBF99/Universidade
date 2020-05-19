import sys
import socket
import select

HOST = 'localhost'
PORT = 40011
RECV_BUFFER = 4096

def menu():
	print("1- Last sensor reading with ID X")
	print("2- Get list of registered sensors")
	print("3- Update firmware")
	print("4- Disable sensor")

'''The message is made readable for the broker'''
def encode_message(message):
	'''The client requests the last reading from a sensor with a certain id'''
	if message == "1":
		iD = input("ID: ")
		return "GETLEITURA_BY_ID "+ iD

	'''The client requests a list of all sensors running at the moment'''
	if message == "2" :
		return "GETLISTA_SENSORES"

	'''The client requests that an update is sent to the sensors of a certain type'''
	if message == "3" :
		return "UPDATE_FIRMWARE"

	'''The client requests that a sensor with a certain id to be closed and all of
	its information to be erased from the broker'''
	if message == "4":
		iD = input("ID: ")
		return "DELETESENSOR "+ iD

	return

'''Initializes the socket'''
def start_connection():
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientsocket.settimeout(2)

	servaddr = (HOST, PORT)
	clientsocket.connect(servaddr)

	return clientsocket

'''Main loop where messages are received and sent to the broker'''
def run_adm_client(clientsocket):
	while True:
		socket_list = [sys.stdin, clientsocket]

		rsocks,wsocks,esocks = select.select(socket_list,[],[])

		for socket in rsocks:
			if socket == clientsocket:
				data = socket.recv(RECV_BUFFER)
				data = data.decode()
				if not data:
					print("disconnected")
					sys.exit()
				else:
					print(data)
					
			else:

				message = input()
				message = encode_message(message)
				
				if message == "exit":
					sys.exit()

				if message == "UPDATE_FIRMWARE":
					update_sock = start_connection()

					update_sock.sendall(message.encode())

					file = open("firmware.txt", "r+")

					msg = update_sock.recv(RECV_BUFFER)
					print(msg.decode())

					for i in file.readlines():
						print(i)
						update_sock.sendall(i.encode())
					print("enviou ficheiro admin-sensor")

					file.close()

					update_sock.close()

				else:
					clientsocket.sendall(message.encode())

				menu()

	clientsocket.close()

if __name__ == "__main__":
	sock = start_connection()

	menu()

	run_adm_client(sock)