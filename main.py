#!/usr/bin/env python3

# imports
import keyboard
from win32gui import GetWindowText, GetForegroundWindow

print('>>> Importing Offsets...')

import utils.offsets as offsets

print('>>> Initialising Packages...')

from packages.bhop import bhop
from packages.no_flash import no_flash
from packages.trigger import trigger
from packages.glow import glow

# ------------------------------ main ------------------------------ #

def main():

    print(">>> Launching...")

    game_names = [
        "Counter-Strike: Global Offensive - Direct3D 9",
        "Counter-Strike: Global Offensive"   
    ]

    while True:
        # basic exit script
        if keyboard.is_pressed('del') or keyboard.is_pressed('esc'):
            exit()

        # most scripts check if we're in game anyway 
        # but to prevent terminal flood of messages
        if GetWindowText(GetForegroundWindow()) not in game_names:
            continue

        # stuff that runs every loop
        no_flash()

        glow()

        # stuff that runs when a key is pressed
        if keyboard.is_pressed('space'):
            bhop()

        if keyboard.is_pressed('shift'):
            trigger()

if __name__ == '__main__':
    main()