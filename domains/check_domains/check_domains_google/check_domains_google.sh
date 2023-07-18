SRC=$1
DST=$2
SRC=data/noconnect.whois.17072023.expired_sort

#SRC="data/domains-data/crawl/2023/info_domains_noconnect_whois.free"
SRC1="$SRC.csv"
DST1="$SRC.index.csv"
DST2="$SRC.noindex.csv"
DST3="$SRC.nowa.csv"

python3 -m check_domains_google $SRC1 $DST1 $DST2 $DST3
