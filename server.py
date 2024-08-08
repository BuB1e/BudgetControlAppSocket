import socket
import threading

HOST = "localhost"
PORT = 12345
MAX_CLIENT = 5

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.bind(HOST, PORT)
server_socket.listen(MAX_CLIENT)