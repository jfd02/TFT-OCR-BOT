"""
Where the bot execution starts & contains the game loop that keeps the bot running indefinitely
"""

import auto_queue
from game import Game
import settings

def game_loop():
    while True:
        auto_queue.queue()
        Game()

if __name__ == "__main__": 
    if settings.LEAGUE_CLIENT_PATH == None:
        raise Exception("No league client path specified. Please set the path in settings.py")

    print("TFT OCR | https://github.com/jfd02/TFT-OCR-BOT")
    print("Close this window to terminate the overlay window & program")
    game_loop()
