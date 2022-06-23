import constants

from game.casting.cast import Cast
from game.casting.players import PlayerOne
from game.casting.players import PlayerTwo
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorPlayerOne
from game.scripting.control_actors_action import ControlActorPlayerTwo
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("playerone", PlayerOne())
    cast.add_actor("playertwo", PlayerTwo())
    
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorPlayerOne(keyboard_service))
    script.add_action("input", ControlActorPlayerTwo(keyboard_service))
    script.add_action("update", MoveActorsAction())

    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()