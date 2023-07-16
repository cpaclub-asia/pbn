#LIST=data/cc-data/last

LIST=data/cc-data/last/*
RES=data/cc-data/links_com.txt


#KEYWORDS=`cat all_keywords.txt`
ZONES=`cat zones_grep.txt`
ZONESLIST=`cat zones_list.txt`


#echo $KEYWORDS\n
echo $ZONES
echo $ZONESLIST

#find $LIST -type f -exec grep 'паттерн' {} +

grep -rhE '^(com|org|net|info|ru|pro|shop|xyz|life|live|today|online)\,' $LIST | grep '"status": "200"' | grep '"mime": "text/html"' | ggrep -oP '(?<="url": "https://)[^/]*' > $RES