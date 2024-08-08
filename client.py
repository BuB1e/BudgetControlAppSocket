import socket

HOST = "localhost"
PORT = 12345
SERVER_NAME = 'servername'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

sentence = input('input lowercase sentence: ')
client_socket.send(sentence.encode())
modified_sentence = client_socket.recv(1024)
print('From server:', modified_sentence.decode())
client_socket.close()
