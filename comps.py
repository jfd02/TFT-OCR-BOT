"""
Team composition used by the bot
Items are in camel case and a-Z
Strategies:
    Default: This comp uses the standard leveling strategy that revolves around a 4-cost carry.
    Fast 8: This comp looks to level up to 8 aggressively with a strong economy.
    Slow Roll: This comp rolls gold above 50 to look for 3-star champions.
"""
import set_9.comps.azir_nasus_lux_jarvan_spear_and_shield
import set_9.comps.ekko_katarina_lissandra_icy_rogues
import set_9.comps.reksai_kaisa_sejuani_furious_bite

COMP = set_9.comps.azir_nasus_lux_jarvan_spear_and_shield.COMP

AUGMENTS = set_9.comps.azir_nasus_lux_jarvan_spear_and_shield.AUGMENTS

def champions_to_buy() -> list:
    """Creates a list of champions to buy during the game"""
    champs_to_buy: list = []
    for champion, champion_data in COMP.items():
        if champion_data["level"] == 1:
            champs_to_buy.append(champion)
        elif champion_data["level"] == 2:
            champs_to_buy.extend([champion] * 3)
        elif champion_data["level"] == 3:
            champs_to_buy.extend([champion] * 9)
        else:
            raise ValueError("Comps.py | Champion level must be a valid level (1-3)")
    return champs_to_buy


def get_unknown_slots() -> list:
    """Creates a list of slots on the board that don't have a champion from the team composition"""
    container: list = []
    for _, champion_data in COMP.items():
        container.append(champion_data["board_position"])
    return [n for n in range(27) if n not in container]
