
import tldextract
import csv

PATH = "data/domains-data/domains/github"
csv_file = PATH+"/github_all.csv"  # Replace with your CSV file name
txt_file = PATH+"/github_all.txt"  # Replace with the desired output text file name

#csv_file = 'pbn-data/google/domes_google.csv'  # Replace with your CSV file name
#txt_file = 'pbn-data/domains/google/domes_google.txt'  # Replace with the desired output text file name


unique_domains_a = []
unique_domains = set()

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        domain = row['Domain']
        extracted = tldextract.extract(domain)
        domain2 = extracted.domain + '.' + extracted.suffix
        if domain2 not in unique_domains:
            unique_domains.add(domain2)
            unique_domains_a.append(domain2)

with open(txt_file, 'w') as file:
    file.write(' 30\n'.join(unique_domains_a))

