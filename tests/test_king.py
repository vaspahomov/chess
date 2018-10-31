import unittest

from color import Color
from figures.king import King
from figures.queen import Queen
from figures.rook import Rook


class TestKing(unittest.TestCase):
    def test_check_valid_position_up(self):
        king = King(4, 4, Color.BLACK)
        self.assertTrue(king.check_valid_position(4, 3, []))

    def test_check_valid_position_left(self):
        king = King(4, 4, Color.BLACK)
        self.assertTrue(king.check_valid_position(3, 4, []))

    def test_check_valid_position_diagonal(self):
        king = King(4, 4, Color.BLACK)
        self.assertTrue(king.check_valid_position(3, 3, []))

    def test_check_valid_position_black_left_castling(self):
        figures = []
        king = King(4, 0, Color.BLACK)
        rook = Rook(0, 0, Color.BLACK)
        figures.append(king)
        figures.append(rook)
        king.check_valid_position(2, 0, figures)

        self.assertTrue(king.x == 2)
        self.assertTrue(king.y == 0)

        self.assertTrue(rook.x == 3)
        self.assertTrue(rook.y == 0)

    def test_check_valid_position_black_right_castling(self):
        figures = []
        king = King(4, 0, Color.BLACK)
        rook = Rook(7, 0, Color.BLACK)
        figures.append(king)
        figures.append(rook)
        king.check_valid_position(6, 0, figures)

        self.assertTrue(king.x == 6)
        self.assertTrue(king.y == 0)

        self.assertTrue(rook.x == 5)
        self.assertTrue(rook.y == 0)

    def test_check_valid_position_white_left_castling(self):
        figures = []
        king = King(4, 7, Color.WHITE)
        rook = Rook(0, 7, Color.WHITE)
        figures.append(king)
        figures.append(rook)
        king.check_valid_position(2, 7, figures)

        self.assertTrue(king.x == 2)
        self.assertTrue(king.y == 7)

        self.assertTrue(rook.x == 3)
        self.assertTrue(rook.y == 7)

    def test_check_valid_position_white_right_castling(self):
        figures = []
        king = King(4, 7, Color.WHITE)
        rook = Rook(7, 7, Color.WHITE)
        figures.append(king)
        figures.append(rook)
        king.check_valid_position(6, 7, figures)

        self.assertTrue(king.x == 6)
        self.assertTrue(king.y == 7)

        self.assertTrue(rook.x == 5)
        self.assertTrue(rook.y == 7)