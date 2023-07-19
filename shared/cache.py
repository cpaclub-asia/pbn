import tldextract
import os

def get_domain_tld(domain):
    extracted = tldextract.extract(domain)
    tld = extracted.suffix
    return tld

def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ""

def write_file_content(filename,content):
    directory = os.path.dirname(filename)
    os.makedirs(directory, exist_ok=True)
    with open(filename, "w") as file:
        file.write(content)


def get_cache_path(domain):
    first_letter = domain[0]
    tld=get_domain_tld(domain)
    return f"{tld}/{first_letter}/{domain}"

    