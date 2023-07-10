#!/bin/bash

INPUT_DIR=data/cc-data.r/current
OUTPUT_DIR=data/cc-data.n/predomains.r

mkdir -p $OUTPUT_DIR

for file in $INPUT_DIR/*; do
  base=$(basename "$file")
  echo $base
  grep '"status": "200"' "$file" | grep '"mime": "text/html"' | ggrep -oP '(?<="url": "https://)[^/]*' > "$OUTPUT_DIR/$base"
done
