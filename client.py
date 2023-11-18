import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 49002
MAX_PACKET = 1024


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        while True:
            request = input()
            client_socket.send(request.encode())
            response = client_socket.recv(MAX_PACKET)
            print(response.decode())
            if request == 'EXIT':
                break
    except socket.error as msg:
        print('Failed to open server socket - ' + str(msg))
    finally:
        client_socket.close()


if __name__ == '__main__':
    main()


