![main](https://i.imgur.com/roX0N3C.png)

## NOTES:
- Make sure you don't have any overlays on (Blitz, Mobalytics, etc.).
- League & client must be in English.
- 16:9 resolution borderless windowed is required in League, the game must also be on the main monitor ~~(Use 1920x1080 for best results).~~
- Due to some adjustments by Riot, other resolutions are not exactly scaled versions of 1080p, so now **only support 1920x1080 borderless window.**
- If the program crashes or not working, please read the FAQ first. If the issue still cannot be resolved, then create an issue with the error.

## INSTALLATION:
1. Install Python 3.11.4 from https://www.python.org/downloads/windows/
   - Note that Python 3.11.4 cannot be used on Windows 7 or earlier.
2. Clone the repository or download it from here https://github.com/jfd02/TFT-OCR-BOT/archive/refs/heads/main.zip
3. Install tesseract 5.3.1.20230401 using the Windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki
   - Note the tesseract path from the installation.
   - Set Tesseract tessdata folder path in settings.py file (probably already correct)
4. Download tesserocr v2.6.0 to the bot folder via: https://github.com/simonflueckiger/tesserocr-windows_build/releases
   - Please note that the version must be 2.6.0 to be compatible with tesseract 5.3.1
   - Select the installation file for either 3.10 or 3.11 based on the Python version you are currently using
   - The file name should be either tesserocr-2.6.0-cp311-cp311-win_amd64.whl or its corresponding to cp310.
5. Run install.py
6. Configure settings.py so the league client path is correct
7. Disable all in-game overlays
8. Run the main.py file in CMD

## FEATURES:
![main](https://i.imgur.com/1bXOmag.png)
- Read the board state (Round / Level / Gold / Shop / Items)
- Keeps track of champions on the board and bench
- Pick a random item/champ from the carousel
- Pickup items from the board after PVE rounds
- Place correct items onto champions
- Plays the user-defined team comp
- Auto queue using the LCU API
- Comp editor with GUI

## Comp Editor

**Note:** Make sure you have a valid `comps.py` file (copy the one from the repo if you get syntax errors)!

Open by clicking the file or executing from a terminal with `python comp_editor.py` (in the correct folder).

![main](https://i.imgur.com/3e6hKFp.png)

## TODO:
- Implement tome of traits logic
- Revamp the gold spending function
- Revamp auto queue to have more safety checks / fail-safes
- Grab the best compositions from TFT website
- Intelligent carousel item selection
- Change item pickup to be based on the coordinates of orbs

## FAQ:
> ModuleNotFoundError: No module named 'win32gui'
- Open the command prompt (cmd) and run 'pip install pywin32'.
> I double clicked main.py, a window popped up and closed instantly.
- Open the command prompt (cmd), drag and drop main.py into it, and then press Enter to run it.
> The bot said it is moving, buying, and selling champions, but nothing is happening.
- Open the command prompt (cmd) with admin privileges.
> Client not open! Trying again in 10 seconds.
- Check if your game path is correct and open League of Legends by yourself.
> RuntimeError: Failed to init API, possibly an invalid tessdata path.
- You don't need to change the TESSDATA_PATH in settings.py if you didn't modify the destination folder while installing Tesseract.
> ImportError: DLL load failed while importing _tesserocr: The specified module could not be found.
- Download and install vc_redist : https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170
