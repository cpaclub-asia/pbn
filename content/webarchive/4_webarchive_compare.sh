#!/bin/bash

# Путь к файлу с доменами
file="data/shd/webarch-data/domains.txt"

# Проверка наличия файла
if [ ! -f "$file" ]; then
    echo "Файл $file не найден."
    exit 1
fi

# Чтение каждой строки из файла и выполнение команды CMD
while IFS= read -r line; do
    # Извлечение имени домена до первого пробела или точки с запятой
    DOMAIN=$(echo "$line" | awk -F '[ ;]' '{print $1}')
    CMD="python3 webarchive_compare data/shd/sites-data/$DOMAIN/text data/shd/sites-data/$DOMAIN/content"
    echo $CMD
    $CMD
done < "$file"
