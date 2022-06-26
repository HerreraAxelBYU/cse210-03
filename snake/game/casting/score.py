from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point

class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._position = Point(0, 0)
        self._color = Color(30, 30, 30)
        self._points = 0
        self._font_size = 17
        self._name = "Player"
        self.set_text(f"{self._name} Score: {self._points}")
    
    def _prepare_self(self, pos_x, pos_y, set_color, player_name):
        self._position = Point(pos_x, pos_y)
        self._color = set_color
        self._name = player_name
        self.set_position(self._position)
        self.set_text(f"{self._name} Score: {self._points}")

    def _add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"{self._name} Score: {self._points}")