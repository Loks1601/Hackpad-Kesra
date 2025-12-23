import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import KeysScanner
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, TextEntry, ImageEntry

# ----------------------------
# 1. KEYBOARD SETUP
# ----------------------------
keyboard = KMKKeyboard()

# ----------------------------
# 2. BUTTON PIN DEFINITIONS
# ----------------------------
# 4-button macropad
PINS = [
    board.D0,  # SW1
    board.D1,  # SW2
    board.D2,  # SW3
    board.D3,  # SW4
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,  # Active LOW
    pull=True,                 # Enable internal pull-ups
    interval=0.02,             # Debounce (20 ms)
)

# ----------------------------
# 3. KEYMAP
# ----------------------------
# Layout:
# [ SW1 ] [ SW2 ]
# [ SW3 ] [ SW4 ]

keyboard.keymap = [
    [
        KC.A,      # SW1
        KC.B,      # SW2
        KC.C,      # SW3
        KC.D,      # SW4
    ]
]

# ----------------------------
# 4. START KEYBOARD
# ----------------------------
if __name__ == '__main__':
    keyboard.go()

