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


def create_lobby(message_queue, server_url, remoting_auth_token):
    payload = {"queueId": 1090}  # Ranked TFT is 1100
    payload = json.dumps(payload)

    try:
        status = requests.post(server_url + "/lol-lobby/v2/lobby/", payload,
                               auth=HTTPBasicAuth('riot', remoting_auth_token), verify=False)
        if status.status_code == 200:
            message_queue.put(("CONSOLE", "Creating TFT lobby."))
            return 200
        else:
            message_queue.put(("CONSOLE", "Failed to create a lobby, trying again..."))
            return 400
    except:  # I don't know what exception this throws
        message_queue.put(("CONSOLE", "Failed to create a lobby, trying again..."))
        return 400


def start_queue(message_queue, server_url, remoting_auth_token):
    try:
        status = requests.post(server_url + "/lol-lobby/v2/lobby/matchmaking/search",
                               auth=HTTPBasicAuth('riot', remoting_auth_token), verify=False)
        if status.status_code == 204:
            message_queue.put(("CONSOLE", "Starting queue"))
            return 204
        else:
            message_queue.put(("CONSOLE", "Queue start failed, trying again..."))
            return 400
    except:  # Same as above
        message_queue.put(("CONSOLE", "Queue start failed, trying again..."))
        return 400


def accept_queue(server_url, remoting_auth_token):
    requests.post(server_url + "/lol-matchmaking/v1/ready-check/accept",
                  auth=HTTPBasicAuth('riot', remoting_auth_token), verify=False)


def change_arena_skin(server_url, remoting_auth_token):
    requests.delete(server_url + "/lol-cosmetics/v1/selection/tft-map-skin",
                    auth=HTTPBasicAuth('riot', remoting_auth_token), verify=False)


def queue(message_queue):
    message_queue.put(("CONSOLE", "[Auto Queue]"))
    results = str(subprocess.run(['wmic', 'PROCESS', 'WHERE', "name= 'LeagueClientUx.exe'", 'GET', 'commandline'],
                                 capture_output=True))
    while "No Instance(s) Available." in results:  # Means client is not open
        message_queue.put(("CONSOLE", "Client not open! Trying again in 10 seconds..."))
        sleep(10)
        results = str(subprocess.run(['wmic', 'PROCESS', 'WHERE', "name= 'LeagueClientUx.exe'", 'GET', 'commandline'],
                                     capture_output=True))

    sleep(3)
    app_port = re.search("--app-port=([0-9]*)", results)[1]
    remoting_auth_token = re.search("--remoting-auth-token=([\w-]*)", results)[1]
    server_url = f"https://127.0.0.1:{app_port}"

    while create_lobby(message_queue, server_url, remoting_auth_token) != 200:
        sleep(3)

    change_arena_skin(server_url, remoting_auth_token)

    sleep(5)  # This should be done differently but im done messing with the LCU
    while start_queue(message_queue, server_url, remoting_auth_token) != 204:
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
    message_queue.put(("CONSOLE", "Loading screen found! Waiting for round 1-1"))
