from color import Color
from figure import Figure
import pygame


class Pawn(Figure):
    def __init__(self, x, y, w=60, h=60):
        super().__init__(x, y, w, h)
        self.white_image = pygame.image.load('imgs/white_pawn.png')
        self.black_image = pygame.image.load('imgs/black_pawn.png')

        self.is_first_move = True

    def check_cell_under_attack(self, x, y, figures):
        if self.x == x + 1 or self.x == x - 1:
            if self.y == y + 1 and self.color == Color.WHITE:
                return True
            if self.y == y - 1 and self.color == Color.BLACK:
                return True
        pass

    def check_valid_position(self, x, y, figures):
        if self.set_back(x, y):
            return True
        color_of_figure_in_this_cell = self.check_figure_color_in_this_cell(x, y, figures)

        if self.x == x:
            if color_of_figure_in_this_cell != None:
                return False
            if self.is_first_move:
                if self.y == y - 2 and self.color == Color.BLACK:
                    self.is_first_move = False
                    return True
                elif self.y == y + 2 and self.color == Color.WHITE:
                    self.is_first_move = False
                    return True

            if self.y == y - 1 and self.color == Color.BLACK:
                self.is_first_move = False
                return True
            elif self.y == y + 1 and self.color == Color.WHITE:
                self.is_first_move = False
                return True

        elif color_of_figure_in_this_cell != None and color_of_figure_in_this_cell != self.color:
            if self.x == x + 1 or self.x == x - 1:
                if self.y == y + 1 and self.color == Color.WHITE:
                    return True
                if self.y == y - 1 and self.color == Color.BLACK:
                    return True
