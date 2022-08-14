![main](https://i.imgur.com/roX0N3C.png)

## NOTES:
- Make sure you don't have any overlays on (Blitz, Mobalytics, etc.).
- League & client must be in English.
- 16:9 resolution borderless windowed is required in League, the game must also be on the main monitor (Use 1920x1080 for best results).
- If the program crashes, create an issue with the error.

## INSTALLATION:
1. Install Python 3.10.6 from https://www.python.org/downloads/windows/
   - Note that Python 3.10.6 cannot be used on Windows 7 or earlier.
2. Clone the repository or download it from here https://github.com/jfd02/TFT-OCR-BOT/archive/refs/heads/main.zip
3. Open Command Prompt and change the current directory to the folder where main.py is located 
4. Run pip install -r requirements.txt in Command Prompt
5. Install tesseract using the Windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki
   - Note the tesseract path from the installation.
   - Set the tesseract path in the settings.py file (it may already be correct)
6. Configure settings.py so the league client path is correct
7. Disable all in-game overlays
8. Run the main.py file

## FEATURES:
![main](https://i.imgur.com/1bXOmag.png)
- Read the board state (Round / Level / Gold / Shop / Items)
- Keeps track of champions on the board and bench
- Pick a random item/champ from the carousel
- Pickup items from the board after PVE rounds
- Place correct items onto champions
- Plays the user-defined team comp
- Auto queue using the LCU API

## TODO:
- Implement tome of traits logic
- Revamp the gold spending function
- Revamp auto queue to have more safety checks / fail-safes
- Grab the best compositions from TFT website
- Intelligent carousel item selection
- Change item pickup to be based on the coordinates of orbs
