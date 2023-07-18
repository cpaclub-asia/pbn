SRC=data/domains-data/noconnect.whois/cc-2023-06/noconnect.whois.17072023
SRC1=$SRC.csv
DST1=$SRC.free.csv
DST2=$SRC.expired.csv
DST3=$SRC.soon.csv

cat $SRC1 | grep "Free" > $DST1
cat $SRC1 | grep "Exp" > $DST2
cat $SRC1 | grep "Soon" >> $DST3
