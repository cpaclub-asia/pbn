import os
import argparse
import csv


def parse_arguments():
    parser = argparse.ArgumentParser(description='HTML Parsing')
    parser.add_argument('input_dir', type=str, nargs='?', default=None, help='Input folder path')
    parser.add_argument('output_dir', type=str, nargs='?', default=None, help='Output folder path')
    return parser.parse_args()

def main():
    args = parse_arguments()

    if args.input_dir is None or args.output_dir is None:
        print("Необходимо указать пути к папке с HTML-файлами и папке для сохранения результатов.")
        print("Пример использования: python webarchive_csv путь_к_папке_с_HTML_файлами путь_к_папке_для_сохранения_результатов")
        return

    input_dir = args.input_dir
    output_dir = args.output_dir

    # Создаем папку для сохранения
    os.makedirs(output_dir, exist_ok=True)

    # Список файлов в папке
    files = os.listdir(input_dir)

    csv_path = os.path.join(output_dir, "all.csv")


    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['page']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Парсинг HTML-файлов и сохранение элементов в словаре
        for root, dirs, files in os.walk(input_dir):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                relative_dir = os.path.dirname(os.path.relpath(file_path,input_dir))
                if file_name.endswith('.html'):
                    print(f"csv->:{file_path}")
                    with open(file_path, 'r', encoding='utf-8') as f:
                        html = f.read()
                        writer.writerow({'page': html})
 






if __name__ == '__main__':
    main()
