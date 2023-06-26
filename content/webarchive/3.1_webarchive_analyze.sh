#!/bin/bash

check_files() {
    directory=$1
    words=$2
    log_file=$3

    for file in "$directory"/*; do
        if [ -f "$file" ]; then
            content=$(cat "$file")
            for word in ${words[@]}; do
                if [[ $content == *"$word"* ]]; then
                    status="Слова найдены"
                    echo "Файл: $file | Статус: $status"
                    echo "Файл: $file | Статус: $status" >> "$log_file"
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
log_directory="./webarchive_analyze/"
log_file="$log_directory/log.txt"

check_files "$directory" "${words[@]}" "$log_file"

