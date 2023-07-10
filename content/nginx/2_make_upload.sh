#!/bin/bash

# Путь к файлу с доменами
file="data/sites-data/domains.txt"

# Проверка наличия файла
if [ ! -f "$file" ]; then
    echo "Файл $file не найден."
    exit 1
fi

echo Remove
    rm -R data/upload-data/upload
# Чтение каждой строки из файла и выполнение команды CMD
while IFS= read -r line; do
    # Извлечение имени домена до первого пробела или точки с запятой
    DOMAIN=$(echo "$line" | awk -F '[ ;]' '{print $1}')
    echo $DOMAIN
    
    /bin/mkdir -p data/upload-data/upload/$DOMAIN
    cp -r ./data/sites-data/$DOMAIN/cleaned/all/ ./data/upload-data/upload/$DOMAIN
    cp -r ./data/sites-data/$DOMAIN/assets/all/ ./data/upload-data/upload/$DOMAIN
    
done < "$file"

    CMD="tar zcvf data/upload-data/upload.tar.gz data/upload-data/upload/*"
    echo $CMD
    $CMD
