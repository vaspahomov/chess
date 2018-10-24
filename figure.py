import pygame

from color import Color
from game_object import GameObject
from abc import ABCMeta, abstractmethod


class Figure(GameObject):
    def __init__(self, x, y, color, w=60, h=60):
        super().__init__(x * w, y * h, w, h)
        self.x = x
        self.y = y

        self.figure = None

        self.alive = True
        self.white_image = None
        self.black_image = None
        self.color = color
        self.clicked = False

    def set_figure(self, x, y):
        self.clicked = False
        self.x = x
        self.y = y
        self.bounds.x = self.x / 8 * 480
        self.bounds.y = self.y / 8 * 480

    def check_cell_under_attack(self, x, y, figures):
        if self.x == x and self.y == y:
            return True
        return self.check_valid_position(x, y, figures)

    def check_valid_position(self, x, y, figures):
        return True

    def check_figure_color_in_this_cell(self, x, y, figures):
        for f in figures:
            if f.x == x and f.y == y:
                return f.color

    def set_back(self, x, y):
        if self.x == x and self.y == y:
            self.clicked = False
            return True
        return False

    def remove(self):
        self.alive = False

    def follow_mouse(self):
        self.bounds.x, self.bounds.y = pygame.mouse.get_pos()
        self.bounds.x -= self.width / 2
        self.bounds.y -= self.height / 2

    def draw(self, surface):
        if self.color == Color.WHITE:
            surface.blit(self.white_image, self.bounds)
        if self.color == Color.BLACK:
            surface.blit(self.black_image, self.bounds)

    def update(self):
        if self.clicked:
            self.follow_mouse()
        pass
