import socket
from request_configuration import *
from random import randrange
# Different exit the program options
goodbye = ["bye", "goodbye", "have a good one", "see you", "see u", "take care", "bye bye", "thanks for your help", "thanks for the help", "takecare"]
server_socket = socket.socket()
ip = "127.0.0.1"
port = 4000
# Creates the server
server_socket.bind((ip, port))
server_socket.listen(1)
client_socket, client_address = server_socket.accept()
# Receives the first massage from the client
msg = client_socket.recv(1024)
msg = msg.decode()
# keeps receiving massages while the user doesn't use one of the exit program words
while not msg in goodbye:
    mes = str(understand(msg))
    mes = mes.encode()
    client_socket.send(mes)
    # It will read maximum 1024 bytes
    msg = client_socket.recv(1024)
    msg = msg.decode()
# Closes the communication
client_socket.close()
server_socket.close()