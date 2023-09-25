import unittest
from game.cell import Cell
from game.tiles import Tile


class TestCell(unittest.TestCase):
    def test_empty_cell(self):
        cell = Cell()
        self.assertEqual(cell.multiplier, 1)
        self.assertEqual(cell.letter, None)

    def test_cell_letter(self):
        tile = Tile('A', 1)
        cell = Cell()
        cell.put_tile(tile)
        self.assertEqual(cell.letter, tile)

    def test_cell_multiplier(self):
        cell = Cell()
        cell.set_multiplier(2)
        self.assertEqual(cell.get_multiplier(), 2)

    def test_no_multiplier(self):
        cell = Cell()
        self.assertFalse(cell.has_multiplier())

    def test_has_multiplier(self):
        cell = Cell()
        cell.set_multiplier(2)
        self.assertTrue(cell.has_multiplier())

    def test_no_letter(self):
        cell = Cell()
        self.assertFalse(cell.has_tile())

    def test_has_letter(self):
        cell = Cell()
        cell.put_tile(Tile('A', 1))
        self.assertTrue(cell.has_tile())

    def test_insert_letter_full(self):
        cell = Cell()
        cell.set_tile(Tile('A', 1))
        cell.put_tile(Tile('B', 1))
        self.assertEqual(cell.get_tile(), Tile('A', 1))

    def test_insert_letter_empty(self):
        cell = Cell()
        cell.put_tile((Tile('A', 1)))
        self.assertEqual(cell.letter.letter, 'A')

    def test_multiplier_type(self):
        cell = Cell()
        cell.set_multiplier_type('word')
        self.assertEqual(cell.get_multiplier_type(), 'word')

    def test_multiplier_type_2(self):
        cell = Cell()
        cell.set_multiplier_type('letter')
        self.assertEqual(cell.get_multiplier_type(), 'letter')

    def test_score_tile_empty(self):
        cell = Cell()
        self.assertEqual(cell.individual_score(), 0)

    def test_give_info(self):
        cell = Cell()
        cell.put_tile(Tile('A', 1))
        cell.set_multiplier_type('Letter')
        cell.set_multiplier(2)
        self.assertEqual((repr(cell)), 'A, 1, x2 Letter')

    def test_give_info_empty(self):
        cell = Cell()
        self.assertEqual((repr(cell)), "||  |x1||")



if __name__ == '__main__':
    unittest.main()