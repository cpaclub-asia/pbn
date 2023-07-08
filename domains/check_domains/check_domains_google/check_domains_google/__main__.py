import time
import argparse
from check_domains_google.funcs import get_domains_from_file,append_domain_and_results_to_file
from shared.google import get_google_results
from shared.webarchive.webarchive_downloader import webarchive_get_list



parser = argparse.ArgumentParser()
parser.add_argument("file", help="Path to the file with the list of domains")
parser.add_argument("results_file", help="Path to the file where the domains found in the search results will be saved")
parser.add_argument("non_results_file", help="Path to the file where the domains not found in the search results will be saved")
args = parser.parse_args()

domains,data = get_domains_from_file(args.file)

for domain in domains:
    data1=data[domain]

    #results = get_google_results(domain)
    results, titles, favicon = get_google_results(domain)
    wa_data_count=[]


    print(f"Domain {domain} contains {results} results in Google Search")
    print(f"{titles} {favicon}")

    snippets=""
    if results > 0:
        try:
            index_files, system_files, html_files, image_files, other_files=webarchive_get_list(domain)
            wa_data_count=[len(html_files),len(image_files),len(other_files)]
        except:
            wa_data_count=[-1,-1,-1]

        append_domain_and_results_to_file(args.results_file, domain,wa_data_count,data1, results, favicon, titles, snippets)
        time.sleep(2)
    else:
        append_domain_and_results_to_file(args.non_results_file, domain,wa_data_count,data1, results, favicon, titles, snippets)
        time.sleep(3)
