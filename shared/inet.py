import traceback
import time
import requests

def try_get(url):
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text.strip() #response.content
        except Exception as e:
            print(f"ERROR!!!! WHILE GET WA")
            print(str(e))
            traceback.print_exc()
        print("sleep 120")
        time.sleep(120)