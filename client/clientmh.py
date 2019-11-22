# Import socket module
import socket
#from client_utils import *


class ClientUtil:

    def __init__(self):
        self.s = socket.socket()
        self.port = 65426
        self.s.connect(('127.0.0.1', self.port))

    def choose_door(self, choice):
        door = str(choice)
        self.s.send(door.encode('utf-8'))
        goat = self.s.recv(1024).decode('utf-8')
        return int(goat)

    def keep_door(self, choice):
        self.s.send(choice.encode('utf-8'))
        door = self.s.recv(1024).decode('utf-8')
        car = self.s.recv(1024).decode('utf-8')
        # print(choice, door, car)
        return int(door), int(car)

    def __del__(self):
        self.s.close()

# # def get_input(self):
# #     return self.entrada
#
# # Create a socket object
# s = socket.socket()
#
# # Define the port on which you want to connect
# port = 65426
#
# # connect to the server on local computer
# s.connect(('127.0.0.1', port))
#
# # Receive input
# door = input('Selecione sua porta: ')
#
# # Send input
# s.send(door.encode('utf-8'))
#
# # receive data from the server
# goat = s.recv(1024).decode('utf-8')
# print("porta com bode " + goat + '\n')
# s.send(input('Deseja mudar de porta? s/n \n').encode('utf-8'))
#
# door=s.recv(1024).decode('utf-8')
# car=s.recv(1024).decode('utf-8')
#
# if door == car:
#     print('Parabéns, você venceu!')
# else:
#     print ('Que pena, você perdeu.')
#
# # close the connection
# s.close()
