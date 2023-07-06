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

    /bin/mkdir -p data/sites-data/$DOMAIN/upload
    cp -r ./data/sites-data/$DOMAIN/cleaned/all/ ./data/sites-data/$DOMAIN/upload/
    cp -r ./data/sites-data/$DOMAIN/assets/all/ ./data/sites-data/$DOMAIN/upload/
    
    CMD="tar zcvf data/sites-data/upload_$DOMAIN.tar.gz data/sites-data/$DOMAIN/upload/*"
    echo $CMD
    $CMD
done < "$file"
