from chess_pieces import ChessPieces
from color import Color
from figure import Figure
import pygame


class King(Figure):
    def __init__(self, x, y, color, w=60, h=60):
        super().__init__(x, y, color, w, h)
        self.figure = ChessPieces.KING
        self.white_image = pygame.image.load('imgs/white_king.png')
        self.black_image = pygame.image.load('imgs/black_king.png')

    def check_castling(self, x, y, figures):
        if self.y == y:
            if self.color == Color.WHITE:
                if self.x != 4 and self.y != 7:
                    return False
                if self.x == x - 2:
                    imposable = False
                    for f in figures:
                        if f.x == 6 and f.y == 7 or f.x == 5 and f.y == 7:
                            imposable = True
                            break
                    if not imposable:
                        for f in figures:
                            if f.x == 7 and f.y == 7:
                                f.set_figure(5, 7)
                        self.set_figure(6, 7)
                        return True
                if self.x == x + 2:
                    imposable = False
                    for f in figures:
                        if (f.x == 3 and f.y == 7) or (f.x == 2 and f.y == 7) or (f.x == 1 and f.y == 7):
                            imposable = True
                            break
                    if not imposable:
                        for f in figures:
                            if f.x == 0 and f.y == 7:
                                f.set_figure(3, 7)
                        self.set_figure(2, 7)
                        return True
            if self.color == Color.BLACK:
                if self.x != 4 and self.y != 0:
                    return
                if self.x == x - 2:
                    imposable = False
                    for f in figures:
                        if f.x == 6 and f.y == 0 or f.x == 5 and f.y == 0:
                            imposable = True
                            break
                    if not imposable:
                        for f in figures:
                            if f.x == 7 and f.y == 0:
                                f.set_figure(5, 0)
                        self.set_figure(6, 0)
                        return True
                if self.x == x + 2:
                    imposable = False
                    for f in figures:
                        if (f.x == 3 and f.y == 0) or (f.x == 2 and f.y == 0) or (f.x == 1 and f.y == 0):
                            imposable = True
                            break
                    if not imposable:
                        for f in figures:
                            if f.x == 0 and f.y == 0:
                                f.set_figure(3, 0)
                        self.set_figure(2, 0)
                        return True

    def check_valid_position(self, x, y, figures):
        if self.set_back(x, y):
            return True

        if self.check_figure_color_in_this_cell(x, y, figures) == self.color:
            return False

        if self.x <= x + 1 and self.x >= x - 1 and self.y <= y + 1 and self.y >= y - 1:
            if self.x != x or self.y != y:
                return True

        return self.check_castling(x, y, figures)
