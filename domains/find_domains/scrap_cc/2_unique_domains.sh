#!/bin/bash

INPUT_DIR=data/cc-data/predomains.new
OUTPUT_DIR=data/domains-data/list/cc-2023-06/new2


mkdir -p $OUTPUT_DIR

for file in $INPUT_DIR/*; do
  base=$(basename "$file")
  echo $base
  cat  "$file" | tr '[:upper:]' '[:lower:]' | awk -F. '{print $(NF-1)"."$NF}' | sort |  uniq -c | awk '{print $2";"$1}' > "$OUTPUT_DIR/$base"
done
