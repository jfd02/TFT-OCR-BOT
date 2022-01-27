![main](https://i.imgur.com/roX0N3C.png)

## NOTES:
- You must use the default arena skin
- A lower color brightness in game makes the overlay easier to read
- To ensure best results, make sure you are running this on a computer that has decent specs.
- League & client must be in English.
- 1920x1080 borderless windowed is required in League, game must also be on main monitor.
- Make sure you dont have any overlays on.
- If the program crashes, create an issue with the error.

## INSTALLATION:
1. Install Python 3.9.6 from https://www.python.org/downloads/windows/
   - Note that Python 3.9.6 cannot be used on Windows 7 or earlier.
3. Run pip install -r requirements.txt in Command Prompt
4. Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki
   - Note the tesseract path from the installation.
   - Set the tesseract path in the ocr.py file (it may already be correct)
5. Run the main.py file

## FEATURES:
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
- Add more checks to auto queue so it can never fail
- Grab all S teamcomps from a TFT website and determine the best one to play in the game
- Intelligent carousel item selection (Not sure how to accomplish this one)
- Change item pickup to be based of the coordinates of orbs
