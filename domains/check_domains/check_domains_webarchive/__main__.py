import time
import argparse

from check_domains_webarchive.funcs import get_domains_from_file,append_domain_and_results_to_file_wa


from shared.webarchive.webarchive_downloader import webarchive_get_list
from shared.webarchive.webarchive_selenium import webarchive_selenium_page

from shared.args import args_src_dst1_dst2

SRC,DST_WA,DST_NOWA = args_src_dst1_dst2("Webarchive check", "Src", "DST_WA", "DST_NOWA")
print(f"{SRC},{DST_WA},{DST_NOWA}")


domains,data = get_domains_from_file(SRC)
#print(webarchive_get_list("jajaladaexclusivefashion.com",True))


for domain in domains:
    data1=data[domain]


    index_files, system_files, html_files, image_files, other_files=webarchive_get_list(domain,True,"")
    wa_data_count=[len(index_files),len(html_files),len(image_files),len(other_files)]
    print([len(index_files),len(html_files),len(image_files),len(other_files)])

    print(f"Domain {domain} WA {wa_data_count[0]} ")
    if wa_data_count[0] >= 1:
        webarchive_selenium_page(domain,"20230101005413")
        time.sleep(5)
        webarchive_selenium_page(domain,"20220101005413")
        time.sleep(5)
        webarchive_selenium_page(domain,"20210101005413")
        time.sleep(5)
        webarchive_selenium_page(domain,"20200606005413")
        time.sleep(1)
        append_domain_and_results_to_file_wa(DST_WA, domain,wa_data_count,data1)
    else:
        append_domain_and_results_to_file_wa(DST_NOWA, domain,wa_data_count,data1)
        time.sleep(1)
