SRC=data/cc-data.n/domains.test/cdx-00023.connect.whois
SRC1=$SRC.csv
DST1=$SRC.free.csv
DST2=$SRC.pending.csv

cat $SRC1 | grep "Free" > $DST1
cat $SRC1 | grep "Exp" > $DST2
cat $SRC1 | grep "Soon" >> $DST2
