# Expose clock API as a builtin
from . import clock
from . import music
from . import tone
from .actor import Actor
from .storage import storage
from .keyboard import keyboard
from .animation import animate
from .rect import Rect, ZRect

from .loaders import images, sounds

from .constants import mouse, keys, keymods

from .game import exit

__all__ = [
    'Actor', 'images',  # graphics
    'sounds', 'music', 'tone',  # sound
    'clock', 'animate',  # timing
    'Rect', 'ZRect',  # geometry
    'keyboard', 'mouse', 'keys', 'keymods',  # input
    'storage',  # persistence
    'exit',
]
