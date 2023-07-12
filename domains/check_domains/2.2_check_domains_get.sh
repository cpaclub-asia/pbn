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



INPUT_DIR=data/cc-data.n/domains.com.connect
OUTPUT_DIR1=data/cc-data.n/domains.com.noget
OUTPUT_DIR2=data/cc-data.n/domains.com.get
CHECK_FULL=True
NUM_THREADS=10
#NUM_PROCESSES=$(nproc)
NUM_PROCESSES=1



mkdir -p $OUTPUT_DIR1
mkdir -p $OUTPUT_DIR2


# Функция, которую будем выполнять для каждого файла
process_file() {
  file="$1"
  base=$(basename "$file")
  echo "$base"

  SRC="$file"
  DST1="$OUTPUT_DIR1/$base.noget"
  DST2="$OUTPUT_DIR2/$base.get"
echo $DST1 $CHECK_FULL $NUM_THREADS
  python3 -m check_domains_lookup "$SRC" "$DST1" "$DST2" $CHECK_FULL $NUM_THREADS
}

# Если NUM_PROCESSES равно 1, выполняем скрипт через цикл
if [ "$NUM_PROCESSES" -eq 1 ]; then
  for file in "$INPUT_DIR"/*; do
    process_file "$file"
  done
else
  # Иначе, выполняем скрипт через parallel
  export -f process_file
  find "$INPUT_DIR" -type f | parallel -j -X "$NUM_PROCESSES" --eta process_file
fi

exit 0