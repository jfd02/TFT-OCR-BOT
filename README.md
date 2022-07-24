![main](https://i.imgur.com/roX0N3C.png)

## NOTES:
- Make sure you dont have any overlays on.
- To ensure best results, make sure you are running this on a computer that has decent specs.
- League & client must be in English.
- 16:9 resolution borderless windowed is required in League, game must also be on main monitor (Use 1920x1080 for best results).
- If the program crashes, create an issue with the error.

## INSTALLATION:
1. Install Python 3.9.6 from https://www.python.org/downloads/windows/
   - Note that Python 3.9.6 cannot be used on Windows 7 or earlier.
3. Run pip install -r requirements.txt in Command Prompt
4. Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki
   - Note the tesseract path from the installation.
   - Set the tesseract path in the ocr.py file (it may already be correct)
5. Configure settings.py so the league client path is correct & enable surrender functionality if you desere it.
6. Disable all in game overlays
7. Run the main.py file

## FEATURES:
![main](https://i.imgur.com/1bXOmag.png)
- Read the board state (Round / Level / Gold / Shop / Items)
- Keeps track of champions on the board and bench
- Pick a random item/champ from the carousel
- Pickup items from the board after PVE rounds
- Place correct items onto champions
- Plays the user defined team comp
- Auto queue using the LCU api

## TODO:
- Implement tome of traits logic
- Revamp the gold spending function
- Revamp auto queue to have more safety checks / fail safes
- Grab best compositions from TFT website
- Intelligent carousel item selection
- Change item pickup to be based of the coordinates of orbs
