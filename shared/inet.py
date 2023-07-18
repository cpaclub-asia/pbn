import traceback
import time
import requests

def try_get(url):
    while True:
        try:
            response = requests.get(url)
            if response !="":
                return response
        except Exception as e:
            print(f"ERROR!!!! WHILE GET WA")
            print(str(e))
            traceback.print_exc()
        print("sleep 300")
        time.sleep(300)