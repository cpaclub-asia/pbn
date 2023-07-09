SRC=data/domains-data/crawl/2023/info_domains_noconnect_whois
SRC1=$SRC.csv
DST1=$SRC.free.csv
DST2=$SRC.pending.csv

cat $SRC1 | grep "Free" > $DST1
cat $SRC1 | grep "Pending" > $DST2
