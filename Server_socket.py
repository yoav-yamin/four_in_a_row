from Game import Game
import socket

class Server_socket:

    def create_server_socket(self):
        list_of_row = [5, 4, 3, 2, 1, 0]
        game_to_play = Game()
        game_to_play.initialize_game_board()
        HOST = '127.0.0.1'
        PORT = 65432
        BUFFER_SIZE = 1024
        COUNT_OF_SOCKET_TO_LISTEN = 1

        server_socket = socket.socket()
        print("Created Socket")
        server_socket.bind((HOST, PORT))
        print("Binded Socket")
        server_socket.listen(COUNT_OF_SOCKET_TO_LISTEN)
        print("Socket is Listening")

        client_socket, client_address = server_socket.accept()
        print(f"Got a new connection {client_address}")

        # Send an initial message to the client after the connection
        # initial_message = "We Got a Connection, Lets Play!"
        # client_socket.send(initial_message.encode())
        print("Waiting for data")

        while True:
            data_from_client = client_socket.recv(BUFFER_SIZE).decode()
            if not data_from_client:
                break
            num1, num2 = game_to_play.player_turn(data_from_client)
            print("")
            if not game_to_play.check_if_win() and not game_to_play.check_if_tie():
                data_to_send = f"{list_of_row[num1]},{num2},"
                client_socket.send(data_to_send.encode())
            elif game_to_play.check_if_win():
                last_message = f"{list_of_row[num1]},{num2},Game Over! Player {game_to_play.get_winner()} Has Won! "
                client_socket.send(last_message.encode())
                break
            else:
                last_message = f"{list_of_row[num1]},{num2},It's a Tie!"
                client_socket.send(last_message.encode())
                break

        last_data_from_client = client_socket.recv(BUFFER_SIZE).decode()
        server_socket.close()
        print(last_data_from_client)
