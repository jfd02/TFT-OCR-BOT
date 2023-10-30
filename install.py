# Original code from the TFT_OCR_BOT repository on GitHub:
# Repository URL: https://github.com/jfd02/TFT-OCR-BOT
# Original authors:
# - @anthony5301
# Modified by the-user-created
#

"""
Install requirements and tesserocr
"""

import os

current_directory = os.getcwd()
REQUIREMENTS = 'requirements.txt'
# Change to the downloaded version (macOS or Windows)
TESSEROCR311 = 'tesserocr-2.6.1-cp311-cp311-macosx_10_9_x86_64.whl'
TESSEROCR310 = 'tesserocr-2.6.1-cp310-cp310-macosx_10_9_x86_64.whl'

if os.path.exists(os.path.join(current_directory, REQUIREMENTS)):
    print("\033[92mFound requirements.txt file. Installing dependencies...\033[0m")
    os.system('pip install -r requirements.txt')
else:
    print("\033[31mrequirements.txt file not found in the current directory.\033[0m")

if os.path.exists(os.path.join(current_directory, TESSEROCR311)):
    print("\033[92mFound tesserocr installation file. Installing...\033[0m")
    os.system('pip install ' + TESSEROCR311)
elif os.path.exists(os.path.join(current_directory, TESSEROCR310)):
    print("\033[92mFound tesserocr installation file. Installing...\033[0m")
    os.system('pip install ' + TESSEROCR310)
else:
    print("\033[31mTesserocr installation file not found.\033[0m")

input("Press Enter to exit...")
