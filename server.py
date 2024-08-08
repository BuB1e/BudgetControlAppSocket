import socket
import threading

HOST = "localhost"
PORT = 12345
MAX_CLIENT = 5

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.bind((HOST, PORT))
server_socket.listen(MAX_CLIENT)

print("Waiting for client . . .")
while True:
    connection_socket, addr = server_socket.accept()

    sentence = connection_socket.recv(1024).decode()
    capitalized_sentence = sentence.upper()
    connection_socket.send(capitalized_sentence.encode())

    connection_socket.close()