from figure import Figure
import pygame


class Knight(Figure):
    def __init__(self, x, y, w=60, h=60):
        super().__init__(x, y, w, h)
        self.white_image = pygame.image.load('imgs/white_knight.png')
        self.black_image = pygame.image.load('imgs/black_knight.png')

    def check_valid_position(self, x, y, figures):
        if self.set_back(x,y):
            return True
        if self.check_figure_color_in_this_cell(x, y, figures) == self.color:
            return False
        if self.x == x + 2 or self.x == x - 2:
            if self.y == y - 1 or self.y == y + 1:
                print(1)
                return True
        if self.x == x + 1 or self.x == x - 1:
            if self.y == y - 2 or self.y == y + 2:
                print(1)
                return True
