"""
Where the bot execution starts & contains the game loop that keeps the bot running indefinitely
"""

import multiprocessing
from ui import UI
import auto_queue
from game import Game
import settings
import auto_comps
from comps import CompsManager
import os, time
import sys

def game_loop(ui_queue: multiprocessing.Queue, comps : CompsManager)  -> None:
    """Keeps the program running indefinetly by calling queue and game start in a loop"""
    while True:
        auto_queue.queue()
        Game(ui_queue, comps)


if __name__ == "__main__":
    if settings.LEAGUE_CLIENT_PATH is None:
        raise Exception(
            "No league client path specified. Please set the path in settings.py")
    comps_manager = CompsManager()
    comps_manager.champions = {"Sylas": {"Gold": 1, "Board Size": 1}, "Nasus": {"Gold": 1, "Board Size": 1},
                               "Jinx": {"Gold": 2, "Board Size": 1}, "Vayne": {"Gold": 3, "Board Size": 1},
                               "Riven": {"Gold": 3, "Board Size": 1}, "Miss Fortune": {"Gold": 4, "Board Size": 1},
                               "Lucian": {"Gold": 1, "Board Size": 1}, "Sivir": {"Gold": 2, "Board Size": 1},
                               "Janna": {"Gold": 5, "Board Size": 1}, "Nunu & Willump": {"Gold": 5, "Board Size": 1},
                               "Lux": {"Gold": 1, "Board Size": 1}, "Nilah": {"Gold": 3, "Board Size": 1},
                               "Kai'Sa": {"Gold": 3, "Board Size": 1}, "Rell": {"Gold": 2, "Board Size": 1},
                               "Ekko": {"Gold": 4, "Board Size": 1}, "Syndra": {"Gold": 5, "Board Size": 1},
                               "Warwick": {"Gold": 4, "Board Size": 1}, "Draven": {"Gold": 2, "Board Size": 1},
                               "Leona": {"Gold": 5, "Board Size": 1}, "Jax": {"Gold": 3, "Board Size": 1},
                               "Neeko": {"Gold": 4, "Board Size": 1}, "Ashe": {"Gold": 1, "Board Size": 1},
                               "Gnar": {"Gold": 3, "Board Size": 1}, "Twisted Fate": {"Gold": 4, "Board Size": 1},
                               "Mordekaiser": {"Gold": 5, "Board Size": 1}, "Annie": {"Gold": 2, "Board Size": 1},
                               "Fiora": {"Gold": 2, "Board Size": 1}, "Alistar": {"Gold": 3, "Board Size": 1},
                               "Garen": {"Gold": 4, "Board Size": 1}, "Viego": {"Gold": 4, "Board Size": 1},
                               "Kayle": {"Gold": 1, "Board Size": 1}, "Vi": {"Gold": 2, "Board Size": 1},
                               "Samira": {"Gold": 4, "Board Size": 1}, "Sona": {"Gold": 3, "Board Size": 1},
                               "Lulu": {"Gold": 1, "Board Size": 1}, "Shen": {"Gold": 3, "Board Size": 1},
                               "Blitzcrank": {"Gold": 1, "Board Size": 1}, "Camille": {"Gold": 2, "Board Size": 1},
                               "Gangplank": {"Gold": 1, "Board Size": 1}, "Lee Sin": {"Gold": 2, "Board Size": 1},
                               "Malphite": {"Gold": 2, "Board Size": 1}, "Vex": {"Gold": 3, "Board Size": 1},
                               "Morgana": {"Gold": 3, "Board Size": 1}, "Aurelion Sol": {"Gold": 4, "Board Size": 1},
                               "Rammus": {"Gold": 3, "Board Size": 1}, "Bel'Veth": {"Gold": 4, "Board Size": 1},
                               "Jhin": {"Gold": 4, "Board Size": 1}, "Urgot": {"Gold": 5, "Board Size": 1},
                               "Fiddlesticks": {"Gold": 5, "Board Size": 1}, "Pyke": {"Gold": 2, "Board Size": 1},
                               "Yasuo": {"Gold": 2, "Board Size": 1}, "Poppy": {"Gold": 1, "Board Size": 1},
                               "Pantheon": {"Gold": 1, "Board Size": 1}, "Renekton": {"Gold": 1, "Board Size": 1},
                               "Wukong": {"Gold": 1, "Board Size": 1}, "Ezreal": {"Gold": 2, "Board Size": 1},
                               "Aatrox": {"Gold": 4, "Board Size": 1}, "LeBlanc": {"Gold": 3, "Board Size": 1},
                               "Ultimate Ezreal": {"Gold": 5, "Board Size": 1}}

    message_queue = multiprocessing.Queue()
    overlay: UI = UI(message_queue)
    game_thread = multiprocessing.Process(target=game_loop, args=(message_queue,comps_manager))

    print("TFT OCR | https://github.com/jfd02/TFT-OCR-BOT")
    yes_choices = ['yes', 'y']
    no_choices = ['no', 'n']
    comp_input = ''

    if(os.path.isfile("cached_data\cached8.5.json")):
        print(
            'Champions and comps already exist. Last modified: %s' % time.ctime(os.path.getmtime("cached_data\cached8.5.json"))
            )
        print('Do you want the latest comps?(y/n)')
        while True:
            comp_input = input()
            if comp_input.lower() in yes_choices:
                os.remove("cached_data\cached8.5.json")
                print('Old comp files sucessfully deleted!')
                if(os.path.isfile("cached_data\deck.json")):
                    os.remove("cached_data\deck.json")
                if(os.path.isfile("cached_data\inputed")):
                    os.remove("cached_data\inputed")
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