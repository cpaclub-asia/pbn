KEYWORDS=`cat all_keywords.txt`
ZONES=`cat zones_grep.txt`


echo $KEYWORDS\n
echo $ZONES\n

grep -r -E '$KEYWORDS' domains | grep -E '$ZONES' | grep "\"eng\"" > res\urls.txt


#grep -Eo '[A-Za-z0-9.-]+\.([A-Za-z]{2,}|[A-Za-z]{2}\.[A-Za-z]{2})'