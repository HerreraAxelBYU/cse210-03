from turtle import position
import constants
from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point

class Players(Actor):
    """An instance of a Players class. Contains the code for the trail segments.
    """
    def __init__(self):
        super().__init__()
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        self._crashed = False
        self._segments = []
        self._color = constants.BLACK
        self._start_position = Point(x, y)
        self._position = Point(x, y)

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_trail(self, number_of_segments):
        if self._crashed == False:
            for i in range(number_of_segments):
                trail = self._segments[-1]
                velocity = trail.get_velocity()
                offset = velocity.reverse()
                position = trail.get_position().add(offset)
                
                segment = Actor()
                segment.set_position(position)
                segment.set_velocity(velocity)
                segment.set_text("+")
                segment.set_color(self._color)
                self._segments.append(segment)

    def shrink_trail(self, number_of_segments):
        for i in range(number_of_segments):
            self._segments.pop()

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self, pos_x, pos_y, set_color):
        """Create the body of the cycle.
        Arg:
            pos_x = The x position of the object.  
            pos_y = The y position of the object.    
            color = The color of the object.
        """
        self._color = set_color
        self._start_position = Point(pos_x, pos_y)

        for i in range(constants.MIN_TRAIL_LENGTH):
            position = Point(pos_x - i * constants.CELL_SIZE, pos_y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "+"
            color = set_color if i == 0 else set_color
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)

    def get_start_position(self):
        return self._start_position