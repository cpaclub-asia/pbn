import os
from dotenv import load_dotenv


import requests
import csv
import pandas as pd
from urllib.parse import urlparse

# Constants
NUM_RESULTS = 89
#KEYWORDS_FILE = 'src/fulldome_test.csv'
KEYWORDS_FILE = 'src/pacificdomes.csv.4'
RESULTS_FILE = 'dst/pacificdomes_google.csv.4'


load_dotenv()
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
CUSTOM_SEARCH_ENGINE_ID=os.getenv('CUSTOM_SEARCH_ENGINE_ID')


def get_top_domains(keywords, search_volumes, cpcs, api_key, cx):
    domains = []
    for keyword, search_volume, cpc in zip(keywords, search_volumes, cpcs):
        print("Processing keyword:", keyword)
        results = perform_search(keyword, api_key, cx)
        for position, result in enumerate(results, start=1):
            title = result['title']
            full_url = result['link']
            domain = extract_domain(full_url)
            domain2 = extract_domain_2nd_level(domain)
            domains.append(domain2)
            print("Keyword:", keyword, "| Position:", position, "| Result:", domain2)
            save_results(domain2, domain, keyword, search_volume, cpc, position, title, result.get('snippet', ''), full_url)
    return domains


def perform_search(keyword, api_key, cx):
    print("Performing search for keyword:", keyword)
    results = []
    start = 1
    while start <= NUM_RESULTS:
        print("Making API request for keyword:", keyword, "| Start:", start)
        url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={keyword}&start={start}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])
            if not items:
                break  # Break out of the loop if items is empty
            results.extend(items)
            start += len(items)
        else:
            print("Error: Request failed with status code", response.status_code)
            break
    return results

def extract_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc


def extract_domain_2nd_level(domain):
    split_domain = domain.split('.')
    if len(split_domain) > 2:
        return '.'.join(split_domain[-2:])
    return domain


def save_results(domain2, domain, keyword, search_volume, cpc, position, title, snippet, full_url):
    with open(RESULTS_FILE, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([domain2, domain, keyword, search_volume, cpc, position, title, snippet, full_url])


# Read the keywords.csv file using pandas
df = pd.read_csv(KEYWORDS_FILE)

# Extract the lists of keywords, search volumes, and CPC
keywords = df['Keyword'].tolist()
search_volumes = df['Search Volume'].tolist()
cpcs = df['CPC'].tolist()

# Save the column headers to the results.csv file
with open(RESULTS_FILE, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Domain2', 'Domain', 'Keyword', 'Search Volume', 'CPC', 'Position', 'Title', 'Snippet', 'Full URL'])

# Call the get_top_domains function with the constants
top_domains = get_top_domains(keywords, search_volumes, cpcs, GOOGLE_API_KEY, CUSTOM_SEARCH_ENGINE_ID)

print("Results saved in", RESULTS_FILE)