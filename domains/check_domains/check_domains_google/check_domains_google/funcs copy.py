import requests
import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
#chrome_options.add_argument("--headless")  # Запуск в фоновом режиме, без отображения окна браузера

driver = webdriver.Chrome(options=chrome_options)



def parse_cookies(cookies_text):
    cookies = {}
    lines = cookies_text.strip().split(";")
    for line in lines:
        if "=" in line:
            key, value = line.split("=", 1)
            cookies[key.strip()] = value.strip()
    return cookies


def get_google_results(domain):
    query = f"https://www.google.com/search?q=site%3A{domain}"
    headers = {
        #"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        
    }
    
    #cookies_text = "1P_JAR=2023-06-18-09; AEC=AUEFqZfz6VtLPaelZFe07ApA3vGlMrpcptjRygiJUqecUEXGNUDpGjQFOZ8; NID=511=Jia-WNUgAOirfLLMfP3tzC3ngKd5TU1QmbcGce6JvJKv-eOQhZiIsKhxL2XNOpPVqZOAEcyugfgIoM8RzerchAiIHpo4OQ_Q1XKaR3FzffVI1a_j0JqVPLzU4OrEuymJtjgmwlxf6UXuBnVOylR-IEucV9Q6dt_kwJRUkUbi4hQ"
    #cookies = parse_cookies(cookies_text)

    #print(query)
    #response = requests.get(query, headers=headers, cookies=cookies)
    driver.get(query)  # Открытие страницы Google
    print("Ожидание result-stats")
    while True:
        try:
            result_stats = driver.find_element(By.ID, "result-stats")
            break
        except:
            time.sleep(1)



    response_text=driver.page_source


    
    #if response.status_code == 200:
    print("Ok.")
    #time.sleep(2)
    soup = BeautifulSoup(response_text, 'html.parser')
    result_stats = soup.find(id="result-stats")
    if result_stats:
        result_stats_text = result_stats.text.replace(',', '').split()[1]
        return int(result_stats_text)
    #elif response.status_code == 429:  # Too Many Requests
    #    # Retry after a delay of 5 seconds
    #    print("Too many requests. Retrying after 5 seconds...")
    #    time.sleep(5)
    #    return get_google_results(domain)
    #
    #return 0


def get_domains_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


def append_domain_and_results_to_file(domain, results, file_path):
    with open(file_path, 'a') as file:
        file.write(f"Domain: {domain}, Results: {results}\n")
