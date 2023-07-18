from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import requests
import time
import base64

import threading
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


#chrome_options.add_argument("--headless")  # Запуск в фоновом режиме, без отображения окна браузера
chrome_options = Options()
#chrome_options.add_argument("user-data-dir=C:\\Path\\To\\Custom\\Profile")

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

'''
        # Path To Custom Profile
        options.add_argument("user-data-dir=C:\\Path\\To\\Custom\\Profile")
        self.driver = webdriver.Chrome(PATH, options=options)

        chrome://version
'''

'''
saveas = ActionChains(driver).key_down(Keys.CONTROL).send_keys('S').key_up(Keys.CONTROL).send_keys('MyDocumentName').key_down(Keys.ALT).send_keys('S').key_up(Keys.ALT)
'''


'''
from selenium import webdriver
import chromedriver_binary
from lxml import html
import requests
import os

driver = webdriver.Chrome()
URL = 'https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastx&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome'
SEQUENCE = 'CCTAAACTATAGAAGGACAGCTCAAACACAAAGTTACCTAAACTATAGAAGGACAGCTCAAACACAAAGTTACCTAAACTATAGAAGGACAGCTCAAACACAAAGTTACCTAAACTATAGAAGGACAGCTCAAACACAAAGTTACCTAAACTATAGAAGGACA' 
base = 'https://blast.ncbi.nlm.nih.gov/'

driver.get(URL)
seq_query_field = driver.find_element_by_id("seq")
seq_query_field.send_keys(SEQUENCE)
blast_button = driver.find_element_by_id("b1")
blast_button.click()

content = driver.page_source
# write the page content
os.mkdir('page')
with open('page/page.html', 'w') as fp:
    fp.write(content)

# download the referenced files to the same path as in the html
sess = requests.Session()
sess.get(base)            # sets cookies

# parse html
h = html.fromstring(content)
# get css/js files loaded in the head
for hr in h.xpath('head//@href'):
    if not hr.startswith('http'):
        local_path = 'page/' + hr
        hr = base + hr
    res = sess.get(hr)
    if not os.path.exists(os.path.dirname(local_path)):
        os.makedirs(os.path.dirname(local_path))
    with open(local_path, 'wb') as fp:
        fp.write(res.content)

# get image/js files from the body.  skip anything loaded from outside sources
for src in h.xpath('//@src'):
    if not src or src.startswith('http'):
        continue
    local_path = 'page/' + src
    print(local_path)
    src = base + src
    res = sess.get(hr)
    if not os.path.exists(os.path.dirname(local_path)):
        os.makedirs(os.path.dirname(local_path))
    with open(local_path, 'wb') as fp:
        fp.write(res.content)  

'''

driver = webdriver.Chrome(options=chrome_options)
#wait = WebDriverWait(driver, 600)
driver.implicitly_wait(600)


domain_before=""

def webarchive_selenium_page(domain, timestamp):
    global domain_before

    if domain_before != "":
        #Save results of previous domain
        response_text=driver.page_source
        if not "Redirecting to..." in response_text:
            try:
                driver.save_screenshot(f"data/screen-data/webarchive/{domain}_webarchive_{timestamp}.png")
            except:
                print("save screen failed")
    
    domain_before=domain
        

    query = f"https://web.archive.org/web/{timestamp}/http://{domain}/"
    
    #driver.get(query)
    def load_page():
        #driver.execute_script(f"window.open('{query}')")
        driver.get(query)

    threading.Thread(target=load_page).start()

    return
