# Import socket module
import socket
#from client_utils import *

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 65426

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# Receive input
door = input('Selecione sua porta: ')

# Send input
s.send(door.encode('utf-8'))

# receive data from the server
print("porta com bode " + s.recv(1024).decode('utf-8') + '\n')
s.send(input('Deseja mudar de porta? s/n \n').encode('utf-8'))

door=s.recv(1024).decode('utf-8')
car=s.recv(1024).decode('utf-8')

if door == car:
    print('Parabéns, você venceu!')
else:
    print ('Que pena, você perdeu.')

# close the connection
s.close()