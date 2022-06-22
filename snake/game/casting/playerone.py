from turtle import position
from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point

class PlayerOne(Actor):


    def __init__(self):
        super().__init__()

        red = Color(255, 0, 0)
        position = Point(200, 0)

        self.set_text("Player One")
        self.set_color(red)
        self.set_position(position)
        self._font_size = 20