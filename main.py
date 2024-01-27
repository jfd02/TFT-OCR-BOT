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
    except: # pylint: disable=bare-except
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
    "Ahri":{"Gold":4,"Board Size":1,"Trait1":"Spellweaver","Trait2":"KDA","Trait3":""},
    "Akali":{"Gold":4,"Board Size":1,"Trait1":"Executioner","Trait2":"Breakout","Trait3":"TrueDamage"},
    "Amumu":{"Gold":3,"Board Size":1,"Trait1":"Guardian","Trait2":"Emo","Trait3":""},
    "Annie":{"Gold":1,"Board Size":1,"Trait1":"Spellweaver","Trait2":"Emo","Trait3":""},
    "Aphelios":{"Gold":2,"Board Size":1,"Trait1":"Rapidfire","Trait2":"HEARTSTEEL","Trait3":""},
    "Bard":{"Gold":2,"Board Size":1,"Trait1":"Dazzler","Trait2":"Jazz","Trait3":""},
    "Blitzcrank":{"Gold":4,"Board Size":1,"Trait1":"Sentinel","Trait2":"Disco","Trait3":""},
    "Caitlyn":{"Gold":4,"Board Size":1,"Trait1":"Rapidfire","Trait2":"8bit","Trait3":""},
    "Corki":{"Gold":1,"Board Size":1,"Trait1":"BigShot","Trait2":"8bit","Trait3":""},
    "Ekko":{"Gold":3,"Board Size":1,"Trait1":"Sentinel","Trait2":"Spellweaver","Trait3":"TrueDamage"},
    "Evelynn":{"Gold":1,"Board Size":1,"Trait1":"CrowdDiver","Trait2":"K/DA","Trait3":""},
    "Ezreal":{"Gold":4,"Board Size":1,"Trait1":"BigShot","Trait2":"HEARTSTEEL","Trait3":""},
    "Garen":{"Gold":2,"Board Size":1,"Trait1":"Sentinel","Trait2":"8bit","Trait3":""},
    "Gnar":{"Gold":2,"Board Size":1,"Trait1":"Mosher","Trait2":"Superfan","Trait3":"Pentakill"},
    "Gragas":{"Gold":2,"Board Size":1,"Trait1":"Bruiser","Trait2":"Spellweaver","Trait3":"Disco"},
    "Illaoi":{"Gold":5,"Board Size":1,"Trait1":"Bruiser","Trait2":"ILLBEATS","Trait3":""},
    "Tentacle":{"Gold":0,"Board Size":1,"Trait1":"","Trait2":"","Trait3":""},
    "Jax":{"Gold":2,"Board Size":1,"Trait1":"Mosher","Trait2":"EDM","Trait3":""},
    "Jhin":{"Gold":5,"Board Size":1,"Trait1":"BigShot","Trait2":"Maestro","Trait3":""},
    "Jinx":{"Gold":1,"Board Size":1,"Trait1":"Rapidfire","Trait2":"Punk","Trait3":""},
    "Kai'Sa":{"Gold":2,"Board Size":1,"Trait1":"BigShot","Trait2":"K/DA","Trait3":""},
    "Karthus":{"Gold":4,"Board Size":1,"Trait1":"Executioner","Trait2":"Pentakill","Trait3":""},
    "Katarina":{"Gold":2,"Board Size":1,"Trait1":"CrowdDiver","Trait2":"Country","Trait3":""},
    "Kayle":{"Gold":2,"Board Size":1,"Trait1":"Edgelord","Trait2":"Pentakill","Trait3":""},
    "Kayn":{"Gold":5,"Board Size":1,"Trait1":"Edgelord","Trait2":"Wildcard","Trait3":"HEARTSTEEL"},
    "Kennen":{"Gold":1,"Board Size":1,"Trait1":"Guardian","Trait2":"Superfan","Trait3":"TrueDamage"},
    "K'Sante":{"Gold":1,"Board Size":1,"Trait1":"Sentinel","Trait2":"HEARTSTEEL","Trait3":""},
    "Lillia":{"Gold":1,"Board Size":1,"Trait1":"Sentinel","Trait2":"Superfan","Trait3":"K/DA"},
    "Lucian":{"Gold":5,"Board Size":1,"Trait1":"Rapidfire","Trait2":"Jazz","Trait3":""},
    "Lulu":{"Gold":3,"Board Size":1,"Trait1":"Spellweaver","Trait2":"Hyperpop","Trait3":""},
    "Lux":{"Gold":3,"Board Size":1,"Trait1":"Dazzler","Trait2":"EDM","Trait3":""},
    "Miss Fortune":{"Gold":3,"Board Size":1,"Trait1":"BigShot","Trait2":"Jazz","Trait3":""},
    "Mordekaiser":{"Gold":3,"Board Size":1,"Trait1":"Sentinel","Trait2":"Pentakill","Trait3":""},
    "Nami":{"Gold":1,"Board Size":1,"Trait1":"Dazzler","Trait2":"Disco","Trait3":""},
    "Neeko":{"Gold":3,"Board Size":1,"Trait1":"Guardian","Trait2":"Superfan","Trait3":"K/DA"},
    "Olaf":{"Gold":1,"Board Size":1,"Trait1":"Bruiser","Trait2":"Pentakill","Trait3":""},
    "Pantheon":{"Gold":2,"Board Size":1,"Trait1":"Guardian","Trait2":"Punk","Trait3":""},
    "Poppy":{"Gold":4,"Board Size":1,"Trait1":"Mosher","Trait2":"Emo","Trait3":""},
    "Qiyana":{"Gold":5,"Board Size":1,"Trait1":"CrowdDiver","Trait2":"TrueDamage","Trait3":""},
    "Riven":{"Gold":3,"Board Size":1,"Trait1":"Edgelord","Trait2":"8bit","Trait3":""},
    "Samira":{"Gold":3,"Board Size":1,"Trait1":"Executioner","Trait2":"Country","Trait3":""},
    "Senna":{"Gold":2,"Board Size":1,"Trait1":"Rapidfire","Trait2":"TrueDamage","Trait3":""},
    "Seraphine":{"Gold":2,"Board Size":1,"Trait1":"Spellweaver","Trait2":"K/DA","Trait3":""},
    "Sett":{"Gold":3,"Board Size":1,"Trait1":"Mosher","Trait2":"Bruiser","Trait3":"HEARTSTEEL"},
    "Sona":{"Gold":5,"Board Size":1,"Trait1":"Spellweaver","Trait2":"Mixmaster","Trait3":""},
    "Tahm Kench":{"Gold":1,"Board Size":1,"Trait1":"Bruiser","Trait2":"Country","Trait3":""},
    "Taric":{"Gold":1,"Board Size":1,"Trait1":"Guardian","Trait2":"Disco","Trait3":""},
    "Thresh":{"Gold":4,"Board Size":1,"Trait1":"Guardian","Trait2":"Country","Trait3":""},
    "Twisted Fate":{"Gold":4,"Board Size":1,"Trait1":"Dazzler","Trait2":"Disco","Trait3":""},
    "Twitch":{"Gold":2,"Board Size":1,"Trait1":"Executioner","Trait2":"Punk","Trait3":""},
    "Urgot":{"Gold":3,"Board Size":1,"Trait1":"Mosher","Trait2":"Country","Trait3":""},
    "Vex":{"Gold":3,"Board Size":1,"Trait1":"Executioner","Trait2":"Emo","Trait3":""},
    "Vi":{"Gold":1,"Board Size":1,"Trait1":"Mosher","Trait2":"Punk","Trait3":""},
    "Viego":{"Gold":4,"Board Size":1,"Trait1":"Edgelord","Trait2":"Pentakill","Trait3":""},
    "Yasuo":{"Gold":1,"Board Size":1,"Trait1":"Edgelord","Trait2":"TrueDamage","Trait3":""},
    "Yone":{"Gold":3,"Board Size":1,"Trait1":"CrowdDiver","Trait2":"Edgelord","Trait3":"HEARTSTEEL"},
    "Yorick":{"Gold":5,"Board Size":1,"Trait1":"Guardian","Trait2":"Mosher","Trait3":"Pentakill"},
    "Zac":{"Gold":4,"Board Size":1,"Trait1":"Bruiser","Trait2":"EDM","Trait3":""},
    "Zed":{"Gold":4,"Board Size":1,"Trait1":"CrowdDiver","Trait2":"EDM","Trait3":""},
    "Ziggs":{"Gold":5,"Board Size":1,"Trait1":"Dazzler","Trait2":"Hyperpop","Trait3":""}
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
    print(r"""
     ___       __         _____                      ________________  ____  ________    ___       __ 
    / _ |__ __/ /____    / ___/__  __ _  ___  ___   /_  __/ __/_  __/ / __ \/ ___/ _ \  / _ )___  / /_
   / __ / // / __/ _ \  / /__/ _ \/  ' \/ _ \(_-<    / / / _/  / /   / /_/ / /__/ , _/ / _  / _ \/ __/
  /_/ |_\_,_/\__/\___/  \___/\___/_/_/_/ .__/___/   /_/ /_/   /_/    \____/\___/_/|_| /____/\___/\__/
                                      /_/
    """)

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

    file_path = os.path.join("cached_data", "cached10.json")
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
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
