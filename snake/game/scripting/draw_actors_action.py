from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        playerone = cast.get_first_actor("playerone")
        playertwo = cast.get_first_actor("playertwo")
        p1_segments = playerone.get_segments()
        p2_segments = playertwo.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actors(p1_segments)
        self._video_service.draw_actors(p2_segments)
        self._video_service.draw_actor(playerone)
        self._video_service.draw_actor(playertwo)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()