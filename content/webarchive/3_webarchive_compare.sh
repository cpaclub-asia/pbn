#!/bin/bash

# Путь к файлу с доменами
file="domains.txt.1"

# Проверка наличия файла
if [ ! -f "$file" ]; then
    echo "Файл $file не найден."
    exit 1
fi

# Чтение каждой строки из файла и выполнение команды CMD
while IFS= read -r line; do
    # Извлечение имени домена до первого пробела или точки с запятой
    DOMAIN=$(echo "$line" | awk -F '[ ;]' '{print $1}')
    CMD="python3 webarchive_compare webarchive.parsed/$DOMAIN/text webarchive.parsed/$DOMAIN/content"
    echo $CMD
    $CMD
done < "$file"
