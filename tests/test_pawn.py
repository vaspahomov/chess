import unittest

from color import Color
from figures.pawn import Pawn


class TestPawn(unittest.TestCase):
    def test_check_valid_position_first_move_2_black(self):
        pawn = Pawn(4, 1, Color.BLACK)
        self.assertTrue(pawn.check_valid_position(4, 3, []))

    def test_check_valid_position_first_move_1_black(self):
        pawn = Pawn(4, 1, Color.BLACK)
        self.assertTrue(pawn.check_valid_position(4, 2, []))

    def test_check_valid_position_first_move_1_white(self):
        pawn = Pawn(4, 6, Color.WHITE)
        self.assertTrue(pawn.check_valid_position(4, 5, []))

    def test_check_valid_position_first_move_2_white(self):
        pawn = Pawn(4, 6, Color.WHITE)
        self.assertTrue(pawn.check_valid_position(4, 6, []))

    def test_check_attack_position_white_left(self):
        figures = []
        pawn = Pawn(6, 6, Color.WHITE)
        figures.append(pawn)
        figures.append(Pawn(5, 5, Color.BLACK))
        self.assertTrue(pawn.check_cell_under_attack(5, 5, figures))

    def test_check_attack_position_black_left(self):
        figures = []
        pawn = Pawn(5, 5, Color.BLACK)
        figures.append(pawn)
        figures.append(Pawn(6, 6, Color.WHITE))
        self.assertTrue(pawn.check_cell_under_attack(6, 6, figures))

    def test_check_attack_position_white_right(self):
        figures = []
        pawn = Pawn(4, 6, Color.WHITE)
        figures.append(pawn)
        figures.append(Pawn(5, 5, Color.BLACK))
        self.assertTrue(pawn.check_cell_under_attack(5, 5, figures))

    def test_check_attack_position_black_right(self):
        figures = []
        pawn = Pawn(7, 5, Color.BLACK)
        figures.append(pawn)
        figures.append(Pawn(6, 6, Color.WHITE))
        self.assertTrue(pawn.check_cell_under_attack(6, 6, figures))
