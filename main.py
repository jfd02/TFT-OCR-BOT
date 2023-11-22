"""
Where the bot execution starts & contains the game loop that keeps the bot running indefinitely
"""

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
        auto_queue.queue()
        Game(ui_queue, comps)

def check_league_client_path():
    """Check if League of Legends client path is specified."""
    if LEAGUE_CLIENT_PATH is None:
        print("No League of Legends client path specified. Please set the path in settings.py")
        raise ValueError("No League of Legends client path specified. Please set the path in settings.py")

def load_champions_data() -> dict:
    """Load champions data from a file or other source."""
    # Replace this with your actual implementation
    champions_data = {
        "Annie": {"Gold": 1, "Board Size": 1},
        "Corki": {"Gold": 1, "Board Size": 1},
        "Evelynn": {"Gold": 1, "Board Size": 1},
        "Jinx": {"Gold": 1, "Board Size": 1},
        "Kennen": {"Gold": 1, "Board Size": 1},
        "K'Sante": {"Gold": 1, "Board Size": 1},
        "Lillia": {"Gold": 1, "Board Size": 1},
        "Nami": {"Gold": 1, "Board Size": 1},
        "Olaf": {"Gold": 1, "Board Size": 1},
        "Tahm Kench": {"Gold": 1, "Board Size": 1},
        "Taric": {"Gold": 1, "Board Size": 1},
        "Vi": {"Gold": 1, "Board Size": 1},
        "Yasuo": {"Gold": 1, "Board Size": 1},
        "Aphelios": {"Gold": 2, "Board Size": 1},
        "Bard": {"Gold": 2, "Board Size": 1},
        "Garen": {"Gold": 2, "Board Size": 1},
        "Gnar": {"Gold": 2, "Board Size": 1},
        "Gragas": {"Gold": 2, "Board Size": 1},
        "Jax": {"Gold": 2, "Board Size": 1},
        "Kai'Sa": {"Gold": 2, "Board Size": 1},
        "Katarina": {"Gold": 2, "Board Size": 1},
        "Kayle": {"Gold": 2, "Board Size": 1},
        "Pantheon": {"Gold": 2, "Board Size": 1},
        "Senna": {"Gold": 2, "Board Size": 1},
        "Seraphine": {"Gold": 2, "Board Size": 1},
        "Twitch": {"Gold": 2, "Board Size": 1},
        "Amumu": {"Gold": 3, "Board Size": 1},
        "Ekko": {"Gold": 3, "Board Size": 1},
        "Lulu": {"Gold": 3, "Board Size": 1},
        "Lux": {"Gold": 3, "Board Size": 1},
        "Miss Fortune": {"Gold": 3, "Board Size": 1},
        "Mordekaiser": {"Gold": 3, "Board Size": 1},
        "Neeko": {"Gold": 3, "Board Size": 1},
        "Riven": {"Gold": 3, "Board Size": 1},
        "Samira": {"Gold": 3, "Board Size": 1},
        "Sett": {"Gold": 3, "Board Size": 1},
        "Urgot": {"Gold": 3, "Board Size": 1},
        "Vex": {"Gold": 3, "Board Size": 1},
        "Yone": {"Gold": 3, "Board Size": 1},
        "Ahri": {"Gold": 4, "Board Size": 1},
        "Akali": {"Gold": 4, "Board Size": 1},
        "Blitzcrank": {"Gold": 4, "Board Size": 1},
        "Caitlyn": {"Gold": 4, "Board Size": 1},
        "Ezeral": {"Gold": 4, "Board Size": 1},
        "Karthus": {"Gold": 4, "Board Size": 1},
        "Poppy": {"Gold": 4, "Board Size": 1},
        "Thresh": {"Gold": 4, "Board Size": 1},
        "Twisted Fate": {"Gold": 4, "Board Size": 1},
        "Viego": {"Gold": 4, "Board Size": 1},
        "Zac": {"Gold": 4, "Board Size": 1},
        "Zed": {"Gold": 4, "Board Size": 1},
        "Illaoi": {"Gold": 5, "Board Size": 1},
        "Jhin": {"Gold": 5, "Board Size": 1},
        "Kayn": {"Gold": 5, "Board Size": 1},
        "Lucian": {"Gold": 5, "Board Size": 1},
        "Qiyana": {"Gold": 5, "Board Size": 1},
        "Sona": {"Gold": 5, "Board Size": 1},
        "Yorick": {"Gold": 5, "Board Size": 1},
        "Ziggs": {"Gold": 5, "Board Size": 1},
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
    print("AUTO COMPS TFT OCR BOT started.")

    check_league_client_path()

    # Champions data structure
    champions_data = load_champions_data()

    comps_manager = CompsManager()
    comps_manager.champions = champions_data

    message_queue = multiprocessing.Queue()
    overlay = UI(message_queue)
    game_thread = multiprocessing.Process(target=game_loop, args=(message_queue, comps_manager))

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
    main()
