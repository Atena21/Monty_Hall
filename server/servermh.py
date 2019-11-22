import socket
import threading
from server_utils import *

HOST = '172.16.35.115'  # Standard loopback interface address (localhost)
PORT = 65426  # Port to listen on (non-privileged ports are > 1023)
MAX_CLIENTS = 100  # Max number of simultaneous clients

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(MAX_CLIENTS)

clients = [None] * MAX_CLIENTS
addr = [None] * MAX_CLIENTS
cur_client = 0


def handle_game(client_sock):
   try:
       # generate pc hand
        pc_hand = car_door()

        player_hand = client_sock.recv(1024).decode('utf-8')

        client_sock.send(first_choice(player_hand,pc_hand).encode('utf-8'))

        troca = client_sock.recv(1024).decode('utf-8')
        ans = get_solution(player_hand,pc_hand,troca)
        print('selecionada: '+ans+'. Premio: ' + pc_hand)
        client_sock.send(str(ans).encode('utf-8'))
        client_sock.send(str(pc_hand).encode('utf-8'))
   except:
        client_sock.close()
   finally:
        exit(0)


while True:
    if (cur_client >= MAX_CLIENTS):
        break
    clients[cur_client], addr[cur_client] = sock.accept()
    print('Got connection from', addr[cur_client])

    game_thread = threading.Thread(target=handle_game, args=(clients[cur_client],), daemon=True)
    game_thread.start()