import os
import argparse
from bs4 import BeautifulSoup

def parse_arguments():
    parser = argparse.ArgumentParser(description='HTML Parsing')
    parser.add_argument('input_dir', type=str, nargs='?', default=None, help='Input folder path')
    parser.add_argument('output_dir', type=str, nargs='?', default=None, help='Output folder path')
    return parser.parse_args()

def main():
    args = parse_arguments()

    if args.input_dir is None or args.output_dir is None:
        print("Необходимо указать пути к папке с HTML-файлами и папке для сохранения результатов.")
        print("Пример использования: python html_parser.py путь_к_папке_с_HTML_файлами путь_к_папке_для_сохранения_результатов")
        return

    input_dir = args.input_dir
    output_dir = args.output_dir

    # Создаем папку для сохранения уникальных результатов
    os.makedirs(output_dir, exist_ok=True)

    # Список файлов в папке
    files = os.listdir(input_dir)

    # Словарь для хранения элементов каждого файла и их количества
    elements_dict = {}
    elements_dict_ns = {}
    # Парсинг HTML-файлов и сохранение элементов в словаре
    for root, dirs, files in os.walk(input_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            relative_dir = os.path.dirname(os.path.relpath(file_path,input_dir))
            file_extension = os.path.splitext(file_name)[1]
            if file_extension.lower() in ['.html', '.htm', '.asp', '.aspx', '']:
                print(f"common:{file_path}")
                with open(file_path, 'r', encoding='utf-8') as f:
                    html = f.read()
                    soup = BeautifulSoup(html, 'html.parser')
                    elements = soup.find_all()
                    for element in elements:
                        element_str = str(element)
                        element_str_ns = element_str.replace(" ", "")

                        if element_str_ns in elements_dict_ns:
                            elements_dict_ns[element_str_ns] += 1
                        else:
                            elements_dict_ns[element_str_ns] = 1
                            elements_dict[element_str_ns] = element_str

    # Находим общие элементы (встретившиеся хотя бы 3 раза)
    common_elements = set(element for element, count in elements_dict_ns.items() if count >= 3)
    #print(123)
    #print(elements_dict)
    #print(elements_dict_ns)
    print(common_elements)

    # Создаем папку для сохранения общих элементов
    common_elements_folder = os.path.join(output_dir, 'common')
    os.makedirs(common_elements_folder, exist_ok=True)

    # Сохраняем общие элементы в отдельном файле
    common_elements_file_path = os.path.join(common_elements_folder, 'common_elements.html')
    with open(common_elements_file_path, 'w', encoding='utf-8') as f:
        for element in common_elements:
            f.write(elements_dict[element])
            f.write('\n')


    # Создаем папку для сохранения уникальных элементов
    unique_elements_folder = os.path.join(output_dir, 'unique')
    os.makedirs(unique_elements_folder, exist_ok=True)


    for root, dirs, files in os.walk(input_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            relative_dir = os.path.dirname(os.path.relpath(file_path,input_dir))
            file_extension = os.path.splitext(file_name)[1]
            if file_extension.lower() in ['.html', '.htm', '.asp', '.aspx', '']:
                print(f"unique:{file_path} -> {unique_elements_folder}")
                unique_elements_dict = {}
                

                output_subdir = os.path.join(output_dir, 'unique',relative_dir)
                os.makedirs(output_subdir, exist_ok=True)

                unique_elements_file_path = os.path.join(output_subdir, file_name)

                with open(unique_elements_file_path, 'w', encoding='utf-8') as f2:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        html = f.read()
                        soup = BeautifulSoup(html, 'html.parser')
                        elements = soup.find_all()

                        for element in elements:
                            element_str = str(element)
                            element_str_ns = element_str.replace(" ", "")

                            if element_str_ns not in common_elements:
                                f2.write(elements_dict[element_str_ns])
                                f2.write('\n')




if __name__ == '__main__':
    main()
