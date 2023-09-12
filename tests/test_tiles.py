import unittest
from game.tiles import Tile, NotAJoker


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)
        
    def test_joker_with_valid_letter(self):
        tile = Tile('*', 0)
        tile.joker('A')
        self.assertEqual(tile.letter, 'A')
    
    def test_joker_with_invalid_letter(self):
        tile = Tile('B', 1)
        with self.assertRaises(NotAJoker):
            tile.joker('A')