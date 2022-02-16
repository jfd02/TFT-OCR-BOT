import time

import arena_functions
import auto_queue
from game import Game
import multiprocessing
from ui import Ui


def game_loop(message_queue):
    arena_functions.get_champion_data()

    while True:
        auto_queue.queue(message_queue)
        game = Game(message_queue)


if __name__ == "__main__":
    message_queue = multiprocessing.Queue()
    overlay = Ui(message_queue)
    game_thread = multiprocessing.Process(target=game_loop, args=(message_queue,))

    print("TFT OCR | Ver. 2.2.0 | https://github.com/jfd02/TFT-OCR-BOT")
    print("If text is not visible on the top left of the screen, the program is not functioning correctly.")
    print("Close this window to terminate the overlay window & program")

    game_thread.start()
    overlay.ui_loop()


