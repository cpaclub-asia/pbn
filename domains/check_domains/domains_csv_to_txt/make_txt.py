
import tldextract
import csv

csv_file = 'src/info_2y.csv'  # Replace with your CSV file name
txt_file = 'src/info_2y.txt'  # Replace with the desired output text file name


unique_domains = set()  # Set to store unique values

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        domain = row['Domain']
        extracted = tldextract.extract(domain)
        domain2 = extracted.domain + '.' + extracted.suffix
        if domain2 not in unique_domains:
            unique_domains.add(domain2)

with open(txt_file, 'w') as file:
    file.write(' 30\n'.join(unique_domains))

