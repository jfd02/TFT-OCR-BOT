import auto_queue
from game import Game
import multiprocessing
from ui import Ui
import settings

def game_loop(message_queue):
    while True:
        auto_queue.queue(message_queue)
        game = Game(message_queue)

if __name__ == "__main__": 
    if settings.LEAGUE_CLIENT_PATH == None:
        raise Exception("No league client path specified. Please set the path in settings.py")
    message_queue = multiprocessing.Queue()
    overlay = Ui(message_queue)
    game_thread = multiprocessing.Process(target=game_loop, args=(message_queue,))

    print("TFT OCR | https://github.com/jfd02/TFT-OCR-BOT")
    print("If text is not visible on the top left of the screen, the program is not functioning correctly.")
    print("Close this window to terminate the overlay window & program")

    game_thread.start()
    overlay.ui_loop()

