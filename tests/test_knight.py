import unittest

from color import Color
from figures.knight import Knight


class TestKnight(unittest.TestCase):
    def test_check_valid_position_left_up(self):
        knight = Knight(4, 4, Color.BLACK)
        self.assertTrue(knight.check_valid_position(2, 3, []))

    def test_check_valid_position_up_left(self):
        knight = Knight(4, 4, Color.BLACK)
        self.assertTrue(knight.check_valid_position(3, 2, []))

    def test_check_valid_position_right_up(self):
        knight = Knight(4, 4, Color.BLACK)
        self.assertTrue(knight.check_valid_position(6, 5, []))

    def test_check_valid_position_up_right(self):
        knight = Knight(4, 4, Color.BLACK)
        self.assertTrue(knight.check_valid_position(5, 6, []))

    def test_check_valid_position_left_down(self):
        knight = Knight(4, 4, Color.BLACK)
        self.assertTrue(knight.check_valid_position(6, 3, []))

    def test_check_valid_position_down_left(self):
        knight = Knight(4, 4, Color.BLACK)
        self.assertTrue(knight.check_valid_position(3, 6, []))

    def test_check_valid_position_right_down(self):
        knight = Knight(4, 4, Color.BLACK)
        self.assertTrue(knight.check_valid_position(5, 2, []))

    def test_check_valid_position_down_right(self):
        knight = Knight(4, 4, Color.BLACK)
        self.assertTrue(knight.check_valid_position(2, 5, []))
