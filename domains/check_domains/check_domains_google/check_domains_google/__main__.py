import time
import argparse
from check_domains_google.funcs import get_domains_from_file,append_domain_and_results_to_file
from shared.google import get_google_results
from shared.webarchive.webarchive_downloader import webarchive_get_list
from shared.webarchive.webarchive_selenium import webarchive_selenium_page

WA_MIN=1
parser = argparse.ArgumentParser()
parser.add_argument("file", help="Path to the file with the list of domains")
parser.add_argument("results_file", help="Path to the file where the domains found in the search results will be saved")
parser.add_argument("non_results_file", help="Path to the file where the domains not found in the search results will be saved")
parser.add_argument("nowa_results_file", help="Path to the file where the domains not found in the search results will be saved")
args = parser.parse_args()

domains,data = get_domains_from_file(args.file)

#print(webarchive_get_list("jajaladaexclusivefashion.com",True))

for domain in domains:
    data1=data[domain]

    #results = get_google_results(domain)
    #try:
    index_files, system_files, html_files, image_files, other_files=webarchive_get_list(domain,True)
    wa_data_count=[len(index_files),len(html_files),len(image_files),len(other_files)]
    print([len(index_files),len(html_files),len(image_files),len(other_files)])
    #except:
    #    wa_data_count=[-1,-1,-1]

    print(f"Domain {domain} WA {wa_data_count[0]} ")

    snippets=""

    if wa_data_count[0] >= WA_MIN:
        results, titles, favicon = get_google_results(domain)
        print(f"Domain {domain} contains {results} results in Google Search")
        print(f"{titles} {favicon}")

        if results >= 1:
            webarchive_selenium_page(domain,"20230101005413")
            #webarchive_selenium_page(domain,"20220101005413")
            webarchive_selenium_page(domain,"20210101005413")
            #webarchive_selenium_page(domain,"20200606005413")

            append_domain_and_results_to_file(args.results_file, domain,wa_data_count,data1, results, favicon, titles, snippets)
            time.sleep(5)
        else:
            append_domain_and_results_to_file(args.non_results_file, domain,wa_data_count,data1, results, favicon, titles, snippets)
            time.sleep(5)

    else:
        results, titles, favicon=[-1,"",""]
        append_domain_and_results_to_file(args.nowa_results_file, domain,wa_data_count,data1, results, favicon, titles, snippets)
        time.sleep(1)


