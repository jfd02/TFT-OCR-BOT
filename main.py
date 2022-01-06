import auto_queue
from game import Game


if __name__ == "__main__":
    print("TFT OCR | Ver. 1.0 | https://github.com/jfd02/TFT-OCR-BOT")
    while True:
        auto_queue.queue()
        game = Game()
        game.loading_screen()
