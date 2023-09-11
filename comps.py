"""
Team composition used by the bot
Comps come from https://tftactics.gg/tierlist/team-comps
Items are in camel case and a-Z
"""
import set_9.comps.azir_nasus_lux_jarvan

COMP = set_9.comps.azir_nasus_lux_jarvan.COMP

AUGMENTS: set_9.comps.azir_nasus_lux_jarvan.AUGMENTS

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
