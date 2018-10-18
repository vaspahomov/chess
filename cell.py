import pygame

from game_object import GameObject
from color import Color


class Cell(GameObject):
    def __init__(self, color, x, y, w=60, h=60):
        super().__init__(x * w, y * h, w, h)
        self.color = color
        self.black_cell_img = pygame.image.load('imgs/black_cell.png')
        self.white_cell_img = pygame.image.load('imgs/white_cell.png')

    def draw(self, surface):
        if self.color == Color.WHITE:
            surface.blit(self.white_cell_img, self.bounds)

        elif self.color == Color.BLACK:
            surface.blit(self.black_cell_img, self.bounds)

    def update(self):
        pass
