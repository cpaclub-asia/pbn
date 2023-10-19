#!/bin/bash

# Путь к файлу с доменами
file="data/shd/sites-data/domains.txt"

# Проверка наличия файла
if [ ! -f "$file" ]; then
    echo "Файл $file не найден."
    exit 1
fi

# Чтение каждой строки из файла и выполнение команды CMD
while IFS= read -r line; do
    # Извлечение имени домена до первого пробела или точки с запятой
    DOMAIN=$(echo "$line" | awk -F '[ ;]' '{print $1}')
    CMD="python3 -m webarchive_remove data/shd/sites-data/$DOMAIN/webarch data/shd/sites-data/$DOMAIN/cleaned  data/shd/sites-data/$DOMAIN/assets"
    echo $CMD
    #$CMD
    nohup $CMD > /dev/null &
done < "$file"