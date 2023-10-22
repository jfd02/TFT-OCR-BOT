# Original code from the TFT_OCR_BOT repository on GitHub:
# Repository URL: https://github.com/jfd02/TFT-OCR-BOT
# Original authors:
# - @jfd02
# - @anthony5301
# Modified by the-user-created on 21/10/2023
#

"""Settings module"""

FORFEIT = False
FORFEIT_TIME = 600  # Time in seconds

# The following settings are for Windows users only
LEAGUE_CLIENT_PATH = r'C:\\Riot Games\\League of Legends'  # Replace with your game path if needed.
TESSERACT_TESSDATA_PATH = r'C:\\Program Files\\Tesseract-OCR\\tessdata'

# The following settings are for macOS users only
LEAGUE_CLIENT_PATH_OSX = r'/Applications/League of Legends.app/Contents/LoL'
TESSERACT_TESSDATA_PATH_OSX = r'/usr/local/Cellar/tesseract/5.3.2_1/share/tessdata'
