#!/bin/bash

# Путь к файлу с доменами
file="data/nginx-data/domains.txt"
#file=$1

USER=google2

# Проверка наличия файла
if [ ! -f "$file" ]; then
    echo "Файл $file не найден."
    exit 1
fi

echo "Prepare"

/bin/mkdir data/nginx-data

rm -r data/nginx-data/plain
rm -r data/nginx-data/wordpress
rm -r data/nginx-data/main

/bin/mkdir data/nginx-data/plain
/bin/mkdir data/nginx-data/wordpress
/bin/mkdir data/nginx-data/main


echo "" > data/nginx-data/main/includes_plain.conf
echo "" > data/nginx-data/main/includes_wordpress.conf

# Чтение каждой строки из файла и выполнение команды CMD
while IFS= read -r line; do
    # Извлечение имени домена до первого пробела или точки с запятой
    DOMAIN=$(echo "$line" | awk -F '[ ;]' '{print $1}')
    echo "$DOMAIN"
    
    sed "s/{{DOMAIN}}/$DOMAIN/g" "templates/plain_static.conf" |  sed "s/{{USER}}/$USER/g" > data/nginx-data/plain/$DOMAIN.conf
    sed "s/{{DOMAIN}}/$DOMAIN/g" "templates/wordpress_static.conf" | sed "s/{{USER}}/$USER/g" > data/nginx-data/wordpress/$DOMAIN.conf

    echo "include /home/$USER/conf/plain/$DOMAIN.conf;" >> data/nginx-data/main/includes_plain.conf
    echo "include /home/$USER/conf/wordpress/$DOMAIN.conf;" >> data/nginx-data/main/includes_wordpress.conf
done < "$file"


