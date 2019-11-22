# Import socket module
import socket
#from client_utils import *


class ClientUtil:

    def __init__(self):
        self.s = socket.socket()
        self.port = 65426
        self.s.connect(('172.16.35.115', self.port))

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

