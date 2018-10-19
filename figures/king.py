from chess_pieces import ChessPieces
from figure import Figure
import pygame


class King(Figure):
    def __init__(self, x, y, w=60, h=60):
        super().__init__(x, y, w, h)
        self.figure = ChessPieces.KING
        self.white_image = pygame.image.load('imgs/white_king.png')
        self.black_image = pygame.image.load('imgs/black_king.png')

    def check_valid_position(self, x, y, figures):
        if self.set_back(x, y):
            return True

        if self.check_figure_color_in_this_cell(x, y, figures) == self.color:
            return False

        for f in figures:
            if f.figure != ChessPieces.KING and f.check_valid_position(x, y, figures) and f.color != self.color:
                return False
        if self.x <= x + 1 and self.x >= x - 1 and \
                self.y <= y + 1 and self.y >= y - 1:
            if self.x != x or self.y != y:
                return True
