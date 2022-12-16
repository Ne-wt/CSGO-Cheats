#!/usr/bin/env python3

import utils.offsets as offsets
from utils.client_info import client, csgo

# This script currently does not work as of 16-12-2022
# it is included here only as an example of work, until I perhaps find the time to fix it

def glow():
    # find glow manager using the client module and dwGlowObjectManager
    # this uses pymem to access the specific memory byte above within the client module
    glow_manager = csgo.read_int(client + offsets.dwGlowObjectManager)

    # loop through all entities
    for i in range(1, 32): # entities 1-32 are reserved for players
        # get the entity
        try:
            entity = csgo.read_int(client + offsets.dwEntityList + i * 0x10)
        except:
            print(">>> Error reading entity from list.")

        # if the entity is valid
        if entity:
            # get the entity's team number
            try:
                entity_team_id = csgo.read_uint(entity + offsets.m_iTeamNum)
                # get the entity's glow index
            except:
                print(">>> Error reading entity team number.")
                continue

            entity_glow = csgo.read_uint(entity + offsets.m_iGlowIndex * 0x10)
            
                # check the entity's team number
            if entity_team_id == 2: # if the entity is on the terrorist side
                # set the outline to be red
                csgo.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1))   # Red (100% strength)
                csgo.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # Green
                csgo.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0))  # Blue
                ########################################################################################
                csgo.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))  # Alpha (opacity)
                csgo.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)           # Enable glow

            elif entity_team_id == 3:  # Counter-terrorist
                csgo.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))   # R
                csgo.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # G
                csgo.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))  # B
                csgo.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))  # Alpha
                csgo.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)           # Enable glow