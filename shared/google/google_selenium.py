import time


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
#chrome_options.add_argument("--lang=en-US")  # Устанавливаем язык на английский
chrome_options.add_argument('--geolocation=42.3601,-71.0589')
chrome_options.add_argument('--timezone=America/New_York')
chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en-US,en'})
chrome_options.add_argument("--lang=en-US,en;q=0.9")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36")

#chrome_options.add_argument("--headless")  # Запуск в фоновом режиме, без отображения окна браузера

#chrome_path = '/usr/bin/chromium-browser'
#chrome_options.binary_location = chrome_path

driver = webdriver.Chrome(options=chrome_options)



def google_selenium_page(domain):
    url = f"https://www.google.com/search?q=site%3A{domain}"
    print("Request URL:", url)


    driver.get(url) 
    print("Ожидание result-stats")
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "result-stats")))
    while True:
        try:
            result_stats = driver.find_element(By.ID, "result-stats")
            break
        except:
            time.sleep(1)

    return driver.page_source

def google_selenium_screenshot(filename):
    driver.save_screenshot(filename)