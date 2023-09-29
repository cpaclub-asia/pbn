#!/bin/bash

INPUT_DIR=data/hdd/cc-predomains
INPUT_DIR2=data/hdd/cc-predomains/CC-MAIN-2020-29

OUTPUT_DIR=data/shd/domains-data/list/all7


mkdir -p $OUTPUT_DIR

for file in $INPUT_DIR2/*; do
  base=$(basename "$file")
  echo $file
  echo $base
  BASE1=$(basename "$file" .gz)

  LIST="$INPUT_DIR/CC-MAIN-2020-29/$base $INPUT_DIR/CC-MAIN-2021-04/$base $INPUT_DIR/CC-MAIN-2021-25/$base $INPUT_DIR/CC-MAIN-2022-05/$base $INPUT_DIR/CC-MAIN-2022-27/$base $INPUT_DIR/CC-MAIN-2023-14/$base $INPUT_DIR/CC-MAIN-2023-23/$base"
  echo $LIST
  #cat  "$file" | tr '[:upper:]' '[:lower:]' | awk -F. '{print $(NF-1)"."$NF}' | sort |  uniq -c | awk '{print $2";"$1}' > "$OUTPUT_DIR/$base"
  cat $LIST | tr '[:upper:]' '[:lower:]' | awk -F. '{print $(NF-1)"."$NF}' | sort |  uniq -c | awk '{print $2";"$1}' > "$OUTPUT_DIR/$BASE1"
done
