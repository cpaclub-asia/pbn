import argparse
from funcs import get_google_results,get_domains_from_file,append_domain_and_results_to_file,save_favicon




parser = argparse.ArgumentParser()
parser.add_argument("file", help="Path to the file with the list of domains")
parser.add_argument("results_file", help="Path to the file where the domains found in the search results will be saved")
parser.add_argument("non_results_file", help="Path to the file where the domains not found in the search results will be saved")
args = parser.parse_args()

domains = get_domains_from_file(args.file)

for domain in domains:
    #results = get_google_results(domain)
    results, titles, favicon = get_google_results(domain)

    print(f"Domain {domain} contains {results} results in Google Search")
    print(f"{titles} {favicon}")

    snippets=""
    if results > 0:
        append_domain_and_results_to_file(args.results_file, domain, results, favicon, titles, snippets)
    else:
        append_domain_and_results_to_file(args.non_results_file, domain, results, favicon, titles, snippets)
