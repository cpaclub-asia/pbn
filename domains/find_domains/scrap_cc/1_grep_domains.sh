#!/bin/bash

#for macos replace grep to ggrep (-oP)

INPUT_DIR=data/cc-data/current
OUTPUT_DIR=data/cc-data/predomains.new

mkdir -p $OUTPUT_DIR

for file in $INPUT_DIR/*; do
  base=$(basename "$file")
  echo $base
  grep '"status": "200"' "$file" | grep '"mime": "text/html"' | grep -oP '(?<="url": "https:\/\/)[^"/?&#\\]*' > "$OUTPUT_DIR/$base"
done
