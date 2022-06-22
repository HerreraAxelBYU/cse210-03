from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point

class PlayerTwo(Actor):


    def __init__(self):
        super().__init__()

        green = Color(0, 255, 0)
        position = Point(600, 0)

        self.set_text("Player Two")
        self.set_color(green)
        self.set_position(position)
        self._font_size = 20