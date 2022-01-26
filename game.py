from time import sleep

import game_assets
import game_functions
from arena import Arena


class Game:
    def __init__(self):
        self.arena = Arena()
        self.round = "0-0"

    def loading_screen(self):
        game_functions.default_pos()
        while game_functions.get_round() != "1-1":
            sleep(1)
        print("\n[game.py game_loop()] We are now in game")
        self.game_loop()

    def game_loop(self):
        ran_round = None
        while game_functions.check_alive():
            self.round = game_functions.get_round()

            if self.round != ran_round and self.round in game_assets.carousel_rounds:
                self.carousel_round()
                ran_round = self.round
            elif self.round != ran_round and self.round in game_assets.pve_round:
                self.pve_round()
                ran_round = self.round
            elif self.round != ran_round and self.round in game_assets.pvp_round:
                self.pvp_round()
                ran_round = self.round
            sleep(0.5)
        game_functions.exit_game()

    def carousel_round(self):
        if self.round == "3-4":
            self.arena.final_comp = True

        print(f"\n[Carousel Round] {self.round}")
        print("\tGetting a champ from the carousel")
        game_functions.get_champ_carousel(self.round)

    def pve_round(self):
        sleep(0.5)
        print(f"\n[PvE Round] {self.round}")

        if self.round in game_assets.augment_rounds:
            sleep(1)
            self.arena.pick_augment()
            sleep(2.5)  # Can't purchase champions for a short period after choosing augment
        elif self.round == "1-3":
            sleep(1.5)
            self.arena.fix_unknown()
            self.arena.tacticians_check()
        elif self.round == "2-7":
            self.arena.krug_round()

        self.arena.update_health()
        self.arena.fix_board_state()
        self.arena.spend_gold()
        self.arena.move_champions()
        if self.arena.final_comp is True:
            self.arena.final_comp_check()
        self.arena.replace_unknown()
        self.arena.bench_cleanup()
        self.arena.print_arena_state()
        game_functions.default_pos()

    def pvp_round(self):
        sleep(0.5)
        print(f"\n[PvP Round] {self.round}")
        if self.round in game_assets.augment_rounds:
            sleep(1)
            self.arena.pick_augment()
            sleep(2.5)
        elif self.round in game_assets.pickup_round:
            game_functions.pickup_items()

        self.arena.update_health()
        self.arena.fix_board_state()
        self.arena.spend_gold()
        self.arena.move_champions()
        if self.arena.final_comp is True:
            self.arena.final_comp_check()
        self.arena.replace_unknown()
        self.arena.bench_cleanup()

        if self.round in game_assets.item_placement_rounds:
            sleep(1)
            self.arena.place_items()
        self.arena.print_arena_state()
        game_functions.default_pos()
