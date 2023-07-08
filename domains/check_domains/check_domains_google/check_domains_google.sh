SRC=$1
DST=$2

SRC="data/domains-data/crawl/2023/info_domains_noconnect_whois.csv"
DST1="data/domains-data/crawl/2023/info_domains_noconnect_whois_index.csv"
DST2="data/domains-data/crawl/2023/info_domains_noconnect_whois_noindex.csv"


python3 -m check_domains_google $SRC $DST1 $DST2
