import traceback
import time
import requests
import os

import requests_cache


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
        print("sleep 120")
        time.sleep(120)


def try_get_bin(url,cache):
    cache_dir = os.path.abspath(f"data/cache/www/{cache}")
    #requests_cache.install_cache(cache_dir,backend="filesystem", serializer='json', expire_after=None)
    requests_cache.install_cache(cache_dir,backend="sqlite", expire_after=None)

    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return 200,response.content
            return 0,""
        except Exception as e:
            print(f"ERROR!!!! WHILE GET WA")
            print(str(e))
            traceback.print_exc()
        print("sleep 120")
        time.sleep(120)

