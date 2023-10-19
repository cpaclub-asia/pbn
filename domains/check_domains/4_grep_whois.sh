SRC=data/shd/domains-data/noconnect.whois/cc-2023-06/com

SRC1=$SRC/*
DST1=$SRC.all.csv
DST2=$SRC.expired.csv
DST3=$SRC.soon.csv

cat $SRC1 | grep "Free" > $DST1
cat $SRC1 | grep "Exp" > $DST2
cat $SRC1 | grep "Soon" >> $DST3
