#!/bin/bash

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


INPUT_DIR=data/shd/domains-data/list/cc-2023-06/info
OUTPUT_DIR1=data/shd/domains-data/noconnect/cc-2023-06/info
OUTPUT_DIR2=data/shd/domains-data/connect/cc-2023-06/info

CHECK_FULL=False
NUM_THREADS=20
#NUM_PROCESSES=$(nproc)
NUM_PROCESSES=4

export OUTPUT_DIR1
export OUTPUT_DIR2

export CHECK_FULL
export NUM_THREADS

mkdir -p $OUTPUT_DIR1
mkdir -p $OUTPUT_DIR2


# Функция, которую будем выполнять для каждого файла
process_file() {
  file="$1"
  base=$(basename "$file")
  echo "$base"
  echo "!!!"
  SRC="$file"
  DST1="$OUTPUT_DIR1/$base.noconnect"
  DST2="$OUTPUT_DIR2/$base.connect"
echo $DST1 $CHECK_FULL $NUM_THREADS
  python3 -m check_domains_lookup "$SRC" "$DST1" "$DST2" $CHECK_FULL $NUM_THREADS
}

export -f process_file

# Если NUM_PROCESSES равно 1, выполняем скрипт через цикл
#if [ "$NUM_PROCESSES" -eq 1 ]; then
#  for file in "$INPUT_DIR"/*; do
#    process_file "$file"
#  done
#else
  # Иначе, выполняем скрипт через parallel

  find "$INPUT_DIR" -type f | parallel -j  "$NUM_PROCESSES" --eta   process_file {}
#fi
#env INPUT_DIR="$INPUT_DIR" OUTPUT_DIR1="$OUTPUT_DIR1" OUTPUT_DIR2="$OUTPUT_DIR2" CHECK_FULL="$CHECK_FULL" NUM_THREADS="$NUM_THREADS" 

exit 0