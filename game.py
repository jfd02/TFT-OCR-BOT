from time import sleep, perf_counter

import requests
import time
from pymem import Pymem
from world import find_pointers, find_game_time, find_local_net_id, find_view_proj_matrix, read_object, world_to_screen
from target import select_lowest_target
from constants import PROCESS_NAME

import arena_functions
import game_assets
import game_functions
import settings
import random
from arena import Arena
import mk_functions
import screen_coords


class Game:
    def __init__(self, message_queue):
        self.message_queue = message_queue
        self.arena = Arena(self.message_queue)
        self.round = "0-0"
        self.time = None
        self.forfeit_time = settings.forfeit_time + random.randint(50, 150)
        self.loading_screen()


    def loading_screen(self):
        game_functions.default_pos()
        while arena_functions.check_GameStart() is False:
            sleep(1)
        # while game_functions.get_round() != "1-1":
        #     sleep(1)
        self.start_time = perf_counter()
        self.game_loop()

    def game_loop(self):
        ran_round = None
        while game_functions.check_alive() or arena_functions.check_GameStart() is False:

            self.round = game_functions.get_round()

            if settings.forfeit is True:
                if perf_counter() - self.start_time > self.forfeit_time:
                    game_functions.forfeit()
                    return

            if self.round != ran_round and self.round in game_assets.carousel_rounds:
                self.carousel_round()
                ran_round = self.round
            elif self.round != ran_round and self.round in game_assets.pve_round:
                self.pve_round()
                self.pickup_items()
                ran_round = self.round
            elif self.round != ran_round and self.round in game_assets.pvp_round:
                self.pvp_round()
                self.pickup_items()
                ran_round = self.round


            sleep(0.5)
        game_functions.exit_game()

    def pickup_items(self):
        mem = Pymem(PROCESS_NAME)
        pickers = ["tft_itemunknown", "testcuberender"]
        pickers_pointers = find_pointers(mem, pickers)
        view_proj_matrix, width, height = find_view_proj_matrix(mem)
        # print(view_proj_matrix, width, height)
        for p in pickers_pointers:
            o = read_object(mem, p)
            x = None
            y = None
            x, y = world_to_screen(view_proj_matrix, width, height, o.x, o.z, o.y)
            if x is not None and y is not None:
                if x < 500:
                    return
                self.message_queue.put(("CONSOLE", f"Picking up items({int(x)}, {int(y)})"))
            while x is not None and y is not None and o.name != '':
                mk_functions.right_click((int(x), int(y)))
                sleep(0.5)
                o = read_object(mem, p)
                x = None
                y = None
                x, y = world_to_screen(view_proj_matrix, width, height, o.x, o.z, o.y)
                if x is None or x < 500:
                    return


    def carousel_round(self):
        if self.round == "3-4":
            self.arena.final_comp = True
        self.message_queue.put(("CONSOLE", f"[Carousel Round] {self.round}"))
        self.arena.check_health()
        self.message_queue.put(("CONSOLE", "Getting a champ from the carousel"))
        game_functions.get_champ_carousel(self.round)

    def pve_round(self):
        sleep(0.5)
        self.message_queue.put(("CONSOLE", f"[PvE Round] {self.round}"))

        if self.round in game_assets.augment_rounds:
            sleep(1)
            self.arena.pick_augment()
            sleep(2.5)  # Can't purchase champions for a short period after choosing augment
        elif self.round == "1-2":
            return
        elif self.round == "1-3":
            sleep(1)
            mk_functions.press_e(screen_coords.board_loc[3])
            # self.arena.fix_unknown()
            self.arena.tacticians_check()
        elif self.round == "2-7":
            self.arena.krug_round()

        self.arena.fix_board_state()
        self.arena.spend_gold()
        self.arena.move_champions()
        self.arena.replace_unknown()
        if self.arena.final_comp is True:
            self.arena.final_comp_check()
        self.arena.bench_cleanup()
        self.arena.check_health()
        self.arena.fix_board_state()
        self.arena.get_label()
        game_functions.default_pos()

    def pvp_round(self):
        sleep(0.5)
        self.message_queue.put(("CONSOLE", f"[PvP Round] {self.round}"))
        if self.round in game_assets.augment_rounds:
            sleep(1)
            self.arena.pick_augment()
            sleep(2.5)
        # elif self.round in game_assets.pickup_round:
        #     self.message_queue.put(("CONSOLE", f"Picking up items"))
        #     game_functions.pickup_items()

        self.arena.fix_board_state()
        self.arena.bench_cleanup()
        self.arena.spend_gold()
        self.arena.move_champions()
        self.arena.replace_unknown()
        if self.arena.final_comp is True:
            self.arena.final_comp_check()
        self.arena.bench_cleanup()
        self.arena.fix_board_state()
        if self.round in game_assets.item_placement_rounds:
            sleep(1)
            self.arena.place_items()
        self.arena.check_health()
        self.arena.fix_board_state()
        self.arena.get_label()
        game_functions.default_pos()
