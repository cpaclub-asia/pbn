#LIST=data/cc-data/last
LIST=data/cc-data/test
RES=data/cc-data/links.txt


#KEYWORDS=`cat all_keywords.txt`
ZONES=`cat zones_grep.txt`
ZONESLIST=`cat zones_list.txt`


#echo $KEYWORDS\n
echo $ZONES
echo $ZONESLIST

#find $LIST -type f -exec grep 'паттерн' {} +

grep -rhE '^(com|org|net|info|ru|pro|shop|xyz|life|live|today|online)\,' $LIST | grep '"status": "200"' | grep '"mime": "text/html"' | grep -oP '(?<="url": "https://)[^/]*'

# sed -e 's/"url": "https:\/\///' -e 's/"languages": "//' | awk -v ORS=';' 'NR%2{print;next}{print "\n"$0}'
#  >  $RES
#
#| grep "\"eng\""
#cat $LIST | grep -E "$ZONES" | grep "Free" > $LIST.free
#cat $LIST | grep -E "$ZONES" | grep "Exp" | grep "( -" > $LIST.pending
#grep -Eo '[A-Za-z0-9.-]+\.([A-Za-z]{2,}|[A-Za-z]{2}\.[A-Za-z]{2})'