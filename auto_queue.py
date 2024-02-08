"""
Handles getting into a game
"""

from time import sleep
import json
from requests.auth import HTTPBasicAuth
import requests
import urllib3
import settings

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def create_lobby(client_info: tuple) -> bool:
    """Creates a lobby"""
    payload: dict[str, int] = {"queueId": 1090}  # Ranked TFT is 1100
    payload: dict[str, int] = json.dumps(payload)
    try:
        status = requests.post(
            f"{client_info[1]}/lol-lobby/v2/lobby/",
            payload,
            auth=HTTPBasicAuth('riot', client_info[0]),
            timeout=10,
            verify=False,
        )
        if status.status_code == 200:
            print("  Creating lobby")
            return True
        return False
    except ConnectionError:
        return False


def start_queue(client_info: tuple) -> bool:
    """Starts queue"""
    try:
        status = requests.post(
            f"{client_info[1]}/lol-lobby/v2/lobby/matchmaking/search",
            auth=HTTPBasicAuth('riot', client_info[0]),
            timeout=10,
            verify=False,
        )
        if status.status_code == 204:
            print("  Starting queue")
            return True
        return False
    except ConnectionError:
        return False


def check_queue(client_info: tuple) -> bool:
    """Checks queue to see if we are searching"""
    try:
        status = requests.get(
            f"{client_info[1]}/lol-lobby/v2/lobby/matchmaking/search-state",
            auth=HTTPBasicAuth('riot', client_info[0]),
            timeout=10,
            verify=False,
        )
        return status.json()['searchState'] == 'Searching'
    except ConnectionError:
        return False


def check_game_status(client_info: tuple) -> bool:
    """Checks to see if we are in a game"""
    try:
        status = requests.get(
            f"{client_info[1]}/lol-gameflow/v1/session",
            auth=HTTPBasicAuth('riot', client_info[0]),
            timeout=10,
            verify=False,
        )
        return status.json().get("phase", "None")
    except ConnectionError:
        return False


def accept_queue(client_info: tuple) -> bool:
    """Accepts the queue"""
    requests.post(
        f"{client_info[1]}/lol-matchmaking/v1/ready-check/accept",
        auth=HTTPBasicAuth('riot', client_info[0]),
        timeout=10,
        verify=False,
    )


def change_arena_skin(client_info: tuple) -> bool:
    """Changes arena skin to default, other arena skins have different coordinates"""
    try:
        status = requests.delete(
            f"{client_info[1]}/lol-cosmetics/v1/selection/tft-map-skin",
            auth=HTTPBasicAuth('riot', client_info[0]),
            timeout=10,
            verify=False,
        )
        if status.status_code == 204:
            print("  Changed arena skin to default")
            return True
        return False
    except ConnectionError:
        return False


def get_client() -> tuple:
    """Gets data about the client such as port and auth token"""
    print("\n\n[Auto Queue]")
    file_path = settings.LEAGUE_CLIENT_PATH + "\\lockfile"
    got_lock_file = False
    while not got_lock_file:
        try:
            with open(file_path, "r", encoding="utf-8") as data:
                data: list[str] = data.read().split(":")
                app_port: str = data[2]
                remoting_auth_token: str = data[3]
                server_url: str = f"https://127.0.0.1:{app_port}"
                got_lock_file = True
        except IOError:
            print("  Client not open! Trying again in 10 seconds.")
            sleep(10)
    print("  Client found")
    return (remoting_auth_token, server_url)


def reconnect(client_info: tuple) -> None:
    """Reconnect to game when "Failed to Connect" windows are found"""
    requests.post(
        f"{client_info[1]}/lol-gameflow/v1/reconnect",
        auth=HTTPBasicAuth('riot', client_info[0]),
        timeout=10,
        verify=False,
    )


def queue() -> None:
    """Function that handles getting into a game"""
    client_info: tuple = get_client()
    while check_game_status(client_info) == "InProgress":
        sleep(2)
    if check_game_status(client_info) == "Reconnect":
        print("  Reconnecting")
        reconnect(client_info)
        return
    while not create_lobby(client_info):
        sleep(3)

    change_arena_skin(client_info)

    sleep(3)

    while state := check_game_status(client_info):
        if state == "None":
            create_lobby(client_info)
        if state == "Lobby":
            start_queue(client_info)
        if state == "ReadyCheck":
            accept_queue(client_info)
            print("  Accepting")
        if state == "InProgress":
            return
        sleep(3)
