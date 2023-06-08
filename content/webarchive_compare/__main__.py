import os
import argparse
from bs4 import BeautifulSoup

def parse_arguments():
    parser = argparse.ArgumentParser(description='HTML Parsing')
    parser.add_argument('input_folder', type=str, nargs='?', default=None, help='Input folder path')
    parser.add_argument('output_folder', type=str, nargs='?', default=None, help='Output folder path')
    return parser.parse_args()

def main():
    args = parse_arguments()

    if args.input_folder is None or args.output_folder is None:
        print("Необходимо указать пути к папке с HTML-файлами и папке для сохранения результатов.")
        print("Пример использования: python html_parser.py путь_к_папке_с_HTML_файлами путь_к_папке_для_сохранения_результатов")
        return

    input_folder = args.input_folder
    output_folder = args.output_folder

    # Создаем папку для сохранения уникальных результатов
    os.makedirs(output_folder, exist_ok=True)

    # Список файлов в папке
    files = os.listdir(input_folder)

    # Словарь для хранения элементов каждого файла и их количества
    elements_dict = {}

    # Парсинг HTML-файлов и сохранение элементов в словаре
    for file in files:
        file_path = os.path.join(input_folder, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()
            soup = BeautifulSoup(html, 'html.parser')
            elements = soup.find_all()
            for element in elements:
                element_str = str(element)
                if element_str in elements_dict:
                    elements_dict[element_str] += 1
                else:
                    elements_dict[element_str] = 1

    # Находим общие элементы (встретившиеся хотя бы 3 раза)
    common_elements = set(element for element, count in elements_dict.items() if count >= 3)

    # Создаем папку для сохранения общих элементов
    common_elements_folder = os.path.join(output_folder, 'common_elements')
    os.makedirs(common_elements_folder, exist_ok=True)

    # Сохраняем общие элементы в отдельном файле
    common_elements_file_path = os.path.join(common_elements_folder, 'common_elements.html')
    with open(common_elements_file_path, 'w', encoding='utf-8') as f:
        for element in common_elements:
            f.write(element)
            f.write('\n')

    # Находим уникальные элементы для каждого файла
    unique_elements_dict = {}
    for file in files:
        file_path = os.path.join(input_folder, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()
            soup = BeautifulSoup(html, 'html.parser')
            elements = soup.find_all()
            unique_elements = set(str(element) for element in elements if str(element) not in common_elements)
            unique_elements_dict[file] = unique_elements

    # Создаем папку для сохранения уникальных элементов
    unique_elements_folder = os.path.join(output_folder, 'unique_elements')
    os.makedirs(unique_elements_folder, exist_ok=True)

    # Сохраняем уникальные элементы для каждой страницы в отдельном файле
    for file, elements in unique_elements_dict.items():
        unique_elements_file_path = os.path.join(unique_elements_folder, f'{file}_unique_elements.html')
        with open(unique_elements_file_path, 'w', encoding='utf-8') as f:
            for element in elements:
                f.write(element)
                f.write('\n')

if __name__ == '__main__':
    main()
