from game.board import Board
from game.player import Player
from game.tilesbag import Tilebag
from game.dictionary import Dictionary


class ScrabbleGame:
    def __init__(self, player_count):
        self.board = Board()
        self.tilesbag = Tilebag()
        self.players = []
        self.dictionary = Dictionary('dictionaries/dictionary.txt')
        for _ in range(player_count):
            self.players.append(Player())
            self.current_player = None
            
    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif id(self.current_player) == id(self.players[(len(self.players)) -1]):
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[self.players.index(self.current_player)+ 1]