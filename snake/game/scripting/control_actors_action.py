import constants
import time
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """An input action that controls movement of an actor.
    The responsibility of ControlActorsAction is to get the direction and move the player's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

class PlayerTrailGrow(ControlActorsAction):
    """Causes player trails to grow continuosly until the max trail length is reached.
    """
    def execute(self, cast, script):
        # ============ PLAYER ONE ============ #

        # Extend trail if 'e' is pressed.
        if self._keyboard_service.is_key_down('e'):
            p1 = cast.get_first_actor("player_1")
            p1_length = len(p1.get_segments())
            if p1_length < constants.MAX_TRAIL_LENGTH:
                p1.grow_trail(1)
         # Return original legnth of trail if 'e' is released.
        if self._keyboard_service.is_key_up('e'):
            p1 = cast.get_first_actor("player_1")
            p1_length = len(p1.get_segments())
            if p1_length > constants.MIN_TRAIL_LENGTH:
                p1.shrink_trail(1)

        # ============ PLAYER TWO ============ #

        # Extend trail if 'o' is pressed.
        if self._keyboard_service.is_key_down('o'):
            p2 = cast.get_first_actor("player_2")
            p2_length = len(p2.get_segments())
            if p2_length < constants.MAX_TRAIL_LENGTH:
                p2.grow_trail(1)
        # Return original legnth of trail if 'o' is released.
        if self._keyboard_service.is_key_up('o'):
            p2 = cast.get_first_actor("player_2")
            p2_length = len(p2.get_segments())
            if p2_length > constants.MIN_TRAIL_LENGTH:
                p2.shrink_trail(1)
            
class ResetActorPositions(ControlActorsAction):
    """Reset the positions of both players when pressing 'space'.
    """
    def execute(self, cast, script):
        # ============ PLAYER ONE ============ #

        if self._keyboard_service.is_key_down('space'):
            p1 = cast.get_first_actor("player_1")
            p1_segments = p1.get_segments()
            p1_length = len(p1.get_segments())
            # Remove the Player's trail.
            if p1_length > 1:
                for segments in p1_segments:
                    p1.shrink_trail(1)
            # Reposition Player back to their starting positon.
            p1_head = p1.get_head()
            p1_start = p1.get_start_position()
            p1_head.set_position(p1_start)

        if self._keyboard_service.is_key_up('space'):
            p1 = cast.get_first_actor("player_1")
            p1_length = len(p1.get_segments())
            # Grow back the Player's trail.
            if p1_length < constants.MIN_TRAIL_LENGTH:
                p1.grow_trail(1)

        # ============ PLAYER TWO ============ #

        if self._keyboard_service.is_key_down('space'):
            p2 = cast.get_first_actor("player_2")
            p2_segments = p2.get_segments()
            p2_length = len(p2.get_segments())
            # Remove the Player's trail.
            if p2_length > 1:
                for segments in p2_segments:
                    p2.shrink_trail(1)
            # Reposition Player back to their starting positon.
            p2_head = p2.get_head()
            p2_start = p2.get_start_position()
            p2_head.set_position(p2_start)

        if self._keyboard_service.is_key_up('space'):
            p2 = cast.get_first_actor("player_2")
            p2_length = len(p2.get_segments())
            # Grow back the Player's trail.
            if p2_length < constants.MIN_TRAIL_LENGTH:
                p2.grow_trail(1)

class PrintPlayers(ControlActorsAction):
    """Print player details in the console log when pressing 'tab'.
    """
    def execute(self, cast, script):
        # ============ PLAYER ONE ============ #

        if self._keyboard_service.is_key_down('tab'):
            # Get Player_1 from Cast.
            p1 = cast.get_first_actor("player_1")
            p1_head = p1.get_head()
            p1_length = len(p1.get_segments())
            # Get Player_1 Position.
            p1_pos = p1_head.get_position()
            p1_x = p1_pos.get_x()
            p1_y = p1_pos.get_y()
            # Get Player_1 Color.
            p1_color = p1.get_color()
            p1_rgb = p1_color.to_tuple()
        
            # ============ PLAYER TWO ============ #

            # Get Player_2 from Cast.
            p2 = cast.get_first_actor("player_2")
            p2_head = p2.get_head()
            p2_length = len(p2.get_segments())
            # Get Player_2 Position.
            p2_pos = p2_head.get_position()
            p2_x = p2_pos.get_x()
            p2_y = p2_pos.get_y()

            # ============ BOTH ============ #
            collision = " "
            if p1_x == p2_x and p1_y == p2_y:
                collision = "*** @-Collision ***"
            elif p1_x == p2_x:
                collision = "*** X-Collision ***"
            elif p1_y == p2_y:
                collision = "*** Y-Collision ***"
            else:
                collision = " "
                
            print(f"(P1) Length = {p1_length}, Position = ({p1_x}, {p1_y}) || (P2) Length = {p2_length}, Position = ({p2_x}, {p2_y}), {collision}")

class ControlActorPlayerOne(ControlActorsAction):
    """Conrols the movement of Player One with W, A, S, D.
    """
    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
    
        player_1 = cast.get_first_actor("player_1")
        player_1.turn_head(self._direction)

class ControlActorPlayerTwo(ControlActorsAction):
    """Conrols the movement of Player Two with I, J, K, L.
    """
    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction = Point(constants.CELL_SIZE, 0)
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction = Point(0, -constants.CELL_SIZE)
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction = Point(0, constants.CELL_SIZE)

        player_2 = cast.get_first_actor("player_2")
        player_2.turn_head(self._direction)

