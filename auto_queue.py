from http import server
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


def create_lobby(message_queue, client_info):
    payload = {"queueId": 1090}  # Ranked TFT is 1100
    payload = json.dumps(payload)
    try:
        status = requests.post(client_info[1] + "/lol-lobby/v2/lobby/", payload,
                            auth=HTTPBasicAuth('riot', client_info[0]), verify=False)
        if status.status_code == 200:
            return True
        else:
            return False
    except ConnectionError:
        return False


def start_queue(message_queue, client_info):
    try:
        status =requests.post(client_info[1] + "/lol-lobby/v2/lobby/matchmaking/search",
                            auth=HTTPBasicAuth('riot', client_info[0]), verify=False)
        if status.status_code == 204:
            return True
        else:
            return False
    except ConnectionError:
        return False


def accept_queue(client_info):
    requests.post(client_info[1] + "/lol-matchmaking/v1/ready-check/accept",
                  auth=HTTPBasicAuth('riot', client_info[0]), verify=False)


def change_arena_skin(client_info):
    try:
        status = requests.delete(client_info[1] + "/lol-cosmetics/v1/selection/tft-map-skin",
                                auth=HTTPBasicAuth('riot', client_info[0]), verify=False)
        if status.status_code == 204:
            return True
        else:
            return False
    except ConnectionError:
        return False


def get_client(message_queue):
    message_queue.put(("CONSOLE", "[Auto Queue]"))
    results = str(subprocess.run(['wmic', 'PROCESS', 'WHERE', "name= 'LeagueClientUx.exe'", 'GET', 'commandline'],
                                 capture_output=True))
    while "--app-port" not in results:  # Means client is not open
        message_queue.put(("CONSOLE", "Client not open! Trying again in 10 seconds..."))
        sleep(10)
        results = str(subprocess.run(['wmic', 'PROCESS', 'WHERE', "name= 'LeagueClientUx.exe'", 'GET', 'commandline'],
                                     capture_output=True))

    sleep(3)
    app_port = re.search("--app-port=([0-9]*)", results)[1]
    remoting_auth_token = re.search("--remoting-auth-token=([\w-]*)", results)[1]
    server_url = f"https://127.0.0.1:{app_port}"
    return (remoting_auth_token, server_url)
    

def queue(message_queue):
    client_info = get_client(message_queue)
    while create_lobby(message_queue, client_info) != True:
        sleep(3)

    change_arena_skin(client_info)

    sleep(5) 
    while start_queue(message_queue, client_info) != True:
        sleep(3)

    in_queue = True
    while in_queue:
        accept_queue(client_info)
        in_game = ImageGrab.grab(bbox=(19, 10, 38, 28))
        array = np.array(in_game)
        if (np.abs(array - (27, 79, 66)) <= 2).all(
                axis=2).any():  # Checks the top left of the loading screen for the green circle
            in_queue = False
        sleep(1)
    message_queue.put(("CONSOLE", "Loading screen found! Waiting for round 1-1"))

