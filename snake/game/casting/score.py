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

        red = Color(255, 0, 0)
        position = Point(300, 0)
        self._points = 0
        self._font_size = 17
        self._color = red
        self.set_position(position)
        self.add_points(0)
        

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")

class Score2(Actor):
    def __init__(self):
        super().__init__()

        green = Color(0, 255, 0)
        position = Point(700, 0)
        self._points = 0
        self._font_size = 17
        self._color = green
        self.set_position(position)
        self.add_points(0)
        

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")
