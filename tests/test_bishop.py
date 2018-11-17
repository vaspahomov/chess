import unittest

from color import Color
from figures.bishop import Bishop


class TestBishop(unittest.TestCase):
    def test_check_valid_position_move_up_right(self):
        bishop = Bishop(4, 4, Color.BLACK)
        self.assertTrue(bishop.check_valid_position(1, 7, []))

    def test_check_valid_position_move_up_left(self):
        bishop = Bishop(4, 4, Color.BLACK)
        self.assertTrue(bishop.check_valid_position(1, 1, []))

    def test_check_valid_position_move_down_right(self):
        bishop = Bishop(4, 4, Color.BLACK)
        self.assertTrue(bishop.check_valid_position(7, 7, []))

    def test_check_valid_position_move_down_left(self):
        bishop = Bishop(4, 4, Color.BLACK)
        self.assertTrue(bishop.check_valid_position(1, 7, []))