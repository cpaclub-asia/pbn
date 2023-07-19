import tldextract
import os

def get_domain_tld(domain):
    extracted = tldextract.extract(domain)
    tld = extracted.suffix
    return tld

def read_file_content(filename):
    try:
        with open(filename, 'rb') as file:
            return 200,file.read()
    except FileNotFoundError:
        return -1, ""

def write_file_content(filename,content):
    directory = os.path.dirname(filename)
    os.makedirs(directory, exist_ok=True)
    with open(filename, "wb") as file:
        file.write(content)

def try_get_cache_webarchive(url, cachedir)
    

def get_cache_path(domain):
    first_letter = domain[0]
    tld=get_domain_tld(domain)
    return f"{tld}/{first_letter}/{domain}"

    