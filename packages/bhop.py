#!/usr/bin/env python3

import utils.offsets as offsets
from utils.client_info import client, csgo, get_player

def bhop():
    player = get_player()
    if player:
        # if we cant find player flags we can't do much
        # flags indicate the state of the player in game
        try:
            on_ground = csgo.read_int(player + offsets.m_fFlags)
        except:
            print(">>> Error reading player flags.")
            return
        if on_ground and on_ground == 257 or on_ground == 263:
            csgo.write_int(client + offsets.dwForceJump, 6)