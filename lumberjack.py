# -*- coding: utf-8 -*-
"""lumberjack.py

Silly scripts that plays Telegram's "lumberjack" game
and basically destroys all your friend's records.
"""
import time
from ctypes import windll
from pynput.keyboard import Key, Controller

# Game lumber's RGB color
LUMBER_COLOR = (161, 116, 56)

# Some delays in seconds
KEYBOARD_DELAY = 0.05
START_DELAY = 3

dc = windll.user32.GetDC(0)

# Lumber positions for a 1920x1080 screen
keys = {
    Key.left: (889, 430),
    Key.right: (1027, 430)
}

def getpixel(x,y):
    """Return an RGB tuple

    Way faster method than PIL's to return a given pixel's RGB color
    Props to: https://stackoverflow.com/questions/1997678/faster-method-of-reading-screen-pixel-in-python-than-pil
    """
    return tuple(int.to_bytes(windll.gdi32.GetPixel(dc,x,y), 3, "little"))

def play():
    """
    Play the game and shame your friends
    """

    print("Staring in %s seconds... switch to game now!" % START_DELAY)
    time.sleep(START_DELAY)

    # Controller to press keys
    keyboard = Controller()

    # Default key at start
    current_key = Key.left

    # Loop that checks for incoming lumber pixels
    # and switches to the other side
    while True:
        time.sleep(KEYBOARD_DELAY)

        if getpixel(keys[current_key][0], keys[current_key][1]) == LUMBER_COLOR:
            # Switch keys
            current_key = Key.right if current_key == Key.left else Key.left

        # Press either left or right directionals
        keyboard.press(current_key)
        keyboard.release(current_key)

if __name__ == "__main__":
    play()