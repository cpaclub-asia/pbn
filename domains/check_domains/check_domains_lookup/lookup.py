
import socket
import tldextract
import re
import urllib.request
from urllib.error import URLError
import os



CACHE_DIR="data/cache/web/"
CACHE_INDEX_DIR=CACHE_DIR+"index/"
CACHE_ROBOTS_DIR=CACHE_DIR+"robots/"
CACHE_FAVICON_DIR=CACHE_DIR+"favicon/"
CACHE_SITEMAP_DIR=CACHE_DIR+"sitemap/"
CACHE_ADS_DIR=CACHE_DIR+"ads/"


def get_domain_tld(domain):
    extracted = tldextract.extract(domain)
    tld = extracted.suffix
    return tld

def download_url(url, save_path):
    try:
        directory = os.path.dirname(save_path)
        os.makedirs(directory, exist_ok=True)
        urllib.request.urlretrieve(url, save_path)
        return True
    except urllib.error.URLError as e:
        return False



def check_domain(domain,full):
    print(domain);
    try:
        ip_address = socket.gethostbyname(domain)
        print("+")
    except socket.gaierror:
        print("-")
        return False
    if not full:
        return True

    first_letter = domain[0]
    tld=get_domain_tld(domain)
    r=download_url(f"https://{domain}/",f"{CACHE_INDEX_DIR}/{tld}/{first_letter}/{domain}.index.html")
    if not r:
        print("-")
        return False
    download_url(f"https://{domain}/robots.txt",f"{CACHE_ROBOTS_DIR}/{tld}/{first_letter}/{domain}.robots.txt")
    print("+")
    download_url(f"https://{domain}/favicon.ico",f"{CACHE_FAVICON_DIR}/{tld}/{first_letter}/{domain}.favicon.ico")
    print(".")
    download_url(f"https://{domain}/sitemap.xml",f"{CACHE_SITEMAP_DIR}/{tld}/{first_letter}/{domain}.sitemap.xml")
    print(".")
    download_url(f"https://{domain}/ads.txt",f"{CACHE_ADS_DIR}/{tld}/{first_letter}/{domain}.ads.txt")    
    print(".")
    return True




