import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.scripting.move_actors_action import MoveActorsAction

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._p1_victory = False
        self._p2_victory = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        playerone = cast.get_first_actor("playerone")
        p1_bike = playerone.get_segments()[0]
        p1_segments = playerone.get_segments()[1:]

        playertwo = cast.get_first_actor("playertwo")
        p2_bike = playertwo.get_segments()[0]
        p2_segments = playertwo.get_segments()[1:]
        
        # If Player One collides with itself or with Player Two...
        for segment in p1_segments:
            if p1_bike.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._p2_victory = True
            if p2_bike.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._p1_victory = True
        # If Player Two collides with itself or with Player One...
        for segment in p2_segments:
            if p2_bike.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._p1_victory = True
            if p1_bike.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._p2_victory = True

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            playerone = cast.get_first_actor("playerone")
            p1_all_segments = playerone.get_segments()
            playertwo = cast.get_first_actor("playertwo")
            p2_all_segments = playertwo.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            if self._p1_victory == True:
                message.set_text("Player One Wins!")
                for segment in p2_all_segments:
                    segment.set_color(constants.WHITE)

            elif self._p2_victory == True:
                message.set_text("Player Two Wins!")
                for segment in p1_all_segments:
                    segment.set_color(constants.WHITE)
