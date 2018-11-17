import unittest

from color import Color
from figures.rook import Rook


class TestRook(unittest.TestCase):
    def test_check_valid_position_right(self):
        rook = Rook(0, 0, Color.BLACK)
        self.assertTrue(rook.check_valid_position(7, 0, []))

    def test_check_valid_position_left(self):
        rook = Rook(7, 0, Color.BLACK)
        self.assertTrue(rook.check_valid_position(0, 0, []))

    def test_check_valid_position_up(self):
        rook = Rook(0, 7, Color.BLACK)
        self.assertTrue(rook.check_valid_position(0, 0, []))

    def test_check_valid_position_down(self):
        rook = Rook(0, 0, Color.BLACK)
        self.assertTrue(rook.check_valid_position(0, 7, []))
