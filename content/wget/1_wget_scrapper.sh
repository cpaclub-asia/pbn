#!/bin/bash

# Путь к файлу с доменами
file="data/wget-data/domains.txt"
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
    #CMD="./wget_scrapper/wget_scrapper.sh data/wget-data/ $DOMAIN"
    #echo $CMD
    #$CMD
    
    CMD="./wget_logger/wget_logger.sh data/wget-data/$DOMAIN/wget.log "
    echo $CMD
    $CMD > data/wget-data/$DOMAIN/urls.txt

done < "$file"
