from figure import Figure
import pygame


class King(Figure):
    def __init__(self, x, y, w=60, h=60):
        super().__init__(x, y, w, h)
        self.white_image = pygame.image.load('imgs/white_king.png')
        self.black_image = pygame.image.load('imgs/black_king.png')
