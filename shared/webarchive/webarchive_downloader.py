import requests
#from funcs.file_processor import is_html, is_img,is_root_path
#from webarchive_scrapper.funcs import  is_root_path
from shared.file_processor import is_html, is_img, is_root_path, is_system
import re
import os
import tldextract
from shared.cache import get_cache_path,write_file_content,read_file_content
from shared.inet import try_get,try_get_bin
import traceback
import time

CACHE_DIR="data/cache/"
CACHE_WA_DIR=CACHE_DIR+"webarchive/"


import requests_cache
cache_dir = os.path.abspath("data/cache/webarchive/lists")
requests_cache.install_cache('cache_webarchive_lists', use_cache_dir=True, cache_dir=cache_dir)

def webarchive_get_list(domain, collapse, additional):
    print(f"Checking {domain}")

    # Form the URL for requesting data from the web archive
    if collapse and collapse!="urlkey":
        collapse="digest"        

    if collapse:
        # additional = "&from=YYYYMMDDHHMMSS&to=YYYYMMDDHHMMSS"
        # https://web.archive.org/cdx/search/cdx?url=noema.info/*&output=xml&fl=timestamp,original&collapse=digest
        # was collapse=urlkey
        # digest
        url = f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=xml&fl=timestamp,original&collapse={collapse}"
        url += "&filter=statuscode:200&sort=date"
        CACHE_WA_DIR_C=CACHE_WA_DIR+f"{collapse}_{additional}/"        
    else:
        url = f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=xml&fl=timestamp,original"
        CACHE_WA_DIR_C=CACHE_WA_DIR+f"full_{additional}/"

    print(CACHE_WA_DIR_C)

    CACHE_FILE_NAME=""
    code=0
    from_cache="NOFILE"
    
    if additional:
        url+="&"+additional.strip()
    else:
        CACHE_FILE_NAME=f"{CACHE_WA_DIR_C}/{get_cache_path(domain)}.index.html"
        #code,from_cache=read_file_content(CACHE_FILE_NAME)


    '''
    response_text=""

    if(code==200):
        print("from cache")
        response_text=from_cache
    else:
        # Debug print the URL
        print("Request URL:", url)

        # Send a GET request to retrieve data
        code,response_text=try_get_bin(url)
        #time.sleep(1)
        print("OK")
        # Parse the XML response
        if CACHE_FILE_NAME:
            write_file_content(CACHE_FILE_NAME,response_text)
        response_text=response_text.decode('utf-8')
    print(response_text)
    '''

    #code,
    response_text=try_get(url)
    if(response_text==""):
        return [], [], [], [], []

    rows = response_text.split('\n')

    # Dictionary to store the last versions of each file
    last_versions = {}
    urls_files ={}

    # Lists to store different types of files
    index_files = []
    system_files = []
    html_files = []
    image_files = []
    other_files = []


    # Process each URL address
    for row in rows:
        parts=row.split(' ', 1)
        if len(parts) < 2:
            continue
        timestamp, original_url = parts
        clean_url = re.sub(r'[\/:*?"<>|]', '_', original_url.strip())

        # Form the URL for downloading data
        download_url = f"https://web.archive.org/web/{timestamp}/{original_url}"

        # Add the file to the appropriate list
        if is_root_path(original_url):
            index_files.append(download_url)
        elif is_html(original_url):
            html_files.append(download_url)
        elif is_system(original_url):
            system_files.append(download_url)
        elif is_img(original_url):
            image_files.append(download_url)
        else:
            other_files.append(download_url)

        # Check if the current version is the latest
        if clean_url not in last_versions:
            last_versions[clean_url] = download_url
    #print ([index_files, system_files, html_files, image_files, other_files])
    return index_files, system_files, html_files, image_files, other_files