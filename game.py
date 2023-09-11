"""
Handles tasks that happen each game round
"""

import multiprocessing
import random
from time import sleep, perf_counter

import win32gui

import arena_functions
import game_assets
import game_functions
import screen_coords
import settings
from arena import Arena
from champion import Champion
from vec2 import Vec2
from vec4 import Vec4


class Game:
    """Game class that handles game logic such as round tasks"""

    def __init__(self, message_queue: multiprocessing.Queue) -> None:
        self.start_time = None
        self.message_queue = message_queue
        self.arena = Arena(self.message_queue)
        self.round = "0-0"
        self.time: None = None
        self.forfeit_time: int = settings.FORFEIT_TIME + random.randint(50, 150)
        self.found_window = False

        print("\n[!] Searching for game window")
        while not self.found_window:
            print("  Did not find window, trying again...")
            win32gui.EnumWindows(self.callback, None)
            sleep(1)

        self.loading_screen()

    def callback(self, hwnd, extra) -> None:  # pylint: disable=unused-argument
        """Function used to find the game window and get its size"""
        if "League of Legends (TM) Client" not in win32gui.GetWindowText(hwnd):
            return

        rect = win32gui.GetWindowRect(hwnd)

        x_pos = rect[0]
        y_pos = rect[1]
        width = rect[2] - x_pos
        height = rect[3] - y_pos

        if width < 200 or height < 200:
            return

        print(f"  Window {win32gui.GetWindowText(hwnd)} found")
        print(f"    Location: ({x_pos}, {y_pos})")
        print(f"    Size:     ({width}, {height})")
        Vec4.setup_screen(x_pos, y_pos, width, height)
        Vec2.setup_screen(x_pos, y_pos, width, height)
        self.found_window = True

    def loading_screen(self) -> None:
        """Loop that runs while the game is in the loading screen"""
        game_functions.default_pos()
        while game_functions.get_round() != "1-1":
            sleep(1)
        print("\n\nStarting match...")
        self.start_time: float = perf_counter()
        self.game_loop()

    def game_loop(self) -> None:
        """Loop that runs while the game is active, handles calling the correct tasks for round and exiting game"""
        ran_round: str = None
        while game_functions.check_alive():
            self.round: str = game_functions.get_round()

            # Display the seconds remaining for this phase in real time.
            self.time: int = arena_functions.get_seconds_remaining()
            labels = [(f"{arena_functions.get_seconds_remaining()}",
                       screen_coords.SECONDS_REMAINING_UNTIL_NEXT_STEP_LOC.get_coords(), 0, 0)]
            self.message_queue.put(("LABEL", labels))

            if (
                    settings.FORFEIT
                    and perf_counter() - self.start_time > self.forfeit_time
            ):
                game_functions.forfeit()
                return

            if self.round != ran_round:
                if self.round in game_assets.SECOND_ROUND:
                    self.second_round()
                    self.arena.identify_champions_on_board()
                    self.arena.identify_champions_on_bench()
                    ran_round: str = self.round
                elif self.round in game_assets.CAROUSEL_ROUND:
                    self.carousel_round()
                    ran_round: str = self.round
                elif self.round in game_assets.PVE_ROUND:
                    self.arena.identify_champions_on_board()
                    self.arena.identify_champions_on_bench()
                    game_functions.default_pos()
                    self.pve_round()
                    ran_round: str = self.round
                elif self.round in game_assets.PVP_ROUND:
                    self.arena.identify_champions_on_board()
                    self.arena.identify_champions_on_bench()
                    game_functions.default_pos()
                    self.pvp_round()
                    ran_round: str = self.round
            sleep(0.5)
        self.message_queue.put("CLEAR")
        game_functions.exit_game()

    def second_round(self) -> None:
        """Move unknown champion to board after first carousel"""
        print(f"\n[Second Round] {self.round}")
        self.message_queue.put("CLEAR")
        self.arena.bench[0] = "?"
        self.arena.move_unknown()
        self.end_round_tasks()

    def carousel_round(self) -> None:
        """Handles tasks for carousel rounds"""
        print(f"\n[Carousel Round] {self.round}")
        self.message_queue.put("CLEAR")
        if self.round == "3-4":
            self.arena.final_comp = True
        self.arena.check_health()
        print("  Getting a champ from the carousel")
        game_functions.get_champ_carousel(self.round)

    def pve_round(self) -> None:
        """Handles tasks for PVE rounds"""
        print(f"\n[PvE Round] {self.round}")
        self.print_arena_values()
        self.message_queue.put("CLEAR")
        sleep(0.5)
        if self.round in game_assets.AUGMENT_ROUNDS:
            sleep(1)
            self.arena.pick_augment()
            # Can't purchase champions for a short period after choosing augment
            sleep(2.5)
        if self.round == "1-3":
            sleep(1.5)
            self.arena.fix_unknown()
            # self.arena.tacticians_crown_check() #not getting any item in set9 round 1-3, skipped

        self.arena.fix_bench_state()
        self.arena.spend_gold()
        self.arena.move_champions()
        self.arena.replace_unknown()
        self.arena.replace_units_not_in_our_comp()
        if self.arena.final_comp:
            self.arena.final_comp_check()
        self.arena.bench_cleanup()
        self.end_round_tasks()

    def pvp_round(self) -> None:
        """Handles tasks for PVP rounds"""
        print(f"\n[PvP Round] {self.round}")
        self.print_arena_values()
        self.message_queue.put("CLEAR")
        sleep(0.5)
        print("  Checking health at the beginning of PvP Round, so I know how much health I have before shopping.")
        self.arena.check_health()
        if self.round in game_assets.AUGMENT_ROUNDS:
            sleep(1)
            self.arena.pick_augment()
            sleep(2.5)
        if self.round in ("2-1", "2-5"):
            arena_functions.buy_xp_round()
        if self.round in game_assets.PICKUP_ROUNDS:
            print("  Picking up items:")
            # game_functions.move_to_items_orbs_on_board()
            game_functions.pickup_items()

        self.arena.fix_bench_state()
        self.arena.bench_cleanup()
        if self.round in game_assets.ANVIL_ROUNDS:
            self.arena.clear_anvil()
        self.arena.spend_gold()
        self.arena.move_champions()
        self.arena.replace_unknown()
        self.arena.replace_units_not_in_our_comp()
        if self.arena.final_comp:
            self.arena.final_comp_check()
        self.arena.bench_cleanup()

        if self.round in game_assets.ITEM_PLACEMENT_ROUNDS or arena_functions.get_health() <= 15:
            sleep(1)
            self.arena.place_items()
        self.end_round_tasks()

    def end_round_tasks(self) -> None:
        """Common tasks across rounds that happen at the end"""
        print(f"  Running end round tasks:")
        self.arena.check_health()
        self.arena.set_labels()
        game_functions.default_pos()

    def print_arena_values(self):
        #print(f"    Board: {self.arena.board}")
        print(f"    Board Size: {self.arena.board_size}")
        print(f"    Board Names: {self.arena.board_names}")
        print(f"    Board Unknown: {self.arena.board_unknown}")
        print(f"    Board Slot For Non Comp Units: {self.arena.board_slots_for_non_comp_units}")
        unit_names_on_bench = []
        for unit in self.arena.bench:
            if unit is not None and isinstance(unit, Champion):
                unit_names_on_bench.append(unit.name)
        print(f"    Bench: {unit_names_on_bench}")
        print(f"    Items: {[item for item in self.arena.items if item is not None]}")
        print(f"    Augments: {self.arena.augments}")
        print(f"    Level: {self.arena.level}")
        print(f"    Final Comp: {self.arena.final_comp}")
        print(f"    Augment Roll: {self.arena.augment_roll}")
        print(f"    Spam Roll: {self.arena.spam_roll}")
        print(f"    Spam Roll To Zero: {self.arena.spam_roll_to_zero}")