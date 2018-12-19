import pygame

from figure import Figure


class Bishop(Figure):
    def __init__(self, x, y, color, w=60, h=60):
        super().__init__(x, y, color, w, h)
        self.white_image = pygame.image.load('imgs/white_bishop.png')
        self.black_image = pygame.image.load('imgs/black_bishop.png')

    def check_valid_position(self, x, y, figures):
        if self.set_back(x, y):
            return True
        for shift in range(1, 9):
            color_of_figure_in_this_cell = self.check_figure_color_in_this_cell(self.x + shift, self.y + shift, figures)
            if color_of_figure_in_this_cell == self.color:
                break
            if self.x + shift == x and self.y + shift == y:
                return True
            if color_of_figure_in_this_cell != self.color and color_of_figure_in_this_cell != None:
                break

        for shift in range(1, 9):
            color_of_figure_in_this_cell = self.check_figure_color_in_this_cell(self.x - shift, self.y - shift, figures)
            if color_of_figure_in_this_cell == self.color:
                break
            if self.x - shift == x and self.y - shift == y:
                return True
            if color_of_figure_in_this_cell != self.color and color_of_figure_in_this_cell != None:
                break

        for shift in range(1, 9):
            color_of_figure_in_this_cell = self.check_figure_color_in_this_cell(self.x + shift, self.y - shift, figures)
            if color_of_figure_in_this_cell == self.color:
                break
            if self.x + shift == x and self.y - shift == y:
                return True
            if color_of_figure_in_this_cell != self.color and color_of_figure_in_this_cell != None:
                break

        for shift in range(1, 9):
            color_of_figure_in_this_cell = self.check_figure_color_in_this_cell(self.x - shift, self.y + shift, figures)
            if color_of_figure_in_this_cell == self.color:
                break
            if self.x - shift == x and self.y + shift == y:
                return True
            if color_of_figure_in_this_cell != self.color and color_of_figure_in_this_cell != None:
                break
