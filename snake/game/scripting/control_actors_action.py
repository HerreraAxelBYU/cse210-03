import constants
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
    
        player_one = cast.get_first_actor("playerone")
        player_one.turn_head(self._direction)

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

        player_two = cast.get_first_actor("playertwo")
        player_two.turn_head(self._direction)


class ResetActorPositions(ControlActorsAction):
    """ 
    Reset the positions of both players when pressing 'space'.
    """

    def execute(self, cast, script):
        
        if self._keyboard_service.is_key_down('space'):

            player_one = cast.get_first_actor("playerone")
            player_one.grow_trail(1)