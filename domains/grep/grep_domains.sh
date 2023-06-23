#LIST=pbn-data/commoncrawl_domains_2015_whois_checked.txt
LIST=pbn-data/info_domains_nc_whois.txt


KEYWORDS=`cat all_keywords.txt`
ZONES=`cat zones_grep.txt`


echo $KEYWORDS\n
echo $ZONES\n

#cat $LIST | grep -r -E '$KEYWORDS' domains | grep -E '$ZONES' | grep "\"eng\"" > res\urls.txt

cat $LIST | grep -E "$ZONES" | grep "Free" > $LIST.free
cat $LIST | grep -E "$ZONES" | grep "Exp" | grep "( -" > $LIST.pending

#grep -Eo '[A-Za-z0-9.-]+\.([A-Za-z]{2,}|[A-Za-z]{2}\.[A-Za-z]{2})'