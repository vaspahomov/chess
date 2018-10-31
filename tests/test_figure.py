import unittest

from color import Color
from figure import Figure


class TestFigure(unittest.TestCase):
    def test_init_position(self):
        figure = Figure(4, 4, Color.BLACK)
        self.assertEqual(4, figure.x)
        self.assertEqual(4, figure.y)

    def test_init_color(self):
        figure = Figure(4, 4, Color.BLACK)
        self.assertEqual(Color.BLACK, figure.color)
