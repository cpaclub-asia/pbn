import os
import argparse
import make_csv from file_csv

def parse_arguments():
    parser = argparse.ArgumentParser(description='HTML Parsing')
    parser.add_argument('input_dir', type=str, nargs='?', default=None, help='Input folder path')
    #parser.add_argument('output_dir', type=str, nargs='?', default=None, help='Output folder path')
    return parser.parse_args()

def main():
    args = parse_arguments()

    if args.input_dir is None:
        print("Необходимо указать пути к папке с HTML-файлами и папке для сохранения результатов.")
        print("Пример использования: python webarchive_csv путь_к_папке_с_HTML_файлами")
        return

    pages_dir = args.input_dir+"/content/pages/"
    posts_dir = args.input_dir+"/content/posts/"
    output_dir = args.input_dir+"/content/csv/"

    # Создаем папку для сохранения
    os.makedirs(output_dir, exist_ok=True)

    # Список файлов в папке
    files = os.listdir(input_dir)

    pages_csv_path = os.path.join(output_dir, "pages.csv")
    posts_csv_path = os.path.join(output_dir, "posts.csv")

    make_csv(pages_dir,pages_csv_path)
    make_csv(posts_dir,posts_csv_path)




if __name__ == '__main__':
    main()
