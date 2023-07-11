import concurrent.futures
import socket
import tldextract
from shared.args import args_src_dst1_dst2
import csv
import re
import urllib.request
from urllib.error import URLError
import os

NUM_WORKERS = 200

FILE_SRC,FILE_DST,FILE_CON = args_src_dst1_dst2("Connection check", "Src", "No connect", "Connect")

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
    download_url(f"https://{domain}/",f"{CACHE_INDEX_DIR}/{tld}/{first_letter}/{domain}.index.html")
    print(".")
    download_url(f"https://{domain}/robots.txt",f"{CACHE_ROBOTS_DIR}/{tld}/{first_letter}/{domain}.robots.txt")
    print(".")
    download_url(f"https://{domain}/favicon.ico",f"{CACHE_FAVICON_DIR}/{tld}/{first_letter}/{domain}.favicon.ico")
    print(".")
    download_url(f"https://{domain}/sitemap.xml",f"{CACHE_SITEMAP_DIR}/{tld}/{first_letter}/{domain}.sitemap.xml")
    print(".")
    download_url(f"https://{domain}/ads.txt",f"{CACHE_ADS_DIR}/{tld}/{first_letter}/{domain}.ads.txt")    
    print(".")
    return True




def process_line(line):
    #print(line)
    #global domain_index
    #domain2=line[domain_index]
    domain3=line[0]
    domain4=re.match(r'^[a-z0-9.-]+', domain3).group(0)
    
    #domain3 = domain.split()[0].strip(',').strip(':').strip(';')  # take only the first part before space or comma
    domain2=domain4
    #print(domain4)
    
    #extracted = tldextract.extract(domain4)
    #domain2 = extracted.domain + '.' + extracted.suffix

    if len(domain2.split('.')) >= 3:
        print(f"Skipping {domain2}: {line}")
        return
        
    domain=domain2

    #print(domain)
    if check_domain(domain,True):
        with open(FILE_CON, 'a') as good_file:
            good_file.write(f"{domain};{line[1]}\n")
    else:
        with open(FILE_DST, 'a') as bad_file:
            bad_file.write(f"{domain};{line[1]}\n")





def process_domains(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        headers = next(reader)  # Считываем заголовки столбцов

        if 'Domain' in headers:
            domain_index = headers.index('Domain')
        else:
            domain_index = 0  # Если столбец "Domain" не найден, читаем из первого столбца

        #data = {}
        domains = []
        
        for row in reader:
            domains.append(row)

        #print(domains)
                                
    if NUM_WORKERS>1:
        with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
            executor.map(process_line, domains)
    else:
        for line in domains:
            process_line(line)




if __name__ == "__main__":
    process_domains(FILE_SRC)
    #process_domains('bad.txt')