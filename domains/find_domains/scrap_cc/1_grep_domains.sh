#!/bin/bash

#for macos replace grep to ggrep (-oP)

##23-14
##23-23
##22-27
##22-05
##21-25
##21-04
##20-29

INDEX=2023-14

INPUT_DIR=data/hdd/cc-data.gz/CC-MAIN-$INDEX
OUTPUT_DIR=data/shd/predomains2/CC-MAIN-$INDEX

mkdir -p $OUTPUT_DIR

for file in $INPUT_DIR/*; do
  base=$(basename "$file")
  base1=$(basename "$file" .gz)
  echo $base
  #grep '"status": "200"' "$file" | grep '"mime": "text/html"' | grep -oP '(?<="url": "https:\/\/)[^"/?&#\\]*' > "$OUTPUT_DIR/$base"
  zcat "$file" | grep '"status": "200"'| grep '"mime": "text/html"' | grep -oP '(?<="url": "https:\/\/)[^"/?&#\\]*' > "$OUTPUT_DIR/$base1"
done
