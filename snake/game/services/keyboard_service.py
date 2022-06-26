import pyray
from game.shared.point import Point


class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.

    Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {}
        
        self._keys['w'] = pyray.KEY_W # P1 - Up
        self._keys['a'] = pyray.KEY_A # P1 - Left
        self._keys['s'] = pyray.KEY_S # P1 - Down
        self._keys['d'] = pyray.KEY_D # P1 - Right 

        self._keys['i'] = pyray.KEY_I # P2 - Up
        self._keys['j'] = pyray.KEY_J # P2 - Left
        self._keys['k'] = pyray.KEY_K # P2 - Down
        self._keys['l'] = pyray.KEY_L # P2 - Right

        self._keys['e'] = pyray.KEY_E # Player1 Boost
        self._keys['o'] = pyray.KEY_O # Player2 Boost

        self._keys['tab'] = pyray.KEY_TAB # ConsoleLog Help - Print Players
        self._keys['space'] = pyray.KEY_SPACE # Reset Game

    def is_key_up(self, key):
        """Checks if the given key is currently up.
        
        Args:
            key (string): The given key (w, a, s, d or i, j, k, l)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_down(self, key):
        """Checks if the given key is currently down.
        
        Args:
            key (string): The given key (w, a, s, d or i, j, k, l)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)