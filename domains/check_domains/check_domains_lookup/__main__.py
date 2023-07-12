import multiprocessing
from check_domains_lookup.lookup import process_line
from shared.args import args_src_dst1_dst2
import csv
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor


from queue import Queue



NUM_PROCESSES = multiprocessing.cpu_count()*12
NUM_THREADS = 10

FILE_SRC,FILE_DST,FILE_CON = args_src_dst1_dst2("Connection check", "Src", "No connect", "Connect")


'''
def worker(queue):
    while not queue.empty():
        domain = queue.get()
        process_line(domain)
'''


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