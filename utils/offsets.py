#!/usr/bin/env python3

# import requests
# import json

# we need these memory address offsets to read and write to the correct memory locations
# these may change depending on the game version,
# up to date versions can be found at:
# https://github.com/frk1/hazedumper/

# offsets = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
# response = requests.get(offsets).json()

# as of writing 16-12-2022 current repo is out of date, so using constants instead

dwGlowObjectManager = 0x535A9D8
dwEntityList = 0x4DFFF14
dwForceJump = 0x52BBC9C
dwLocalPlayer = 0xDEA964

m_iTeamNum = 0xF4
m_iGlowIndex = 0x10488
m_fFlags = 0x104
m_flFlashMaxAlpha = 0x1046C