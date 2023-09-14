"""
Handles tasks that happen each game round
"""

import multiprocessing
import random
from time import sleep, perf_counter

import win32gui

import arena_functions
import comps
from set_9_5 import game_assets
import game_functions
import mk_functions
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
        self.seconds_remaining_in_phase: int = -1

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
        # Make the bot play a random comp from the comps we have created.
        random_comp = comps.return_random_comp()
        comps.COMP = random_comp.COMP
        self.start_time: float = perf_counter()
        self.game_loop()

    def game_loop(self) -> None:
        """Loop that runs while the game is active, handles calling the correct tasks for round and exiting game"""
        ran_round: str = None
        while game_functions.check_alive():
            self.round: str = game_functions.get_round()

            # Display the seconds remaining for this phase in real time.
            self.seconds_remaining_in_phase: int = arena_functions.get_seconds_remaining()
            labels = [(f"{arena_functions.get_seconds_remaining()}",
                       screen_coords.SECONDS_REMAINING_UNTIL_NEXT_STEP_LOC.get_coords(), -40, -10)]
            self.message_queue.put(("LABEL", labels))

            if (
                    settings.FORFEIT
                    and perf_counter() - self.start_time > self.forfeit_time
            ):
                game_functions.forfeit()
                return

            if self.round != ran_round:
                if self.round in game_assets.SECOND_ROUND:
                    second_round_process = multiprocessing.Process(target=self.second_round(), name="Second Round", args=(30,))
                    second_round_process.start()
                    mk_functions.right_click(screen_coords.TACTICIAN_RESTING_SPOT_LOC.get_coords())
                    ran_round: str = self.round
                elif self.round in game_assets.THIRD_ROUND:
                    third_round_process = multiprocessing.Process(target=self.third_round(), name="Third Round", args=(30,))
                    third_round_process.start()
                    mk_functions.right_click(screen_coords.TACTICIAN_RESTING_SPOT_LOC.get_coords())
                    ran_round: str = self.round
                elif self.round in game_assets.CAROUSEL_ROUND:
                    carousel_round_process = multiprocessing.Process(target=self.carousel_round(), name="Carousel Round", args=(25,))
                    carousel_round_process.start()
                    mk_functions.right_click(screen_coords.TACTICIAN_RESTING_SPOT_LOC.get_coords())
                    ran_round: str = self.round
                elif self.round in game_assets.AUGMENT_ROUNDS:
                    game_functions.default_pos()
                    pve_round_process = multiprocessing.Process(target=self.pvp_round(), name="PvP Round", args=(50,))
                    pve_round_process.start()
                    mk_functions.right_click(screen_coords.TACTICIAN_RESTING_SPOT_LOC.get_coords())
                    ran_round: str = self.round
                elif self.round in game_assets.PVE_ROUND:
                    game_functions.default_pos()
                    pve_round_process = multiprocessing.Process(target=self.pve_round(), name="PvE Round", args=(15,))
                    pve_round_process.start()
                    mk_functions.right_click(screen_coords.TACTICIAN_RESTING_SPOT_LOC.get_coords())
                    ran_round: str = self.round
                elif self.round in game_assets.PVP_ROUND:
                    game_functions.default_pos()
                    pve_round_process = multiprocessing.Process(target=self.pvp_round(), name="PvP Round", args=(30,))
                    pve_round_process.start()
                    mk_functions.right_click(screen_coords.TACTICIAN_RESTING_SPOT_LOC.get_coords())
                    ran_round: str = self.round
            sleep(0.5)
        self.message_queue.put("CLEAR")
        game_functions.exit_game()

    def second_round(self) -> None:
        """ """
        print(f"\n\n[Second Round] {self.round}")
        self.print_arena_values()
        self.message_queue.put("CLEAR")
        sleep(1)
        self.arena.identify_champions_on_board()
        self.arena.identify_champions_on_bench()
        self.arena.move_champions()
        self.end_round_tasks()

    def third_round(self) -> None:
        """ """
        print(f"\n\n[Third Round] {self.round}")
        self.print_arena_values()
        self.message_queue.put("CLEAR")
        sleep(2)
        self.arena.identify_champions_on_board()
        self.arena.identify_champions_on_bench()
        self.arena.move_champions()
        self.end_round_tasks()

    def carousel_round(self) -> None:
        """Handles tasks for carousel rounds"""
        print(f"\n\n[Carousel Round] {self.round}")
        self.print_arena_values()
        self.message_queue.put("CLEAR")
        if self.round == "3-4":
            self.arena.final_comp = True
        self.arena.check_health()
        # There are 1 or more units on the board we don't know, so view our board instead of the carousel and identify
        # what units are on our board that we don't know about.
        # It's ok if our tactician gets a random item&champ chosen for it anyways,
        # because it picks a random one on its own.
        if self.arena.board_size > len(self.arena.board):
            print("    Moving our view from the carousel to the game board.")
            mk_functions.left_click(screen_coords.CAROUSEL_TO_BOARD_BUTTON_LOC.get_coords())
            valid_champs = self.arena.identify_unknown_champions_on_board()
            for name_and_pos in valid_champs:
                self.arena.create_champion_object_from_unit_name_on_the_board(name_and_pos[0], name_and_pos[1])
        else:
            print("  Getting a champ from the carousel")
            game_functions.get_champ_carousel(self.round)

    def pve_round(self) -> None:
        """Handles tasks for PVE rounds"""
        print(f"\n\n[PvE Round] {self.round}")
        self.print_arena_values()
        self.message_queue.put("CLEAR")
        sleep(1)
        if self.round in game_assets.AUGMENT_ROUNDS:
            sleep(1)
            self.arena.pick_augment(False, [])
            # Can't purchase champions for a short period after choosing augment
            sleep(2.5)

        # Have this happen after the augment selection.
        self.arena.identify_champions_on_board()
        self.arena.identify_champions_on_bench()

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
        elif self.arena.check_health() <= 15:
            self.arena.final_comp = True
        self.arena.bench_cleanup()
        self.end_round_tasks()

    def pvp_round(self) -> None:
        """Handles tasks for PVP rounds"""
        print(f"\n\n[PvP Round] {self.round}")
        self.print_arena_values()
        self.message_queue.put("CLEAR")
        sleep(1)
        print("  Checking health at the beginning of PvP Round, so I know how much health I have before shopping.")
        self.arena.check_health()
        if self.round in game_assets.AUGMENT_ROUNDS:
            sleep(1)
            self.arena.pick_augment(False, [])
            sleep(2.5)

        # Have this happen after the augment selection.
        self.arena.identify_champions_on_board()
        self.arena.identify_champions_on_bench()

        if self.round in ("2-1", "2-5"):
            arena_functions.buy_xp_round()
        if self.round in game_assets.PICKUP_ROUNDS:
            print("  Picking up items:")
            # game_functions.move_to_items_orbs_on_board()
            game_functions.pick_up_items_holding_down_right_click()

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
        elif self.arena.check_health() <= 15:
            self.arena.final_comp = True
        self.arena.bench_cleanup()

        if self.round in game_assets.ITEM_PLACEMENT_ROUNDS \
                or arena_functions.get_health() <= 15 or len(self.arena.items) >= 8:
            sleep(1)  # why do we sleep here?
            self.arena.place_items()
        self.end_round_tasks()

    def end_round_tasks(self) -> None:
        """Common tasks across rounds that happen at the end"""
        print(f"  Running end round tasks:")
        self.arena.check_health()
        self.arena.set_labels()
        self.print_arena_values()
        game_functions.default_pos()

    def print_arena_values(self):
        unit_names_on_entire_board = []
        for unit in self.arena.board:
            if unit is not None and isinstance(unit, Champion):
                unit_names_on_entire_board.append(unit.name)
            else:
                unit_names_on_entire_board.append(unit)
        print(f"-------------------------------------------")
        print(f"        Board: {unit_names_on_entire_board}")
        print(f"        Board Size: {self.arena.board_size}")
        print(f"        Board Names: {self.arena.board_names}")
        print(f"        Board Unknown: {self.arena.board_unknown}")
        print(f"        Board Unknown And Pos: {self.arena.board_unknown_and_pos}")
        print(f"        Board Slot For Non Comp Units: {self.arena.board_slots_for_non_comp_units}")
        unit_names_on_bench = []
        for unit in self.arena.bench:
            if unit is not None and isinstance(unit, Champion):
                unit_names_on_bench.append(unit.name)
            elif unit is not None:
                unit_names_on_bench.append(unit)
        print(f"        Bench: {unit_names_on_bench}")
        print(f"        Items: {[item for item in self.arena.items if item is not None]}")
        print(f"        Augments: {self.arena.augments}")
        print(f"        Level: {self.arena.level}")
        print(f"        Final Comp: {self.arena.final_comp}")
        print(f"        Augment Roll: {self.arena.augment_roll}")
        print(f"        Spam Roll: {self.arena.spam_roll}")
        print(f"        Spam Roll To Zero: {self.arena.spam_roll_to_zero}")
        print(f"-------------------------------------------")
