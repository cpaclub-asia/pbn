import time
import argparse
from check_domains_google.funcs import get_domains_from_file,append_domain_and_results_to_file


from shared.google.google_parser import get_google_results


from shared.args import args_src_dst1_dst2
SRC,DST_INDEX,DST_NOINDEX = args_src_dst1_dst2("Google check", "Src", "DST_INDEX", "DST_NOINDEX")



domains,data = get_domains_from_file(SRC)
#print(webarchive_get_list("jajaladaexclusivefashion.com",True))

for domain in domains:
    data1=data[domain]
    snippets=""

    results, titles, favicon = get_google_results(domain)
    print(f"Domain {domain} contains {results} results in Google Search")
    print(f"{titles} {favicon}")

    newdata=[results, favicon, titles, snippets]
    if results >= 1:
        append_domain_and_results_to_file(DST_INDEX, domain,newdata,data1)
    else:
        append_domain_and_results_to_file(DST_NOINDEX, domain,newdata,data1)


