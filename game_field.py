import pygame
from cell import Cell
from color import Color


class Field():
    def __init__(self, w, h):
        self.field = [[]]
        self.__init_field__(w, h)

    def __init_field__(self, w, h):
        self.field = [
            [Cell(Color.WHITE if (x + y) % 2 == 0 else Color.BLACK, x, y, w//8, h//8) for x in range(8)]
            for y in range(8)]
