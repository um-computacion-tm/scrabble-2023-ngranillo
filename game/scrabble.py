from game.board import Board
from game.player import Player
from game.tilesbag import Tilebag


class ScrabbleGame:
    def __init__(self, player_count):
        self.board = Board()
        self.tilesbag = Tilebag()
        self.players = []
        for _ in range(player_count):
            self.players.append(Player())