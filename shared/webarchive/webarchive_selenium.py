from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import requests
import time
import base64

import threading
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


#chrome_options.add_argument("--headless")  # Запуск в фоновом режиме, без отображения окна браузера
chrome_options = Options()

'''
# Disable images
chrome_prefs = {
    "profile.managed_default_content_settings.images": 2,
}


chrome_options.add_experimental_option("prefs", chrome_prefs)


# Set maximum file size for downloads (in bytes)
max_file_size = 1024 * 1024  # Example: 1MB
caps = DesiredCapabilities.CHROME

caps['prefs'] = {
    "download_restrictions": 3,
    "download_restrictions_extra": f"max_bytes={max_file_size}",
}

# Instantiate the WebDriver with the modified options and capabilities
driver = webdriver.Chrome(options=chrome_options, desired_capabilities=caps)
'''

driver = webdriver.Chrome(options=chrome_options)




domain_before=""

def webarchive_selenium_page(domain, timestamp):
    global domain_before

    if domain_before != "":
        #Save results of previous domain
        response_text=driver.page_source
        if not "Redirecting to..." in response_text:
            driver.save_screenshot(f"data/screen-data/webarchive/{domain}_{timestamp}.png")
    
    domain_before=domain
        

    query = f"https://web.archive.org/web/{timestamp}/http://{domain}/"
    
    #driver.get(query)
    def load_page():
        #driver.execute_script(f"window.open('{query}')")
        driver.get(query)

    threading.Thread(target=load_page).start()

    return
