from figure import Figure
import pygame


class Bishop(Figure):
    def __init__(self, x, y, w=60, h=60):
        super().__init__(x, y, w, h)
        self.white_image = pygame.image.load('imgs/white_bishop.png')
        self.black_image = pygame.image.load('imgs/black_bishop.png')
