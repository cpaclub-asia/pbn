#!/bin/bash

# Путь к файлу с доменами
file="data/nginx-data/domains.txt"
#file=$1


# Проверка наличия файла
if [ ! -f "$file" ]; then
    echo "Файл $file не найден."
    exit 1
fi

echo "Prepare"

/bin/mkdir data/nginx-data
/bin/mkdir data/nginx-data/static
/bin/mkdir data/nginx-data/wordpress
echo "" > data/nginx-data/include.conf

# Чтение каждой строки из файла и выполнение команды CMD
while IFS= read -r line; do
    # Извлечение имени домена до первого пробела или точки с запятой
    DOMAIN=$(echo "$line" | awk -F '[ ;]' '{print $1}')
    echo "$DOMAIN"
    
    sed "s/{{DOMAIN}}/$DOMAIN/g" "templates/plain_static.conf" > data/nginx-data/static/$DOMAIN.conf
    sed "s/{{DOMAIN}}/$DOMAIN/g" "templates/wordpress_static.conf" > data/nginx-data/wordpress/$DOMAIN.conf
    echo "include $DOMAIN.conf;" >> data/nginx-data/include.conf
done < "$file"


