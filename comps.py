"""
Team composition used by the bot
Items are in camel case and a-Z
Strategies:
    Default: This comp uses the standard leveling strategy that revolves around a 4-cost carry.
    Fast 8: This comp looks to level up to 8 aggressively with a strong economy.
    Slow Roll: This comp rolls gold above 50 to look for 3-star champions.
"""
import set_9_5.comps.arcane_domain_jayce_vi_silco as arcane_domain
import set_9_5.comps.heart_of_the_cards_twisted_fate_illaoi_nilah_miss_fortune as heart_of_the_cards
import set_9_5.comps.roll_the_rogues_ekko_qiyana_katarina as roll_the_rogues
import set_9_5.comps.walk_the_plank_nilah_miss_fortune_gangplank_nautilus as walk_the_plank
import set_9_5.comps.super_nash_bros_kaisa_chogath_belveth as super_nash_bros
import set_9_5.comps.milio_cr7_shen_taric_ryze as milio_cr7
import set_9_5.comps.bastion_barrage_aphelios_shen_silco as bastion_barrage
import set_9_5.comps.bruiser_bites_malzahar_chogath_reksai as bruiser_bites
import set_9_5.comps.noxus_rolls_samira_swain_mordekaiser_naafiri as noxus_rolls
import random

COMPS_TO_SELECT_RANDOMLY_FROM: list = [bruiser_bites, noxus_rolls]


def return_random_comp():
    return random.choice(COMPS_TO_SELECT_RANDOMLY_FROM)


class Comp:

    def __init__(self, composition):
        # The name we have given the comp.
        self.name: str = composition.NAME
        # Do we play Normal? Do we go Fast 8? Do we Slow Roll?
        self.strategy: str = composition.STRATEGY
        # How difficult it is to obtain all the units and items.
        self.difficulty_to_play: str = composition.DIFFICULTY
        # The traits that are being used when the final version of the comp is in play.
        self.active_final_comp_traits: list = composition.ACTIVE_FINAL_COMP_TRAITS
        # The traits that are inactive when the final version of the comp is in play.
        self.inactive_final_comp_traits: list = composition.INACTIVE_FINAL_COMP_TRAITS
        # The legend that was recommended by whatever website the comp is from.
        self.recommended_legend: str = composition.RECOMMENDED_LEGEND
        self.comp: dict = composition.COMP
        self.primary_augments: list = composition.PRIMARY_AUGMENTS
        self.secondary_augments: list = composition.SECONDARY_AUGMENTS

    def champions_to_buy(self) -> list[str]:
        """Creates a list of champions to buy during the game"""
        champs_to_buy: list[str] = []
        for champion, champion_data in self.comp.items():
            if champion_data["level"] == 1:
                champs_to_buy.append(champion)
            elif champion_data["level"] == 2:
                champs_to_buy.extend([champion] * 3)
            elif champion_data["level"] == 3:
                champs_to_buy.extend([champion] * 9)
            else:
                raise ValueError("Comps.py | Champion level must be a valid level (1-3)")
        return champs_to_buy

    def get_unknown_slots(self) -> list:
        """Creates a list of slots on the board that don't have a champion from the team composition"""
        container: list = []
        for _, champion_data in self.comp.items():
            container.append(champion_data["board_position"])
        return [n for n in range(27) if n not in container]
