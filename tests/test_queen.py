import unittest

from color import Color
from figures.queen import Queen


class TestQueen(unittest.TestCase):
    def test_check_valid_position_rook_move_up(self):
        queen = Queen(4, 4, Color.BLACK)
        self.assertTrue(queen.check_valid_position(4, 0, []))

    def test_check_valid_position_rook_move_down(self):
        queen = Queen(4, 4, Color.BLACK)
        self.assertTrue(queen.check_valid_position(4, 7, []))

    def test_check_valid_position_rook_move_left(self):
        queen = Queen(4, 4, Color.BLACK)
        self.assertTrue(queen.check_valid_position(0, 4, []))

    def test_check_valid_position_rook_move_right(self):
        queen = Queen(4, 4, Color.BLACK)
        self.assertTrue(queen.check_valid_position(7, 4, []))

    def test_check_valid_position_bishop_move_up_right(self):
        queen = Queen(4, 4, Color.BLACK)
        self.assertTrue(queen.check_valid_position(1, 7, []))

    def test_check_valid_position_bishop_move_up_left(self):
        queen = Queen(4, 4, Color.BLACK)
        self.assertTrue(queen.check_valid_position(1, 1, []))

    def test_check_valid_position_bishop_move_down_right(self):
        queen = Queen(4, 4, Color.BLACK)
        self.assertTrue(queen.check_valid_position(7, 7, []))

    def test_check_valid_position_bishop_move_down_left(self):
        queen = Queen(4, 4, Color.BLACK)
        self.assertTrue(queen.check_valid_position(1, 7, []))
