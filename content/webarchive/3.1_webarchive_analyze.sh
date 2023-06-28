#!/bin/bash

check_files() {
    directory=$1
    words=("${@:2:$#-2}")
    log_file=${@:$#}

    for file in "$directory"/*; do
        if [ -f "$file" ]; then
            content=$(cat "$file")
            for word in ${words[@]}; do
                if [[ $content == *"$word"* ]]; then
										lang_check=$(grep -iE 'lang="en-EN"|lang="ru-RU"' "$file")
                    if [[ ! -z "$lang_check" ]]; then
											status="Explicit"
											folder=$(echo "$file" | cut -d '/' -f 7)
											trimmed_file=$(echo "$file" | cut -d '/' -f 8-)
											if [[ "$folder" != "all" ]]; then
												echo "Folder: $folder | File: $trimmed_file | Status: $status"
												echo "Folder: $folder | File: $trimmed_file | Status: $status" >> "$log_file"
											fi
										fi
                    break
                fi
            done
        elif [ -d "$file" ]; then
            check_files "$file" "${words[@]}" "$log_file"
        fi
    done
}

# Choose directory that you need to check
directory="./data/webarch-data/"

# List of words for check
words=("porn" "casino" "betting")

# Choose the log file
log_file="./webarchive_analyze/log.txt"

check_files "$directory" "${words[@]}" "$log_file"
echo "---------------------------------------------------------" >> "$log_file"