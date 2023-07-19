from shared.google.google_selenium import google_selenium_page,google_selenium_screenshot



from bs4 import BeautifulSoup



import requests
import time
import base64

from shared.cache import get_cache_path,write_file_content,read_file_content



# Set additional options if needed
# chrome_options.add_argument('--headless')  # Uncomment this line to run in headless mode



DELAY_GOOGLE=40




CACHE_DIR="data/cache/"
CACHE_GOOGLE_DIR=CACHE_DIR+"google/"

SCREENS_DIR="data/screens/"
SCREENS_GOOGLE_DIR=CACHE_DIR+"google/"
SCREENS_FAVICONS_DIR=CACHE_DIR+"favicons/"



def parse_cookies(cookies_text):
    cookies = {}
    lines = cookies_text.strip().split(";")
    for line in lines:
        if "=" in line:
            key, value = line.split("=", 1)
            cookies[key.strip()] = value.strip()
    return cookies


def get_google_results(domain):
    CACHE_FILE_NAME=f"{CACHE_GOOGLE_DIR}/{get_cache_path(domain)}.google.html"
    from_cache=read_file_content(CACHE_FILE_NAME)

    response_text=""

    if(from_cache!="NOFILE"):
        print("from cache")
        response_text=from_cache
    else:
        response_text=google_selenium_page(domain)
        print("Ok")
        write_file_content(CACHE_FILE_NAME,response_text)

    print(response_text)

    soup = BeautifulSoup(response_text, 'html.parser')
    result_stats = soup.find(id="result-stats")

    if result_stats:
        result_stats_text = result_stats.text.replace(',', '').split()[1]
        if result_stats_text=="results":
            result_stats_text = result_stats.text.replace(',', '').split()[0]
        if result_stats_text=="кiлькость":
            result_stats_text = result_stats.text.replace(',', '').split()[0]
        if result_stats_text=="количество":
            result_stats_text = result_stats.text.replace(',', '').split()[0]

        # Find all search result titles
        search_results = soup.find_all("h3")
        #print(search_results)

        #search_results = soup.find_all("h3", class_="LC20lb DKV0Md")
        #print(search_results)
        titles = [result.get_text() for result in search_results]

        #favicon_link = soup.find("link", rel="shortcut icon")
        #favicon_url = favicon_link["href"] if favicon_link else ""
        favicon_img = soup.find("img", class_="XNo5Ab")
        favicon_url = favicon_img["src"] if favicon_img else ""

        favicon_file = save_favicon(favicon_url, domain) if favicon_url else ""
        print(domain)
        print(result_stats_text)

        if(int(result_stats_text))>0:
            if(from_cache!=True):
                google_selenium_screenshot(f"data/screen-data/google/{domain}_google.png")

        if(from_cache!="NOFILE"):
            print("From cache, no delay")
        else:
            print(f"sleep {DELAY_GOOGLE}")
            time.sleep(DELAY_GOOGLE)

        return int(result_stats_text), titles, favicon_file



    #elif response.status_code == 429:  # Too Many Requests
    #    # Retry after a delay of 5 seconds
    #    print("Too many requests. Retrying after 5 seconds...")
    #    time.sleep(5)
    #    return get_google_results(domain)
    #
    #return 0



def save_favicon(favicon_url, domain):

    if favicon_url.startswith("data:image/png;base64,"):
        # Remove the "data:image/png;base64," prefix
        favicon_base64 = favicon_url[len("data:image/png;base64,"):]

        # Decode the base64 image data
        favicon_data = base64.b64decode(favicon_base64)

        # Generate the file name
        file_name = f"data/screen-data/favicons/{domain}.png"

        # Save the favicon image as a file
        '''
        with open(file_name, "wb") as file:
            file.write(favicon_data)
        '''

        return file_name
    else:
        return None    
