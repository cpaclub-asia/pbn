SRC=$1
DST1=$2
DST2=$3

#SRC="data/domains-data/crawl/2023/info_domains.txt"
#DST1="data/domains-data/crawl/2023/info_domains_noconnect.txt"
#DST2="data/domains-data/crawl/2023/info_domains_connect.txt"

SRC=data/cc-data/domains-u/cdx-00081
DST1=$SRC.noconnect.csv
DST2=$SRC.connect.csv

python3 -m check_domains_lookup $SRC $DST1 $DST2