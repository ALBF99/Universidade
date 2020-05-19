import sys
import socket
import select
import time

HOST = 'localhost'
PORT = 40011
RECV_BUFFER = 4096

def menu():
	print("1- Get list of locations with sensors of type X")
	print("2- Get last reading for a certain location") 
	print("3- Get reading for a certain date and time")
	print("4- Register place of interest")

'''The message is made readable for the broker'''
def encode_message(message, clientsocket):
	'''The client requests a list of all locations with sesnsors of a certain type'''
	if message == "1":
		tipo = input("Type: ")
		return "GETLISTA_BY_TIPO "+ tipo

	'''The client requests the last reading of a certain location'''
	if message == "2":
		local = input("Location: ")
		return "GETLEITURA_BY_LOCAL "+ local

	'''The client requests the last reading for a certain location and time'''
	if message == "3":
		local = input("Location: ")
		data = input("Date (Month/Day/Year): ")
		hora = input("Time (Hours:Minutes:Seconds): ")
		return "GETLEITURA_BY_DATA "+ local+ " "+ data+ " "+ hora

	'''The client requests to be notified if there are any changes recorded to a certain
	location especified by them'''
	if message == "4":
		local = input("Local: ")

		return "SETLOCAL_INTERESSE " + local

'''Initializes the socket'''
def start_connection():
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	servaddr = (HOST, PORT)
	clientsocket.connect(servaddr)

	return clientsocket

'''Main loop where messages are received and sent to the broker'''
def run_pub_client(clientsocket):
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
				message = encode_message(message, clientsocket)
				
				if message == "exit":
					sys.exit()
				
				clientsocket.send(message.encode())

				menu()

	clientsocket.close()

if __name__ == "__main__":
	sock = start_connection()

	menu()

	run_pub_client(sock)