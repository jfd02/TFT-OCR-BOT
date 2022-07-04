from time import sleep
from requests.auth import HTTPBasicAuth
import requests
import urllib3
import json
import settings

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def create_lobby(client_info):
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

def start_queue(client_info):
    try:
        status = requests.post(client_info[1] + "/lol-lobby/v2/lobby/matchmaking/search",
                            auth=HTTPBasicAuth('riot', client_info[0]), verify=False)
        if status.status_code == 204:
            return True
        else:
            return False
    except ConnectionError:
        return False

def check_queue(client_info):
    try:
        status = requests.get(client_info[1] + "/lol-lobby/v2/lobby/matchmaking/search-state",
                            auth=HTTPBasicAuth('riot', client_info[0]), verify=False)
        return True if status.json()['searchState'] == 'Searching' else False
    except ConnectionError:
        return False

def check_game_status(client_info):
    try:
        status = requests.get(client_info[1] + "/lol-gameflow/v1/session",
                            auth=HTTPBasicAuth('riot', client_info[0]), verify=False)
        if status.json()["phase"] == "InProgress":
            return True
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

def get_client():
    file_path = settings.LEAGUE_CLIENT_PATH + "\\lockfile"
    got_lock_file = False
    while got_lock_file is False:
        try:
            data = open(file_path, "r").read().split(':')
            app_port = data[2]
            remoting_auth_token = data[3]
            server_url = f"https://127.0.0.1:{app_port}"
            got_lock_file = True
        except IOError:
            sleep(10)
    return (remoting_auth_token, server_url)

def queue():
    client_info = get_client()
    while create_lobby(client_info) != True:
        sleep(3)

    change_arena_skin(client_info)

    sleep(3)
    while check_queue(client_info) != True:
        sleep(5)
        create_lobby(client_info)
        sleep(3)
        start_queue(client_info)
        sleep(1)

    in_queue = True
    time = 0
    while in_queue:
        if time % 60 == 0:
            create_lobby(client_info)
            sleep(5)
            start_queue(client_info)
        accept_queue(client_info)
        if check_game_status(client_info):
            in_queue = False
        sleep(1)
        time += 1
