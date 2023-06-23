#!/bin/bash

# Функция для копирования содержимого папки
copy_directory() {
    source_dir="$1"
    destination_dir="$2"

    # Создаем папку назначения, если она не существует
    mkdir -p "$destination_dir"

    # Копируем содержимое папки из источника в назначение
    cp -R "$source_dir"/* "$destination_dir"
}

# Проверяем количество переданных аргументов
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 pathin pathout"
    exit 1
fi

# Получаем переданные пути
pathin="$1"
pathout="$2"

# Проверяем, существует ли путь pathin
if [ ! -d "$pathin" ]; then
    echo "Error: $pathin is not a directory."
    exit 1
fi

# Проверяем, существует ли путь pathout
if [ ! -d "$pathout" ]; then
    echo "Error: $pathout is not a directory."
    exit 1
fi

# Получаем список папок внутри pathin
folders=$(find "$pathin" -mindepth 1 -maxdepth 1 -type d)

# Копируем каждую папку из pathin в pathout
for folder in $folders; do
    folder_name=$(basename "$folder")
    destination="$pathout/$folder_name"
    copy_directory "$folder" "$destination"
done

echo "Folders copied successfully."