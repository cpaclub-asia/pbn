SRC=$1
DST=$2

#data/cc-data.n/domains
SRC=data/cc-data.n/domains.test/cdx-00081.noconnect
SRC1=$SRC.csv
DST1=$SRC.whois.csv

python3 -m check_domains_whois -f $SRC1 -c -i 0 -oe --track-whois-text-changes --workers 30 --csv $DST1

#SRC=data/cc-data/domains-u/cdx-00081.noconnect
#SRC1=$SRC.csv
#DST1=$SRC.whois.csv

#python3 -m check_domains_whois -f $SRC1 -c -i 0 -oe --csv $DST1
