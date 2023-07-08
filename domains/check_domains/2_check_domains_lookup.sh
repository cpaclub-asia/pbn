SRC=$1
DST1=$2
DST2=$3

#SRC="data/domains-data/crawl/2023/info_domains.txt"
#DST1="data/domains-data/crawl/2023/info_domains_noconnect.txt"
#DST2="data/domains-data/crawl/2023/info_domains_connect.txt"

SRC="data/domains-data/crawl/2015/commoncrawl_domains_2015.csv"
DST1="data/domains-data/crawl/2015/commoncrawl_domains_2015_noconnect.csv"
DST2="data/domains-data/crawl/2015/commoncrawl_domains_2015_connect.csv"

python3 -m check_domains_lookup $SRC $DST1 $DST2