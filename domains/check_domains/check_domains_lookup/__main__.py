import concurrent.futures
import socket
import tldextract
from shared.args import args_src_dst1_dst2
import csv
import re

NUM_WORKERS = 20


def check_domain(line):
    #print(line)
    #global domain_index
    #domain2=line[domain_index]
    domain3=line[0]
    domain4=re.match(r'^[a-z0-9.-]+', domain3).group(0)
    
    #domain3 = domain.split()[0].strip(',').strip(':').strip(';')  # take only the first part before space or comma
    domain2=domain4
    print(domain4)
    
    #extracted = tldextract.extract(domain4)
    #domain2 = extracted.domain + '.' + extracted.suffix

    if len(domain2.split('.')) >= 3:
        print(f"Skipping {domain2}: {line}")
        return
        
        
    #print(domain2)
    try:
        ip = socket.gethostbyname(domain2)
        with open(FILE_CON, 'a') as good_file:
            good_file.write(f"{domain2};{line[1]}\n")
    except Exception as e:
        print(f"{domain2}")
        #with open('2y2_full.txt', 'a') as bad_file:
        #    bad_file.write(f"{domain2} 30 {line}\n")
        with open(FILE_DST, 'a') as bad_file:
            bad_file.write(f"{domain2};{line[1]}\n")

            #bad_file.write(f"{domain}: {str(e)}\n")

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

        print(domains)
                
                

    #with open(filename, 'r') as file:
    #    domains = [line.strip() for line in file]

    #check_domain(domains[0])
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        executor.map(check_domain, domains)

FILE_SRC,FILE_DST,FILE_CON = args_src_dst1_dst2("Connection check", "Src", "No connect", "Connect")

if __name__ == "__main__":
    process_domains(FILE_SRC)
    #process_domains('bad.txt')