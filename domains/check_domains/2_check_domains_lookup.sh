#SRC=$1
#DST1=$2
#DST2=$3

#SRC="data/domains-data/crawl/2023/info_domains.txt"
#DST1="data/domains-data/crawl/2023/info_domains_noconnect.txt"
#DST2="data/domains-data/crawl/2023/info_domains_connect.txt"

#SRC=data/domains-data/cc-2023-06-domains.com.csv
#DST1=$SRC.noconnect.csv
#DST2=$SRC.connect.csv

#python3 -m check_domains_lookup $SRC $DST1 $DST2


INPUT_DIR=data/cc-data.n/domains.com
OUTPUT_DIR1=data/cc-data.n/domains.com.noconnect
OUTPUT_DIR2=data/cc-data.n/domains.com.connect

mkdir -p $OUTPUT_DIR1
mkdir -p $OUTPUT_DIR2

for file in $INPUT_DIR/*; do
  base=$(basename "$file")
  echo $base
  
  SRC=$file
  DST1=$OUTPUT_DIR1/$base.noconnect
  DST2=$OUTPUT_DIR2/$base.connect

  python3 -m check_domains_lookup $SRC $DST1 $DST2
done