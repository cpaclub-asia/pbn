import multiprocessing

from check_domains_lookup.lookup import check_domain
from shared.args import args_src_dst1_dst2_full_threads
import csv
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor


from queue import Queue





import socket
import tldextract
import re
import urllib.request
from urllib.error import URLError
import os

NUM_PROCESSES = multiprocessing.cpu_count()*12
NUM_THREADS = 20


FILE_SRC,FILE_DST,FILE_CON,CHECK_FULL,NUM_THREADS = args_src_dst1_dst2_full_threads("Connection check", "Src", "No connect", "Connect")
print(f"{CHECK_FULL},{NUM_THREADS}")

'''
def worker(queue):
    while not queue.empty():
        domain = queue.get()
        process_line(domain)
'''


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
    if check_domain(domain,CHECK_FULL):
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
        #queue = Queue()
        #for domain in domains:
        #    queue.put(domain)


        domains = []
        
        for row in reader:
            domains.append(row)
            #queue.put(row)

        #with multiprocessing.Pool(NUM_PROCESSES) as pool:
        #        pool.map(process_line, domains)
        #print(domains)
        '''
        with multiprocessing.Pool(NUM_PROCESSES) as pool:
            with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
                workers = [executor.submit(worker, queue) for _ in range(NUM_PROCESSES)]

                # Дождитесь завершения всех задач
                for worker in workers:
                    worker.result()
        '''
        if NUM_THREADS>1:
            with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
                executor.map(process_line, domains)
        else:
            for line in domains:
                process_line(line)
        

        '''                            
        with multiprocessing.Pool(NUM_PROCESSES) as pool:
            with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
                pool.map(process_line, domains)
        
        '''



if __name__ == "__main__":
    process_domains(FILE_SRC)
    #process_domains('bad.txt')