SRC=$1
DST=$2
#SRC=data/noconnect.whois.17072023.expired_sort
#SRC=data/noconnect.whois.17072023.expired_sort2.wa

#SRC=data/sav_auction.wa
SRC=data/shd/domains-data/noconnect.whois/cc-2023-06/com.expired

#SRC="data/domains-data/crawl/2023/info_domains_noconnect_whois.free"
SRC1="$SRC.csv"
DST1="$SRC.index.csv"
DST2="$SRC.noindex.csv"

python3 -m check_domains_google $SRC1 $DST1 $DST2
