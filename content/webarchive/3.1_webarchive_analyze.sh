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
                    status="Слова найдены"
                    folder=$(echo "$file" | cut -d '/' -f 7)
										trimmed_file=$(echo "$file" | cut -d '/' -f 8-)
										if [[ "$folder" != "all" ]]; then
											echo "Папка: $folder | Файл: $trimmed_file | Статус: $status"
                    	echo "Папка: $folder | Файл: $trimmed_file | Статус: $status" >> "$log_file"
										fi
                    break
                fi
            done
        elif [ -d "$file" ]; then
            check_files "$file" "${words[@]}" "$log_file"
        fi
    done
}

# Задайте директорию, которую нужно проверить
directory="./data/webarch-data/"

# Задайте список слов для поиска
words=("porn" "casino" "betting")

# Задайте путь к папке для сохранения файла журнала
log_file="./webarchive_analyze//log.txt"

check_files "$directory" "${words[@]}" "$log_file"
