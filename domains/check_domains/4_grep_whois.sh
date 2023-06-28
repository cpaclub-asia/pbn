LIST=data/domains-data/commoncrawl_domains_2015_whois_checked.txt
#LIST=pbn-data/info0_whois.txt

ZONES=`cat grep/zones_grep.txt`

echo $ZONES\n


cat $LIST | grep -E "$ZONES" | grep "Free" > $LIST.free
cat $LIST | grep -E "$ZONES" | grep "Exp" | grep "( -" > $LIST.expired