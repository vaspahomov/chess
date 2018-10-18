import pygame

from color import Color
from game_object import GameObject
from abc import ABCMeta, abstractmethod


class Figure(GameObject):
    def __init__(self, color, x, y, w=60, h=60):
        super().__init__(x * w, y * h, w, h)
        self.alive = True
        self.white_image = None
        self.black_image = None
        self.color = color

    def change_position(self, x, y):
        pass

    def remove(self):
        self.alive = False

    def draw(self, surface):
        if self.color == Color.WHITE:
            surface.blit(self.white_image, self.bounds)
        if self.color == Color.BLACK:
            surface.blit(self.black_image, self.bounds)

    def update(self):
        pass
