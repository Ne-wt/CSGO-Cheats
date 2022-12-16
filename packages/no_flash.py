#!/usr/bin/env python3

import utils.offsets as offsets
from utils.client_info import csgo, get_player

def no_flash():
    # no flash
    player = get_player()
    if player:
        flash_value = player + offsets.m_flFlashMaxAlpha

        # if player is flashed
        if flash_value:
            csgo.write_float(flash_value, float(0))