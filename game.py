"""
Handles tasks that happen each game round
"""

from time import sleep, perf_counter
import random
import win32gui
import settings
import game_assets
import game_functions
from arena import Arena
import vec4
import vec2

class Game:
    def __init__(self, message_queue):
        self.message_queue = message_queue
        self.arena = Arena(self.message_queue)
        self.round = "0-0"
        self.time = None
        self.forfeit_time = settings.FORFEIT_TIME + random.randint(50, 150)
        self.found_window = False

        while not self.found_window:
            print("Did not find window, trying again...")
            win32gui.EnumWindows(self.callback, None)
            sleep(1)

        self.loading_screen()

    def callback(self, hwnd, extra):
        if "League of Legends (TM) Client" not in win32gui.GetWindowText(hwnd):
            return

        rect = win32gui.GetWindowRect(hwnd)

        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y

        if w < 200 or h < 200:
            return

        print(f"Window {win32gui.GetWindowText(hwnd)} found")
        print(f"  Location: ({x}, {y})")
        print(f"  Size:     ({w}, {h})")
        vec4.vec4.setup_screen(x, y, w, h)
        vec2.vec2.setup_screen(x, y, w, h)
        self.found_window = True
        
    def loading_screen(self):
        game_functions.default_pos()
        while game_functions.get_round() != "1-1":
            sleep(1)
        self.start_time = perf_counter()
        self.game_loop()

    def game_loop(self):
        ran_round = None
        while game_functions.check_alive():
            self.round = game_functions.get_round()

            if settings.FORFEIT is True:
                if perf_counter() - self.start_time > self.forfeit_time:
                    game_functions.forfeit()
                    return

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
        elif self.round == "1-3":
            sleep(1.5)
            self.arena.fix_unknown()
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
        self.arena.get_label()
        game_functions.default_pos()

    def pvp_round(self):
        sleep(0.5)
        self.message_queue.put(("CONSOLE", f"[PvP Round] {self.round}"))
        if self.round in game_assets.augment_rounds:
            sleep(1)
            self.arena.pick_augment()
            sleep(2.5)
        if self.round in game_assets.pickup_round:
            self.message_queue.put(("CONSOLE", "Picking up items"))
            game_functions.pickup_items()

        self.arena.fix_board_state()
        self.arena.bench_cleanup()
        self.arena.spend_gold()
        self.arena.move_champions()
        self.arena.replace_unknown()
        if self.arena.final_comp is True:
            self.arena.final_comp_check()
        self.arena.bench_cleanup()

        if self.round in game_assets.item_placement_rounds:
            sleep(1)
            self.arena.place_items()
        self.arena.check_health()
        self.arena.get_label()
        game_functions.default_pos()
