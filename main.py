from Server_socket import Server_socket

def startGame():
    server_socket = Server_socket()
    server_socket.create_server_socket()


if __name__ == '__main__':
    startGame()
