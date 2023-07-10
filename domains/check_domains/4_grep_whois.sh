SRC=data/cc-data.n/domains.test/cdx-00081.noconnect.whois
SRC1=$SRC.csv
DST1=$SRC.free.csv
DST2=$SRC.pending.csv

cat $SRC1 | grep "Free" > $DST1
cat $SRC1 | grep "Pending" > $DST2
