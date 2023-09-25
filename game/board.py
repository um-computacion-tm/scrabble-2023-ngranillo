from game.cell import Cell

class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]
            for _ in range(15)
        ]
    
    def is_active_and_letter_multiplier(self,cell):
        return cell.status == 'active' and cell.multiplier_type == 'letter'

    def is_active_and_word_multiplier(self,cell):
        return cell.status == 'active' and cell.multiplier_type == 'word'
    
    def is_desactive_or_none_multiplier(self,cell):
        return cell.status == 'desactive' or cell.multiplier_type == ''

    def place_tile(self, row, col, tile):
        if 0 <= row < 15 and 0 <= col < 15:
            cell = self.grid[row][col]
            if cell.letter is None:
                cell.add_letter(tile)
                return True
        return False

    def validate_word(self, start_row, start_col, word, direction):
        if direction == 'horizontal':
            for i, letter in enumerate(word):
                col = start_col + i
                if col >= 15 or (self.grid[start_row][col].letter is None or self.grid[start_row][col].letter.letter != letter):
                    return False
            return True
        elif direction == 'vertical':
            for i, letter in enumerate(word):
                row = start_row + i
                if row >= 15 or (self.grid[row][start_col].letter is None or self.grid[row][start_col].letter.letter != letter):
                    return False
            return True