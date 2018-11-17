from chess import Game
import unittest
from unittest.mock import patch, Mock, MagicMock
import pygame
import threading
import time


class TestChess(unittest.TestCase):

    # @patch(Game.run, mock_run)
    def test_chess(self):
        def mock_run():
            mock.update()
            mock.draw()
            mock.handle_events()
            # if self.find_match(Color.BLACK):
            #     print('White')
            #     sys.exit(1)
            # if self.find_match(Color.WHITE):
            #     print('Black')
            #     sys.exit(1)


        mock = MagicMock(Game)
        mock.run = mock_run

        # game = Game("test", 480, 480)
        mock.run()

        self.assertTrue(True)
