import requests
from bs4 import BeautifulSoup
import re
import os
import shutil

def download_archive_data(domain):
    # Создаем папку для сохранения данных по домену
    domain_folder = f"{domain}"
    os.makedirs(domain_folder, exist_ok=True)

    # Формируем URL-адрес для запроса данных веб-архива
    url = f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=xml&fl=timestamp,original&collapse=urlkey"

    # Отправляем GET-запрос на получение данных
    response = requests.get(url)

    # Парсим XML-ответ
    soup = BeautifulSoup(response.content, 'lxml')
    response_text = response.text.strip()
    rows = response_text.split('\n')

    # Словарь для хранения последних версий каждого файла
    last_versions = {}

    # Скачиваем данные для каждого URL-адреса
    for row in rows:
        timestamp, original_url = row.split(' ', 1)
        clean_url = re.sub(r'[\/:*?"<>|]', '_', original_url.strip())

        # Формируем структуру папок
        date_folder = os.path.join(domain_folder, timestamp[:8])
        os.makedirs(date_folder, exist_ok=True)

        # Формируем путь для сохранения файла
        file_name = f"{clean_url}_{timestamp}.html"
        file_path = os.path.join(date_folder, file_name)

        # Формируем URL-адрес для загрузки данных
        download_url = f"https://web.archive.org/web/{timestamp}/{original_url}"

        # Отправляем GET-запрос на загрузку данных
        download_response = requests.get(download_url)

        # Сохраняем данные в файле
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(download_response.text)
            print(f"Скачан файл: {file_name}")

        # Проверяем, является ли текущая версия последней
        if clean_url not in last_versions:
            last_versions[clean_url] = file_path
        else:
            # Удаляем предыдущую версию файла
            os.remove(last_versions[clean_url])
            last_versions[clean_url] = file_path

        # Обновляем папку "last" с последними версиями файлов
        last_folder = os.path.join(domain_folder, "last")
        os.makedirs(last_folder, exist_ok=True)
        last_file_path = os.path.join(last_folder, file_name)
        shutil.copyfile(file_path, last_file_path)

    print("Загрузка завершена.")

# Пример использования
#domain = "giaydabonghana.com"
domain = "roberttell.com"
download_archive_data(domain)
