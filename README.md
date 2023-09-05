Fork of https://github.com/jfd02/TFT-OCR-BOT

![main](https://i.imgur.com/roX0N3C.png)

## NOTES:
- Make sure you don't have any overlays on (Blitz, Mobalytics, etc.).
- League & client must be in English.
- 16:9 resolution borderless windowed is required in League, the game must also be on the main monitor (Use 1920x1080 for best results).
- If the program crashes, create an issue with the error.

## INSTALLATION:
1. Install Python 3.10.4 from https://www.python.org/downloads/windows/
   - Note that Python 3.10.4 cannot be used on Windows 7 or earlier.
2. Clone the repository or download it from here https://github.com/Sizzzles/TFT-OCR-BOT/archive/refs/heads/main.zip
3. Open Command Prompt and change the current directory to the folder where main.py is located 
4. Run 'pip install -r requirements.txt' in Command Prompt
    > __Note__ must do again if you came from https://github.com/jfd02/TFT-OCR-BOT
5. Install tesseract 5.3.1.20230401 using the Windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki
   > __Note__ the tesseract path from the installation.
   - Set Tesseract tessdata folder path in settings.py file (probably already correct)
6. Download tesserocr v2.6.0 at: https://github.com/simonflueckiger/tesserocr-windows_build/releases
7. Open Command Prompt and change the current directory to the folder where tesserocr-2.6.0-cp311-cp311-win_amd64.whl is located
8. Run 'pip install tesserocr-2.6.0-cp311-cp311-win_amd64.whl' in Command Prompt

## FEATURES:
![main](https://i.imgur.com/1bXOmag.png)
- Read the board state (Round / Level / Gold / Shop / Items)
- Keeps track of champions on the board and bench
- Pick a random item/champ from the carousel
- Pickup items from the board after PVE rounds
- Place correct items onto champions
- Auto queue using the LCU API
- Implemented auto comps loading from lolchess (champion, board pos, items, augments)
- Various comps selection modes

## TODO:
- Implement tome of traits logic
- Revamp the gold spending function
- Revamp auto queue to have more safety checks / fail-safes
- Intelligent carousel item selection
- Change item pickup to be based on the coordinates of orbs
