import os

current_directory = os.getcwd()
requirements = 'requirements.txt'
tesserocr311 = 'tesserocr-2.6.0-cp311-cp311-win_amd64.whl'
tesserocr310 = 'tesserocr-2.6.0-cp310-cp310-win_amd64.whl'

if os.path.exists(os.path.join(current_directory,requirements)):
    print("\033[92mFound requirements.txt file. Installing dependencies...\033[0m")
    os.system('pip install -r requirements.txt')
else:
    print("\033[31mrequirements.txt file not found in the current directory.\033[0m")

if os.path.exists(os.path.join(current_directory,tesserocr311)):
    print("\033[92mFound tesserocr installation file. Installing...\033[0m")
    os.system('pip install ' + tesserocr311)
elif os.path.exists(os.path.join(current_directory,tesserocr310)):
    print("\033[92mFound tesserocr installation file. Installing...\033[0m")
    os.system('pip install ' + tesserocr310)
else:
    print("\033[31mTesserocr installation file not found.\033[0m")


input("Press Enter to exit...")