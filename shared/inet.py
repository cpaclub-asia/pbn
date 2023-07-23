import traceback
import time
import requests
import os

import requests_cache

DELAY_ON_ERROR=120
DELAY_ON_TIMEOUT=60
GET_TIMEOUT=120

def try_get(url,cache):
    cache_dir = os.path.abspath(f"data/cache/www/{cache}")
    #requests_cache.install_cache(cache_dir,backend="filesystem", serializer='json', expire_after=None)
    requests_cache.install_cache(cache_dir,backend="sqlite", expire_after=None)
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text #.strip() #response.content
        except Exception as e:
            print(f"ERROR!!!! WHILE GET WA")
            print(str(e))
            traceback.print_exc()
            print(f"sleep {DELAY_ON_ERROR}")
            time.sleep(DELAY_ON_ERROR)


def try_get_bin(url,cache):
    cache_dir = os.path.abspath(f"data/cache/www/{cache}")
    #requests_cache.install_cache(cache_dir,backend="filesystem", serializer='json', expire_after=None)
    requests_cache.install_cache(cache_dir,backend="sqlite", expire_after=None)

    while True:
        try:
            response = requests.get(url,timeout=GET_TIMEOUT)
            if response.status_code == 200:
                return 200,response.content
            return 0,""
        except requests.exceptions.Timeout:
            print("Таймаут истек при выполнении запроса.")
            print(f"sleep {DELAY_ON_TIMEOUT}")
            time.sleep(DELAY_ON_TIMEOUT)
        except Exception as e:
            print(f"ERROR!!!! WHILE GET WA")
            print(str(e))
            traceback.print_exc()
            print(f"sleep {DELAY_ON_ERROR}")
            time.sleep(DELAY_ON_ERROR)

