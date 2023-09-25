from tiles import Tile

class Cell:
    def __init__(self):
        self.multiplier = 1
        self.letter = None
        self.multiplier_type = None
        self.multiplier_up = True

    def has_tile(self):
        return self.letter is not None

    def has_multiplier(self):
        return self.multiplier > 1

    def get_multiplier_type(self):
        return self.multiplier_type

    def get_multiplier(self):
        return self.multiplier

    def multiplier_is_up(self):
        if self.has_tile():
            self.multiplier_up = False

    def get_tile(self):
        return self.letter

    def put_tile(self, letter):
        if not self.has_tile():
            self.letter = letter
        self.multiplier_is_up()

    def individual_score(self):
        if self.has_tile():
            return self.letter.get_value() * self.multiplier
        return 0

    def set_multiplier_type(self, word):
        self.multiplier_type = word

    def set_multiplier(self, amount):
        self.multiplier = amount

    def set_tile(self, tile):
        self.letter = tile

    def set_word_multiplier(self, amount):
        self.multiplier = amount

    def __repr__(self):
        if self.letter is None:
            return f"||  |x{self.multiplier}||"

        return (f"{self.get_tile().get_letter()}, {self.get_tile().get_value()}, "
                f"x{self.multiplier} {self.multiplier_type}")