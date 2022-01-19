import subprocess
import re
from requests.auth import HTTPBasicAuth
import requests
import urllib3
import json
from time import sleep
from PIL import ImageGrab
import numpy as np

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def create_lobby(server_url, remoting_auth_token):
    payload = {"queueId": 1090}  # Ranked TFT is 1100
    payload = json.dumps(payload)

    try:
        status = requests.post(server_url + "/lol-lobby/v2/lobby/", payload,
                               auth=HTTPBasicAuth('riot', remoting_auth_token), verify=False)
        if status.status_code == 200:
            print("\tCreating TFT lobby.")
            return 200
        else:
            print("\tFailed to create a lobby, trying again...")
            return 400
    except:  # I don't know what exception this throws
        print("\tFailed to create a lobby, trying again...")
        return 400


def start_queue(server_url, remoting_auth_token):
    try:
        status = requests.post(server_url + "/lol-lobby/v2/lobby/matchmaking/search",
                               auth=HTTPBasicAuth('riot', remoting_auth_token), verify=False)
        if status.status_code == 204:
            print("\tStarting queue")
            return 204
        else:
            print("\tQueue start failed, trying again...")
            return 400
    except:  # Same as above
        print("\tQueue start failed, trying again...")
        return 400


def accept_queue(server_url, remoting_auth_token):
    requests.post(server_url + "/lol-matchmaking/v1/ready-check/accept",
                  auth=HTTPBasicAuth('riot', remoting_auth_token), verify=False)


def queue():
    print("\n[auto_queue.py queue()]")
    results = str(subprocess.run(['wmic', 'PROCESS', 'WHERE', "name= 'LeagueClientUx.exe'", 'GET', 'commandline'],
                                 capture_output=True))
    while "No Instance(s) Available." in results:  # Means client is not open
        print("\tClient not open! Trying again in 10 seconds...")
        sleep(10)
        results = str(subprocess.run(['wmic', 'PROCESS', 'WHERE', "name= 'LeagueClientUx.exe'", 'GET', 'commandline'],
                                     capture_output=True))

    sleep(3)
    app_port = re.search("--app-port=([0-9]*)", results)[1]
    remoting_auth_token = re.search("--remoting-auth-token=([\w-]*)", results)[1]
    server_url = f"https://127.0.0.1:{app_port}"

    while create_lobby(server_url, remoting_auth_token) != 200:
        sleep(3)
    sleep(5)  # This should be done differently but im done messing with the LCU
    while start_queue(server_url, remoting_auth_token) != 204:
        sleep(3)
    in_queue = True
    while in_queue:
        accept_queue(server_url, remoting_auth_token)
        in_game = ImageGrab.grab(bbox=(19, 10, 38, 28))
        array = np.array(in_game)
        if (np.abs(array - (27, 79, 66)) <= 2).all(
                axis=2).any():  # Checks the top left of the loading screen for the green circle
            in_queue = False
        sleep(1)
    print("\tLoading screen found! Waiting for round 1-1")


if __name__ == "__main__":  # used for testing
    queue()