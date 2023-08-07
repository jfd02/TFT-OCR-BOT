"""
Where the bot execution starts & contains the game loop that keeps the bot running indefinitely
"""

import multiprocessing
import os
import time
from ui import UI
import auto_queue
from game import Game
import settings
import auto_comps
from comps import CompsManager

def game_loop(ui_queue: multiprocessing.Queue, comps : CompsManager)  -> None:
    """Keeps the program running indefinetly by calling queue and game start in a loop"""
    while True:
        auto_queue.queue()
        Game(ui_queue, comps)


if __name__ == "__main__":
    if settings.LEAGUE_CLIENT_PATH is None:
        raise ValueError(
            "No league client path specified. Please set the path in settings.py")
    comps_manager = CompsManager()
    comps_manager.champions = {"Tristana": {"Gold": 1, "Board Size": 1}, "Irelia": {"Gold": 1, "Board Size": 1},
                                "Aatrox": {"Gold": 5, "Board Size": 1}, "Ahri": {"Gold": 5, "Board Size": 1}, 
                                "Akshan": {"Gold": 3, "Board Size": 1}, "Ashe": {"Gold": 2, "Board Size": 1}, 
                                "Azir": {"Gold": 4, "Board Size": 1}, "Bel'Veth": {"Gold": 5, "Board Size": 1}, 
                                "Cho'Gath": {"Gold": 1, "Board Size": 1}, "Darius": {"Gold": 3, "Board Size": 1}, 
                                "Ekko": {"Gold": 3, "Board Size": 1}, "Garen": {"Gold": 3, "Board Size": 1}, 
                                "Gwen": {"Gold": 4, "Board Size": 1}, "Heimerdinger": {"Gold": 5, "Board Size": 1}, 
                                "Jarvan IV": {"Gold": 4, "Board Size": 1}, "Jayce": {"Gold": 3, "Board Size": 1}, 
                                "Jinx": {"Gold": 2, "Board Size": 1}, "Kai'Sa": {"Gold": 4, "Board Size": 1}, 
                                "Karma": {"Gold": 3, "Board Size": 1}, "Katarina": {"Gold": 3, "Board Size": 1}, 
                                "Kled": {"Gold": 2, "Board Size": 1}, "K'Sante": {"Gold": 5, "Board Size": 1}, 
                                "Lissandra": {"Gold": 3, "Board Size": 1}, "Lux": {"Gold": 4, "Board Size": 1}, 
                                "Orianna": {"Gold": 1, "Board Size": 1}, "Poppy": {"Gold": 1, "Board Size": 1}, 
                                "Shen": {"Gold": 4, "Board Size": 1}, "Renekton": {"Gold": 1, "Board Size": 1}, 
                                "Sejuani": {"Gold": 4, "Board Size": 1}, "Senna": {"Gold": 5, "Board Size": 1}, 
                                "Sion": {"Gold": 5, "Board Size": 1}, "Sona": {"Gold": 3, "Board Size": 1}, 
                                "Soraka": {"Gold": 2, "Board Size": 1}, "Swain": {"Gold": 2, "Board Size": 1}, 
                                "Taric": {"Gold": 3, "Board Size": 1}, "Teemo": {"Gold": 2, "Board Size": 1}, 
                                "Vel'Koz": {"Gold": 3, "Board Size": 1}, "Warwick": {"Gold": 2, "Board Size": 1}, 
                                "Yasuo": {"Gold": 4, "Board Size": 1}, "Zed": {"Gold": 2, "Board Size": 1}, 
                                "Cassiopeia": {"Gold": 1, "Board Size": 1}, "Vi": {"Gold": 2, "Board Size": 1}, 
                                "Maokai": {"Gold": 1, "Board Size": 1}, "Kayle": {"Gold": 1, "Board Size": 1}, 
                                "Samira": {"Gold": 1, "Board Size": 1}, "Urgot": {"Gold": 4, "Board Size": 1}, 
                                "Aphelios": {"Gold": 4, "Board Size": 1}, "Zeri": {"Gold": 4, "Board Size": 1}, 
                                "Galio": {"Gold": 2, "Board Size": 1}, "Kalista": {"Gold": 3, "Board Size": 1}, 
                                "Nasus": {"Gold": 4, "Board Size": 1}, "Malzahar": {"Gold": 1, "Board Size": 1}, 
                                "Taliyah": {"Gold": 2, "Board Size": 1}, "Ryze": {"Gold": 5, "Board Size": 1}, 
                                "Sett": {"Gold": 2, "Board Size": 1}, "Jhin": {"Gold": 1, "Board Size": 1}, 
                                "Viego": {"Gold": 1, "Board Size": 1}, "Kassadin": {"Gold": 2, "Board Size": 1}, 
                                "Rek'Sai": {"Gold": 3, "Board Size": 1}}

    message_queue = multiprocessing.Queue()
    overlay: UI = UI(message_queue)
    game_thread = multiprocessing.Process(target=game_loop, args=(message_queue,comps_manager))

    print("\nOriginal version - https://github.com/jfd02/TFT-OCR-BOT\n\nAutoComps version - https://github.com/Sizzzles/TFT-OCR-BOT\n")

    yes_choices = ['yes', 'y']
    no_choices = ['no', 'n']

    if os.path.isfile("cached_data/cached9.json"):
        print('Champions and comps already exist. Last modified: %s' % time.ctime(os.path.getmtime("cached_data/cached9.json")))
        while True:
            comp_input = input('Do you want to update comps? (y/n) ')
            if comp_input.lower() in yes_choices:
                os.remove("cached_data/cached9.json")
                print('Old comp files sucessfully deleted!')
                if os.path.isfile("cached_data/deck.json"):
                    os.remove("cached_data/deck.json")
                if os.path.isfile("cached_data/inputed"):
                    os.remove("cached_data/inputed")
                break
            elif comp_input.lower() in no_choices:
                break
            else:
                print('Type yes or no')
                continue

    print("Close this window to terminate the overlay window & program")
    auto_comps.LoadChampionsAndComps(comps_manager)
    game_thread.start()
    overlay.ui_loop()
