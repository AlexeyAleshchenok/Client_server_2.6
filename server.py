import socket
from datetime import datetime
import random

IP = '0.0.0.0'
PORT = 49002
QUEUE_SIZE = 1
MAX_PACKET = 4


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((IP, PORT))
        server_socket.listen(QUEUE_SIZE)
        print('Waiting for connection....')
        while True:
            comm_socket, addr = server_socket.accept()
            print(f'Connection with {addr}')
            try:
                while True:
                    request = comm_socket.recv(MAX_PACKET).decode()
                    if request == 'Time':
                        response = str(datetime.now().time())
                        comm_socket.send(response.encode())

                    elif request == 'Name':
                        response = 'Cyber'
                        comm_socket.send(response.encode())

                    elif request == 'Rand':
                        response = str(random.randint(1, 10))
                        comm_socket.send(response.encode())

                    elif request == 'EXIT':
                        response = 'Bye-bye'
                        comm_socket.send(response.encode())

                    if request == 'EXIT':
                        print('Client left the server')
                        break

            except socket.error as msg:
                print('failed to open client socket - ' + str(msg))
            finally:
                comm_socket.close()
            print('Waiting for connection....')
    except socket.error as msg:
        print('failed to open server socket - ' + str(msg))
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()
