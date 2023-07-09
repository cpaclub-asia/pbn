#!/bin/bash

INPUT_DIR=data/cc-data.2/current
OUTPUT_DIR=data/cc-data/results.2

mkdir -p $OUTPUT_DIR

for file in $INPUT_DIR/*; do
  base=$(basename "$file")
  echo $base
  grep '"status": "200"' "$file" | grep '"mime": "text/html"' | ggrep -oP '(?<="url": "https://)[^/]*' > "$OUTPUT_DIR/$base"
done
