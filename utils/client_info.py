#!/usr/bin/env python3

import pymem
import pymem.process
import time
import utils.offsets as offsets

# get the process csgo
try:
    csgo = pymem.Pymem("csgo.exe")
# if we can't find the process, exit
except pymem.exception.ProcessNotFound:
    # print error message
    print(">>> CSGO not found.")
    exit()

def find(name):
    # find memory location of specified DLL files, 
    # this allows us to figure out the offsets of loaded in objects like players
    return pymem.process.module_from_name(csgo.process_handle, name).lpBaseOfDll

def get_player():
    try:
        return csgo.read_int(client + offsets.dwLocalPlayer)
    except:
        # if we can't find the player we are probably not in a game.
        print(">>> Error reading local player.")
        # sleep for 5 seconds to allow time for the user to launch and stop terminal spam.
        time.sleep(5)
        return

def get_player_team():
    try:
        player = get_player()
        return csgo.read_int(player + offsets.m_iTeamNum)
    except:
        # if we can't find the player we are probably not in a game.
        print(">>> Error reading local player team.")
        # sleep for 5 seconds to allow time for the user to launch and stop terminal spam.
        time.sleep(5)
        return


client = find("client.dll")
engine = find("engine.dll")