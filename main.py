"""
Where the bot execution starts & contains the game loop that keeps the bot running indefinitely
"""

import ctypes
import sys
import multiprocessing
import os
import time
import auto_comps
import auto_queue
from settings import LEAGUE_CLIENT_PATH
from comps import CompsManager
from game import Game
from ui import UI

# Constants for user choices
YES_CHOICES = ["yes", "y"]
NO_CHOICES = ["no", "n"]


def game_loop(ui_queue: multiprocessing.Queue, comps: CompsManager) -> None:
    """Keeps the program running indefinitely by calling queue and game start in a loop"""
    while True:
        auto_queue.handle_queue()
        Game(ui_queue, comps)


def is_admin():
    """Check if bot is running as admin to prevent bot can't move in-game"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:  # pylint: disable=bare-except
        return False


def check_league_client_path():
    """Check if League of Legends client path is specified."""
    if LEAGUE_CLIENT_PATH is None:
        print(
            "No League of Legends client path specified. Please set the path in settings.py"
        )
        raise ValueError(
            "No League of Legends client path specified. Please set the path in settings.py"
        )


def load_champions_data() -> dict:
    """Load champions data from a file or other source."""
    champions_data = {
    "Aatrox":{"Gold":2,"Board Size":1,"Trait1":"Ghostly","Trait2":"Bruiser","Trait3":"Inkshadow"},
    "Ahri":{"Gold":1,"Board Size":1,"Trait1":"Fated","Trait2":"Arcanist","Trait3":""},
    "Alune":{"Gold":3,"Board Size":1,"Trait1":"Umbral","Trait2":"Invoker","Trait3":""},
    "Amumu":{"Gold":3,"Board Size":1,"Trait1":"Porcelain","Trait2":"Warden","Trait3":""},
    "Annie":{"Gold":4,"Board Size":1,"Trait1":"Fortune","Trait2":"Invoker","Trait3":""},
    "Aphelios":{"Gold":3,"Board Size":1,"Trait1":"Fated","Trait2":"Sniper","Trait3":""},
    "Ashe":{"Gold":4,"Board Size":1,"Trait1":"Porcelain","Trait2":"Sniper","Trait3":""},
    "Azir":{"Gold":5,"Board Size":1,"Trait1":"Dryad","Trait2":"Invoker","Trait3":""},
    "Bard":{"Gold":3,"Board Size":1,"Trait1":"Mythic","Trait2":"Trickshot","Trait3":""},
    "Caitlyn":{"Gold":1,"Board Size":1,"Trait1":"Ghostly","Trait2":"Sniper","Trait3":""},
    "Cho'Gath":{"Gold":1,"Board Size":1,"Trait1":"Mythic","Trait2":"Behemoth","Trait3":""},
    "Darius":{"Gold":1,"Board Size":1,"Trait1":"Umbral","Trait2":"Duelist","Trait3":""},
    "Diana":{"Gold":3,"Board Size":1,"Trait1":"Dragonlord","Trait2":"Sage","Trait3":""},
    "Galio":{"Gold":4,"Board Size":1,"Trait1":"Storyweaver","Trait2":"Bruiser","Trait3":""},
    "Garen":{"Gold":1,"Board Size":1,"Trait1":"Storyweaver","Trait2":"Warden","Trait3":""},
    "Gnar":{"Gold":2,"Board Size":1,"Trait1":"Dryad","Trait2":"Warden","Trait3":""},
    "Hwei":{"Gold":5,"Board Size":1,"Trait1":"Mythic","Trait2":"Artist","Trait3":""},
    "Illaoi":{"Gold":3,"Board Size":1,"Trait1":"Ghostly","Trait2":"Arcanist","Trait3":"Warden"},
    "Irelia":{"Gold":5,"Board Size":1,"Trait1":"Storyweaver","Trait2":"Duelist","Trait3":""},
    "Janna":{"Gold":2,"Board Size":1,"Trait1":"Dragonlord","Trait2":"Invoker","Trait3":""},
    "Jax":{"Gold":1,"Board Size":1,"Trait1":"Inkshadow","Trait2":"Warden","Trait3":""},
    "Kai'Sa":{"Gold":4,"Board Size":1,"Trait1":"Inkshadow","Trait2":"Trickshot","Trait3":""},
    "Kayn": {"Gold": 4, "Board Size": 1, "Trait1": "Ghostly", "Trait2": "Reaper", "Trait3": ""},
    "Kha'Zix": {"Gold": 1, "Board Size": 1, "Trait1": "Heavenly", "Trait2": "Reaper", "Trait3": ""},
    "Kindred": {"Gold": 2, "Board Size": 1, "Trait1": "Dryad", "Trait2": "Fated", "Trait3": "Reaper"},
    "Kobuko": {"Gold": 1, "Board Size": 1, "Trait1": "Fortune", "Trait2": "Bruiser", "Trait3": ""},
    "Kog'Maw": {"Gold": 1, "Board Size": 1, "Trait1": "Mythic", "Trait2": "Invoker", "Trait3": "Sniper"},
    "LeeSin": {"Gold": 4, "Board Size": 1, "Trait1": "Dragonlord", "Trait2": "Duelist", "Trait3": ""},
    "Lillia": {"Gold": 4, "Board Size": 1, "Trait1": "Mythic", "Trait2": "Invoker", "Trait3": ""},
    "Lissandra": {"Gold": 5, "Board Size": 1, "Trait1": "Porcelain", "Trait2": "Arcanist", "Trait3": ""},
    "Lux": {"Gold": 2, "Board Size": 1, "Trait1": "Porcelain", "Trait2": "Arcanist", "Trait3": ""},
    "Malphite": {"Gold": 1, "Board Size": 1, "Trait1": "Heavenly", "Trait2": "Behemoth", "Trait3": ""},
    "Morgana": {"Gold": 4, "Board Size": 1, "Trait1": "Ghostly", "Trait2": "Sage", "Trait3": ""},
    "Nautilus": {"Gold": 4, "Board Size": 1, "Trait1": "Mythic", "Trait2": "Warden", "Trait3": ""},
    "Neeko": {"Gold": 2, "Board Size": 1, "Trait1": "Heavenly", "Trait2": "Mythic", "Trait3": "Arcanist"},
    "Ornn": {"Gold": 4, "Board Size": 1, "Trait1": "Dryad", "Trait2": "Behemoth", "Trait3": ""},
    "Qiyana": {"Gold": 2, "Board Size": 1, "Trait1": "Heavenly", "Trait2": "Duelist", "Trait3": ""},
    "Rakan": {"Gold": 5, "Board Size": 1, "Trait1": "Dragonlord", "Trait2": "Altruist", "Trait3": "Lovers"},
    "RekSai": {"Gold": 1, "Board Size": 1, "Trait1": "Dryad", "Trait2": "Bruiser", "Trait3": ""},
    "Riven": {"Gold": 2, "Board Size": 1, "Trait1": "Storyweaver", "Trait2": "Altruist", "Trait3": "Bruiser"},
    "Senna": {"Gold": 2, "Board Size": 1, "Trait1": "Inkshadow", "Trait2": "Sniper", "Trait3": ""},
    "Sett": {"Gold": 5, "Board Size": 1, "Trait1": "Fated", "Trait2": "Umbral", "Trait3": "Warden"},
    "Shen": {"Gold": 2, "Board Size": 1, "Trait1": "Ghostly", "Trait2": "Behemoth", "Trait3": ""},
    "Sivir": {"Gold": 1, "Board Size": 1, "Trait1": "Storyweaver", "Trait2": "Trickshot", "Trait3": ""},
    "Soraka": {"Gold": 3, "Board Size": 1, "Trait1": "Heavenly", "Trait2": "Altruist", "Trait3": ""},
    "Sylas": {"Gold": 4, "Board Size": 1, "Trait1": "Umbral", "Trait2": "Bruiser", "Trait3": ""},
    "Syndra": {"Gold": 4, "Board Size": 1, "Trait1": "Fated", "Trait2": "Arcanist", "Trait3": ""},
    "Tahm Kench": {"Gold": 3, "Board Size": 1, "Trait1": "Mythic", "Trait2": "Bruiser", "Trait3": ""},
    "Teemo": {"Gold": 2, "Board Size": 1, "Trait1": "Fortune", "Trait2": "Trickshot", "Trait3": ""},
    "Thresh": {"Gold": 3, "Board Size": 1, "Trait1": "Fated", "Trait2": "Behemoth", "Trait3": ""},
    "Tristana": {"Gold": 3, "Board Size": 1, "Trait1": "Fortune", "Trait2": "Duelist", "Trait3": ""},
    "Udyr": {"Gold": 5, "Board Size": 1, "Trait1": "Inkshadow", "Trait2": "Behemoth", "Trait3": ""},
    "Volibear": {"Gold": 3, "Board Size": 1, "Trait1": "Inkshadow", "Trait2": "Duelist", "Trait3": ""},
    "Wukong": {"Gold": 5, "Board Size": 1, "Trait1": "Heavenly", "Trait2": "Sage", "Trait3": ""},
    "Xayah": {"Gold": 5, "Board Size": 1, "Trait1": "Dragonlord", "Trait2": "Lovers", "Trait3": "Trickshot"},
    "Yasuo": {"Gold": 1, "Board Size": 1, "Trait1": "Fated", "Trait2": "Duelist", "Trait3": ""},
    "Yone": {"Gold": 3, "Board Size": 1, "Trait1": "Umbral", "Trait2": "Reaper", "Trait3": ""},
    "Yorick": {"Gold": 2, "Board Size": 1, "Trait1": "Umbral", "Trait2": "Behemoth", "Trait3": ""},
    "Zoe": {"Gold": 3, "Board Size": 1, "Trait1": "Fortune", "Trait2": "Storyweaver", "Trait3": "Arcanist"},
    "Zyra": {"Gold": 2, "Board Size": 1, "Trait1": "Storyweaver", "Trait2": "Sage", "Trait3": ""}
    }
    return champions_data


def update_comps(file_path):
    """Update comps if the user chooses to."""
    while True:
        comp_input = input("Do you want to update comps? (y/n) ")
        if comp_input.lower() in YES_CHOICES:
            os.remove(file_path)
            print("Old comp files successfully deleted!")
            for file_name in ["deck.json", "inputed"]:
                file_to_remove = os.path.join("cached_data", file_name)
                if os.path.isfile(file_to_remove):
                    os.remove(file_to_remove)
            break
        elif comp_input.lower() in NO_CHOICES:
            break
        else:
            print("Type yes or no")


def main():
    """The main entry point for the TFT OCR BOT.

    This function initializes the logging configuration, checks the League of Legends client path,
    loads champions data, sets up the CompsManager, and starts the main game loop in a separate process.

    If cached champions and comps exist, the user is prompted to update them. The UI is then started
    in a loop until the user closes the window, keeping the program running indefinitely.

    Raises:
        ValueError: If the League of Legends client path is not specified in settings.py.
    """
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Comps TFT OCR Bot")
    print(
        r"""
     ___       __         _____                      ________________  ____  ________    ___       __ 
    / _ |__ __/ /____    / ___/__  __ _  ___  ___   /_  __/ __/_  __/ / __ \/ ___/ _ \  / _ )___  / /_
   / __ / // / __/ _ \  / /__/ _ \/  ' \/ _ \(_-<    / / / _/  / /   / /_/ / /__/ , _/ / _  / _ \/ __/
  /_/ |_\_,_/\__/\___/  \___/\___/_/_/_/ .__/___/   /_/ /_/   /_/    \____/\___/_/|_| /____/\___/\__/
                                      /_/
    """
    )

    check_league_client_path()

    # Champions data structure
    champions_data = load_champions_data()

    comps_manager = CompsManager()
    comps_manager.champions = champions_data

    message_queue = multiprocessing.Queue()
    overlay = UI(message_queue)
    game_thread = multiprocessing.Process(
        target=game_loop, args=(message_queue, comps_manager)
    )

    print(
        "\nOriginal version - https://github.com/jfd02/TFT-OCR-BOT"
        "\n\nAutoComps version - https://github.com/Sizzzles/TFT-OCR-BOT\n"
    )

    file_path = os.path.join("cached_data", "cached11.json")
    if os.path.isfile(file_path):
        last_modified_time = time.ctime(os.path.getmtime(file_path))
        print(f"Champions and comps already exist. Last modified: {last_modified_time}")
        update_comps(file_path)

    print("Close this window to terminate the overlay window & program")
    auto_comps.load_champions_and_comps(comps_manager)
    game_thread.start()
    overlay.ui_loop()


if __name__ == "__main__":
    if is_admin():
        main()
    else:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
