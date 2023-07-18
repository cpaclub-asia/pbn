


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
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