#!/bin/bash

# Путь к файлу с доменами
file="data/sites-data/domains.txt"

# Проверка наличия файла
if [ ! -f "$file" ]; then
    echo "Файл $file не найден."
    exit 1
fi

# Чтение каждой строки из файла и выполнение команды CMD
while IFS= read -r line; do
    # Извлечение имени домена до первого пробела или точки с запятой
    DOMAIN=$(echo "$line" | awk -F '[ ;]' '{print $1}')
    CMD="tar zcvf data/sites-data/$DOMAIN/clean.tar.gz all data/sites-data/$DOMAIN/clean"
    echo $CMD
    $CMD
    CMD="tar zcvf data/sites-data/$DOMAIN/assets.tar.gz all data/sites-data/$DOMAIN/assets"
    echo $CMD
    $CMD

done < "$file"
