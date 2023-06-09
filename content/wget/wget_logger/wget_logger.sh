#!/bin/bash

# Оригинальный файл, из которого извлекаем информацию
original_file=$1

# Паттерн для поиска времени
time_pattern="--[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}--"

# Паттерн для поиска строки "Saving to:"
save_pattern="Saving to:"

# Паттерн для поиска URL
url_pattern="http[s]?://[^\s]+"

# Переменная для хранения временной метки
time=""

# Переменная для хранения пути сохранения
save_path=""

# Парсим оригинальный файл и получаем необходимую информацию
while IFS= read -r line
do

  # Проверяем, содержит ли строка паттерн URL
  if [[ $line =~ $url_pattern ]]; then
    # Получаем URL из строки
    #url="${BASH_REMATCH[0]}"
    #url=$(echo "$line" | grep -oP '(?<=http[s]?://)[^\s]+')
    url=$(echo "$line" | awk '{match($0, /http[s]?:\/\/[^[:space:]]+/); print substr($0, RSTART, RLENGTH)}')

    # Выводим полученную информацию в нужном формате (URL и путь сохранения)
    
  fi
  # Проверяем, содержит ли строка паттерн "Saving to:"
  if [[ $line =~ $save_pattern ]]; then
    # Извлекаем путь сохранения из строки
    save_path=$(echo "$line" | awk -F "Saving to: ‘|’" '{print $2}')
    echo "${url},${save_path}"
  fi
  
  
done < "$original_file"
