# Original code from the TFT_OCR_BOT repository on GitHub:
# Repository URL: https://github.com/jfd02/TFT-OCR-BOT
# Original authors:
# - @jfd02
# - @danparizher
# Modified by the-user-created on 22/10/2023
#

"""
Where the bot execution starts & contains the game loop that keeps the bot running indefinitely
"""

import multiprocessing
from ui import UI
import auto_queue
from game import Game
import settings


def game_loop(ui_queue: multiprocessing.Queue) -> None:
    """Keeps the program running indefinitely by calling queue and game start in a loop"""
    while True:
        auto_queue.queue()
        Game(ui_queue)


if __name__ == "__main__":
    if settings.LEAGUE_CLIENT_PATH is None:
        raise ValueError("No league client path specified. Please set the path in settings.py")
    message_queue = multiprocessing.Queue()
    overlay: UI = UI(message_queue)
    game_thread = multiprocessing.Process(target=game_loop, args=(message_queue,))

    print("TFT OCR | https://github.com/the-user-created/TFT-OCR-BOT")
    print("Close this window to terminate the overlay window & program")
    game_thread.start()
    overlay.ui_loop()
