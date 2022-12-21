import time
import keyboard
from utils.client_info import client, csgo, get_player
import utils.offsets as offsets


def trigger():
    player = get_player()

    if player:

        entity_id = csgo.read_int(player + offsets.m_iCrosshairId)
        entity = csgo.read_int(client + offsets.dwEntityList + (entity_id - 1) * 0x10)

        if entity:
            try:
                entity_team = csgo.read_int(entity + offsets.m_iTeamNum)
                player_team = csgo.read_int(player + offsets.m_iTeamNum)
            except:
                return
            
            if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                csgo.write_int(client + offsets.dwForceAttack, 6)

            time.sleep(0.01)