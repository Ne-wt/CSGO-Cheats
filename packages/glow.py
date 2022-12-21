#!/usr/bin/env python3

import utils.offsets as offsets
from utils.client_info import client, csgo, get_player_team

# reference: https://github.com/barisbored/hammer-csgo-hack/blob/main/packages/glow.py

def write_glow(glow_manager, glow_index, colours):
    csgo.write_float(glow_manager + ((glow_index * 0x38) + 0x8), colours["red"])
    csgo.write_float(glow_manager + ((glow_index * 0x38) + 0xC), colours["green"])
    csgo.write_float(glow_manager + ((glow_index * 0x38) + 0x10), colours["blue"])
    csgo.write_float(glow_manager + ((glow_index * 0x38) + 0x14), colours["opacity"])
    csgo.write_int(glow_manager + ((glow_index * 0x38) + 0x28), 1) 


def glow():
    glow_manager = csgo.read_bytes(client + offsets.dwGlowObjectManager, 4)
    glow_manager = int.from_bytes(glow_manager, byteorder="little")

    for i in range(1, 32):

        entity = csgo.read_bytes(client + offsets.dwEntityList + i * 0x10, 4)
        entity = int.from_bytes(entity, byteorder="little")

        if entity != 0:
            entity_team_id = csgo.read_int(entity + offsets.m_iTeamNum)
            glow_index = csgo.read_int(entity + offsets.m_iGlowIndex)

            player_team_id = get_player_team()

            if entity_team_id != player_team_id:
                write_glow(glow_manager, glow_index, offsets.enemy_glow)