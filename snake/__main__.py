import constants

from game.casting.cast import Cast
from game.casting.players import Players
from game.casting.score import Score
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorPlayerOne
from game.scripting.control_actors_action import ControlActorPlayerTwo
from game.scripting.control_actors_action import ResetActorPositions
from game.scripting.control_actors_action import PlayerTrailGrow
from game.scripting.control_actors_action import PrintPlayers
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
    # define the half-way point on the grid.
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    # create the players.
    player_1 = Players()
    player_2 = Players()
    cast.add_actor("player_1", player_1)
    cast.add_actor("player_2", player_2)
    # set the positon and color of each player. 
    player_1._prepare_body(300, y, constants.GREEN)
    player_2._prepare_body(600, y, constants.RED)

    # create the scoreboards for each player
    score_1 = Score()
    score_2 = Score()
    cast.add_actor("score_1", score_1)
    cast.add_actor("score_2", score_2)
    # set the positon and color of each scoreboard. 
    score_1._prepare_self(300, 0, constants.GREEN, "Player One")
    score_2._prepare_self(600, 0, constants.RED, "Player Two")

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorPlayerOne(keyboard_service))
    script.add_action("input", ControlActorPlayerTwo(keyboard_service))
    script.add_action("input", PlayerTrailGrow(keyboard_service))
    script.add_action("input", ResetActorPositions(keyboard_service))
    script.add_action("input", PrintPlayers(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()