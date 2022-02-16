# -*- coding:utf-8 -*-
import os
import json

import requests


PROJECT_NAME = 'E:/Development/Python/TFT-OCR-BOT-main'
DATA_CHAMPION_PATH = '/'


class Hero:
    def __init__(self, id, key, name, title):
        self.id = id
        self.key = key
        self.name = name
        self.title = title


def getLatestestVersion():
    data = requests.get("https://ddragon.leagueoflegends.com/api/versions.json", timeout=10).json()
    return data[0]
        

def dowmloadChampionJson(version):
    data = requests.get(f"http://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json").json()

    json_data = {}

    keys = {}
    champion_data = {}
    for i in data['data']:
        hero_info = {}
        keys[data['data'][i]['key']] = i

        idss = data['data'][i]['id']
        keyss = data['data'][i]['key']
        names = data['data'][i]['name']
        titles = data['data'][i]['title']
        champion_data[i.lower()] = Hero(idss, keyss, names, titles).__dict__

    json_data['keys'] = keys
    json_data['data'] = champion_data
    json_data['version'] = data['version']

    output = json.dumps(json_data, separators=(',', ':'), ensure_ascii=False)
    code = f'{output}'
    
    dirs = f'{PROJECT_NAME}{DATA_CHAMPION_PATH}'

    if not os.path.exists(dirs):
        os.makedirs(dirs)
    open(f'{PROJECT_NAME}{DATA_CHAMPION_PATH}/champion.json', 'w').write(code)
    
    
        
        
if __name__ == '__main__':
    game_version = input('input game_version (press Enter get latest version data): ')
    if game_version == '':
        game_version = getLatestestVersion()
        print(f'当前游戏版本：Ver {game_version}')
    dowmloadChampionJson(game_version)
    print('---下载英雄数据完成---')
    print('---操作完成---')