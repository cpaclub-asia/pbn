import requests
#from funcs.file_processor import is_html, is_img,is_root_path
#from webarchive_scrapper.funcs import  is_root_path
from shared.file_processor import is_html, is_img, is_root_path
import re
import os
tldextract


CACHE_DIR="data/cache/"
CACHE_WA_DIR=CACHE_DIR+"webarchive/"

def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return False

def get_cache_path(domain):
    first_letter = domain[0]
    tld=get_domain_tld(domain)
    return=f"{tld}/{first_letter}/{domain}"

def webarchive_get_list(domain, collapse):


    # Form the URL for requesting data from the web archive
    if collapse:
        url = f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=xml&fl=timestamp,original&collapse=urlkey"
        CACHE_WA_DIR_C=CACHE_WA_DIR+"collapse/"
    else:
        url = f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=xml&fl=timestamp,original"
        CACHE_WA_DIR_C=CACHE_WA_DIR+"full/"

    CACHE_FILE_NAME=f"{CACHE_WA_DIR_C}/{get_cache_path(domain)}.index.html"
    from_cache=read_file_content(CACHE_FILE_NAME)
    if(from_cache):
        print("from cache")
        return from_cache
    
    
    # Debug print the URL
    print("Request URL:", url)

    # Send a GET request to retrieve data
    response = requests.get(url)
    print("OK")
    
    with open(CACHE_FILE_NAME", "w") as file:
        file.write(response)

    # Parse the XML response
    response_text = response.text.strip()
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
        timestamp, original_url = row.split(' ', 1)
        clean_url = re.sub(r'[\/:*?"<>|]', '_', original_url.strip())

        # Form the URL for downloading data
        download_url = f"https://web.archive.org/web/{timestamp}/{original_url}"

        # Determine the file type based on the URL
        file_extension = os.path.splitext(clean_url)[1].lower()

        # Add the file to the appropriate list
        if is_root_path(original_url):
            index_files.append(download_url)
        elif is_html(clean_url):
            html_files.append(download_url)
        elif original_url.endswith('sitemap.xml') or original_url.endswith('robots.txt') or original_url.endswith('favicon.ico') or original_url.endswith('ads.txt'):
            system_files.append(download_url)
        elif is_img(clean_url):
            image_files.append(download_url)
        else:
            other_files.append(download_url)

        # Check if the current version is the latest
        if clean_url not in last_versions:
            last_versions[clean_url] = download_url
    
    return index_files, system_files, html_files, image_files, other_files