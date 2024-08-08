import socket
import threading

HOST = "localhost"
PORT = 12345
MAX_CLIENT = 5

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(MAX_CLIENT)

print("Waiting for clients . . . ")

balance = 0
history = []
lock = threading.Lock()

def handle_client(client_socket, addr):
    global balance
    global history

    print(f"Connection established with {addr}")

    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            response = ""
            with lock:
                if data.startswith("DEPOSIT"):
                    parts = data.split(" ", 2)
                    if len(parts) != 3:
                        response = "400 Bad Request: Incorrect format for DEPOSIT"
                    else:
                        reason, amount_str = parts[1], parts[2]
                        try:
                            amount = float(amount_str)
                            balance += amount
                            history.append(f"Deposited {amount} for {reason}")
                            response = "200 OK: Deposit successful"
                        except ValueError:
                            response = "400 Bad Request: Invalid amount format for DEPOSIT"

                elif data == "BALANCE":
                    response = f"200 OK: Current balance is {balance}"

                elif data == "HISTORY":
                    response = "200 OK: Transaction history:\n" + "\n".join(history)

                elif data.startswith("WITHDRAW"):
                    parts = data.split(" ", 2)
                    if len(parts) != 3:
                        response = "400 Bad Request: Incorrect format for WITHDRAW"
                    else:
                        reason, amount_str = parts[1], parts[2]
                        try:
                            amount = float(amount_str)
                            if balance >= amount:
                                balance -= amount
                                history.append(f"Withdrew {amount} for {reason}")
                                response = "200 OK: Withdrawal successful"
                            else:
                                response = "400 Bad Request: Insufficient funds"
                        except ValueError:
                            response = "400 Bad Request: Invalid amount format for WITHDRAW"
                else:
                    response = "400 Bad Request: Invalid operation"

            client_socket.sendall(response.encode())

        except Exception as e:
            print(f"Error with client {addr}: {e}")
            break

    client_socket.close()
    print(f"Connection closed with {addr}")

while True:
    client_socket, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()

