#!/bin/bash

# Путь к файлу с доменами
file="data/webarch-data/domains.txt"
#file=$1


# Проверка наличия файла
if [ ! -f "$file" ]; then
    echo "Файл $file не найден."
    exit 1
fi

# Чтение каждой строки из файла и выполнение команды CMD
while IFS= read -r line; do
    # Извлечение имени домена до первого пробела или точки с запятой
    DOMAIN=$(echo "$line" | awk -F '[ ;]' '{print $1}')
    CMD="python3 -m webarchive_scrapper -f data/webarch-data $DOMAIN"
    echo $CMD
    nohup $CMD &
done < "$file"
