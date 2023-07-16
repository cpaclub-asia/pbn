
#data/cc-data.n/domains
INPUT_DIR=data/domains-data/noconnect/cc-2023-06/com
OUTPUT_DIR=data/domains-data/noconnect.whois/cc-2023-06/com
WORKERS=5

mkdir -p $OUTPUT_DIR


process_file() {
  file="$1"
  base=$(basename "$file")
  echo "$base"

  SRC1="$file"
  DST1="$OUTPUT_DIR/$base.whois"
  
  python3 -m check_domains_whois -f $SRC1 -c -i 0 -oe --track-whois-text-changes --workers 5 --csv $DST1

}

  for file in "$INPUT_DIR"/*; do
    process_file "$file"
  done
