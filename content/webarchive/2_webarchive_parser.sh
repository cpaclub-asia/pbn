#!/bin/bash

# Путь к файлу с доменами
file="data/webarch-data/domains.txt"

# Проверка наличия файла
if [ ! -f "$file" ]; then
    echo "Файл $file не найден."
    exit 1
fi

# Чтение каждой строки из файла и выполнение команды CMD
while IFS= read -r line; do
    # Извлечение имени домена до первого пробела или точки с запятой
    DOMAIN=$(echo "$line" | awk -F '[ ;]' '{print $1}')
    CMD="python3 webarchive_parser data/sites-data/$DOMAIN/all data/sites-data/sites/$DOMAIN"
    echo $CMD
    $CMD
done < "$file"