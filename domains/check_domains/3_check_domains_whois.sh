SRC=$1
DST=$2

SRC="data/domains-data/crawl/2023/info_domains_noconnect.txt"
DST="data/domains-data/crawl/2023/info_domains_noconnect_whois.txt"

python3 -m check_domains_whois -f $SRC -c -i 0 -oe --csv $DST
#nohup python3 -m check_domains_whois -f $SRC -c -i 0 -oe --csv $DST &


SRC="data/domains-data/crawl/2023/info_domains_connect.txt"
DST="data/domains-data/crawl/2023/info_domains_connect_whois.txt"
python3 -m check_domains_whois -f $SRC -c -i 0 -oe --csv $DST
#nohup python3 -m check_domains_whois -f $SRC -c -i 0 -oe --csv $DST &
