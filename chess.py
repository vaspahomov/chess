from collections import defaultdict

from chess_pieces import ChessPieces
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
        self.width = width
        self.height = height

        self.check_white = False
        self.check_black = False

        self.next_turn = Color.WHITE

        self.objects = []
        self.figures = []
        self.field = Field(width, height)

        self.keydown_handlers = defaultdict(list)
        self.mouse_handlers = defaultdict(list)

        self.mouse_handlers[pygame.MOUSEBUTTONDOWN].append(self.on_mouse_down)
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

    # def handle(self, key):
    #     if key == pygame.MOUSEBUTTONDOWN:
    #         self.on_mouse_down()

    def on_mouse_down(self, type, pos):
        x, y = pygame.mouse.get_pos()
        x = x * 8 // self.width
        y = y * 8 // self.height
        if self.check_white or self.check_black:
            for figure in self.figures:
                if figure.x == x and figure.y == y and \
                        figure.color == self.next_turn and figure.figure == ChessPieces.KING:
                    # if not figure.clicked:
                    figure.clicked = True
                    self.next_turn = Color.BLACK if self.next_turn == Color.WHITE else Color.WHITE
                    return

        for figure in self.figures:
            if figure.clicked:
                if figure.check_valid_position(x, y, self.figures):
                    for f in self.figures:
                        if f.x == x and f.y == y and f.color != figure.color:
                            self.figures.remove(f)

                    if figure.x == x and figure.y == y:
                        self.next_turn = Color.BLACK if self.next_turn == Color.WHITE else Color.WHITE

                    figure.set_figure(x, y)

                    king = None
                    for f in self.figures:
                        if f.figure == ChessPieces.KING and f.color != figure.color:
                            king = f

                    check = figure.check_valid_position(king.x, king.y, self.figures)
                    if check and figure.color == Color.WHITE:
                        self.check_white = True
                    elif check and figure.color == Color.BLACK:
                        self.check_black = True

                return

        for figure in self.figures:
            if figure.x == x and figure.y == y and figure.color == self.next_turn:
                figure.clicked = True
                self.next_turn = Color.BLACK if self.next_turn == Color.WHITE else Color.WHITE

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
        for f in self.figures:
            f.update()

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
                for handler in self.mouse_handlers[event.type]:
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
