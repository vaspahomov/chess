from unittest import TestCase

from game_object import GameObject


class TestGameObject(TestCase):
    @property
    def _init_game_obj(self):
        return GameObject(0, 0)

    def test_left(self):
        self.assertEqual(self._init_game_obj.bounds.left, 0)

    def test_right(self):
        self.assertEqual(self._init_game_obj.bounds.right, 32)

    def test_top(self):
        self.assertEqual(self._init_game_obj.bounds.top, 0)

    def test_bottom(self):
        self.assertEqual(self._init_game_obj.bounds.bottom, 32)

    def test_width(self):
        self.assertEqual(self._init_game_obj.bounds.width, 32)

    def test_height(self):
        self.assertEqual(self._init_game_obj.bounds.height, 32)

    def test_center(self):
        self.assertEqual(self._init_game_obj.bounds.center, (16, 16))

    def test_centerx(self):
        self.assertEqual(self._init_game_obj.bounds.centerx, 16)

    def test_centery(self):
        self.assertEqual(self._init_game_obj.bounds.centery, 16)
