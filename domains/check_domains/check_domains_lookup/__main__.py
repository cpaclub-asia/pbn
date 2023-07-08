import concurrent.futures
import socket
import tldextract
from shared.args import args_src_dst1_dst2

NUM_WORKERS = 100


def check_domain(line):
    domain3 = line.split()[0].strip(',').strip(':')  # take only the first part before space or comma
    extracted = tldextract.extract(domain3)
    domain2 = extracted.domain + '.' + extracted.suffix

    if len(domain2.split('.')) >= 3:
        print(f"Skipping {domain2}: {line}")
        return
        
        
    #print(domain2)
    try:
        ip = socket.gethostbyname(domain2)
        with open(FILE_CON, 'a') as good_file:
            good_file.write(f"{domain2} 30\n")
    except Exception as e:
        print(f"{domain2} 30 {line}")
        #with open('2y2_full.txt', 'a') as bad_file:
        #    bad_file.write(f"{domain2} 30 {line}\n")
        with open(FILE_DST, 'a') as bad_file:
            bad_file.write(f"{domain2} 30\n")

            #bad_file.write(f"{domain}: {str(e)}\n")

def process_domains(filename):
    with open(filename, 'r') as file:
        domains = [line.strip() for line in file]

    check_domain(domains[0])
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        executor.map(check_domain, domains)

FILE_SRC,FILE_DST,FILE_CON = args_src_dst1_dst2("Connection check", "Src", "No connect", "Connect")

if __name__ == "__main__":
    process_domains(FILE_SRC)
    #process_domains('bad.txt')