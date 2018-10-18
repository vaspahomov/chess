from collections import defaultdict

from color import Color
from game_field import Field

from figures.bishop import Bishop
from figures.king import King
from figures.knight import Knight
from figures.pawn import Pawn
from figures.queen import Queen
from figures.rook import Rook

import pygame


class Game:
    def __init__(self,
                 caption,
                 width,
                 height,
                 # back_image_filename,
                 frame_rate=30):
        self.objects = []
        self.figures = []
        self.field = Field(480, 480)

        self.keydown_handlers = defaultdict(list)
        self.mouse_handlers = defaultdict(list)

        self.set_figures()

        # self.background_image = pygame.image.load(back_image_filename)
        self.frame_rate = frame_rate
        self.game_over = False

        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.font.init()

        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()

    def set_figures(self):
        for x in range(8):
            self.figures.append(Pawn(Color.BLACK, x, 1))
            self.figures.append(Pawn(Color.WHITE, x, 6))


        self.figures.append(Bishop(Color.BLACK, 2, 0))
        self.figures.append(Bishop(Color.BLACK, 5, 0))
        self.figures.append(Bishop(Color.WHITE, 2, 7))
        self.figures.append(Bishop(Color.WHITE, 5, 7))

        self.figures.append(Knight(Color.BLACK, 1, 0))
        self.figures.append(Knight(Color.BLACK, 6, 0))
        self.figures.append(Knight(Color.WHITE, 1, 7))
        self.figures.append(Knight(Color.WHITE, 6, 7))

        self.figures.append(Rook(Color.BLACK, 0, 0))
        self.figures.append(Rook(Color.BLACK, 7, 0))
        self.figures.append(Rook(Color.WHITE, 0, 7))
        self.figures.append(Rook(Color.WHITE, 7, 7))

        self.figures.append(Queen(Color.BLACK, 3, 0))
        self.figures.append(Queen(Color.WHITE, 4, 7))

        self.figures.append(King(Color.BLACK, 4, 0))
        self.figures.append(King(Color.WHITE, 3, 7))


    def update(self):
        for o in self.objects:
            o.update()

    def draw(self):
        for line in self.field.field:
            for o in line:
                o.draw(self.surface)

        for figure in self.figures:
            figure.draw(self.surface)

        for o in self.objects:
            o.draw(self.surface)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type in (pygame.MOUSEBUTTONDOWN,
                                pygame.MOUSEBUTTONUP,
                                pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def run(self):
        while not self.game_over:
            # self.surface.blit(self.background_image, (0, 0))
            self.update()
            self.draw()
            self.handle_events()

            pygame.display.update()

            self.clock.tick(self.frame_rate)


game = Game("Chess", 480, 480)
game.run()
