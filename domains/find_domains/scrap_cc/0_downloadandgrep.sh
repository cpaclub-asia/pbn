#!/bin/bash

#for macos replace grep to ggrep (-oP)

##23-14
##23-23
##22-27
##22-05
##21-25
##21-04
##20-29

INDEX=2023-06
INDEX_FOR=2023-14

INPUT_DIR=data/hdd/cc-predomains/CC-MAIN-$INDEX_FOR
OUTPUT_DIR=data/shd/predomains3/CC-MAIN-$INDEX

mkdir -p $OUTPUT_DIR

for file in $INPUT_DIR/*; do
  base=$(basename "$file")
  base1=$(basename "$file" .gz)
  url="https://data.commoncrawl.org/cc-index/collections/$INDEX/indexes/$base"
  echo $base
  echo $url
  #grep '"status": "200"' "$file" | grep '"mime": "text/html"' | grep -oP '(?<="url": "https:\/\/)[^"/?&#\\]*' > "$OUTPUT_DIR/$base"
  curl $url | zcat "$file" | grep '"status": "200"'| grep '"mime": "text/html"' | grep -oP '(?<="url": "https:\/\/)[^"/?&#\\]*' > "$OUTPUT_DIR/$base1"
done
