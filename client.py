# 6510451018 Harit Sombatsiri
import socket

HOST = "localhost"
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("Welcome to budget control application!")

while True :
    option_input = input('< D: deposit, S: show balance, H: history, W: withdraw , E: exit > : ')
    match option_input.upper() :
        case 'E' :
            break
        case 'D' :
            output_string = input("<Reason> <Amount> : ")
            client_socket.sendall(f"DEPOSIT {output_string}".encode())
        case 'S' :
            client_socket.sendall("BALANCE".encode())
        case 'H' :
            client_socket.sendall("HISTORY".encode())
        case 'W' :
            output_string = input("<Reason> <Amount> : ")
            client_socket.sendall(f"WITHDRAW {output_string}".encode())
        case _ :
            print("400 Bad Request: Invalid option")
            continue

    response = client_socket.recv(1024).decode()
    print(f"Server response: {response}")


client_socket.close()

