#!/bin/bash

# Запрашиваем у пользователя путь к целевому каталогу
read -p "Введите путь к целевому каталогу (относительно ./data/webarch-data/web.archive.org/): " relative_path

# Получаем абсолютный путь к целевому каталогу, используя относительную ссылку
target_directory="$(realpath "./data/webarch-data/web.archive.org/$relative_path")"

# Укажите путь к папке, в которую будут собраны все файлы и папки
destination_directory="$(realpath "./data/webarch-data/web.archive.org/$relative_path/all")"
find "$destination_directory" -mindepth 1 -delete

# Используем команду find для поиска всех файлов и папок в целевом каталоге
# и его подпапках, а затем копируем их в папку назначения
find "$target_directory" -mindepth 2 -type f -exec cp {} "$destination_directory" \;
find "$target_directory" -mindepth 2 -type d -exec cp -R {} "$destination_directory" \;

