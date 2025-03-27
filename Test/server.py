import socket
import random
import json

class Connect4Server:
    def __init__(self, host='0.0.0.0', port=12345):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(2)
        print("Waiting for players to connect...")

        self.player1, _ = self.server_socket.accept()
        print("Player 1 connected")
        self.player2, _ = self.server_socket.accept()
        print("Player 2 connected")

        self.current_player = self.player1
        self.other_player = self.player2
        self.current_player.send("1".encode('utf-8'))
        self.other_player.send("2".encode('utf-8'))


    def switch_turns(self):
        self.current_player, self.other_player = self.other_player, self.current_player

    def get_move(self):
        move = self.current_player.recv(1024).decode()
        return int(move)

    # def send_turn(self):
    #     self.current_player.send("1".encode('utf-8'))
    #     self.other_player.send("2".endcode('utf-8'))

    def send_move(self, move):
        self.other_player.send(str(move).encode())
        self.switch_turns()

    def close(self):
        self.player1.close()
        self.player2.close()
        self.server_socket.close()
    # def sync_to_clients(self, board, winner):
    #     package = {
    #         'board': board,
    #         'turn': self.current_player,
    #         'winner': winner
    #     }
    #     message = json.dumps(package).encode('utf-8')
    #     self.current_player.sendall(message)
    #     self.other_player.sendall(message)
