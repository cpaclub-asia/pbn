import os
import argparse
from file_csv import make_csv 

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

    input_dir=args.input_dir
    pages_dir = input_dir+"/content/pages/"
    posts_dir = input_dir+"/content/posts/"
    output_dir = input_dir+"/content/csv/"
    title_path = input_dir+"/title/"

    # Создаем папку для сохранения
    os.makedirs(output_dir, exist_ok=True)

    # Список файлов в папке
    files = os.listdir(input_dir)

    pages_csv_path = os.path.join(output_dir, "pages.csv")
    posts_csv_path = os.path.join(output_dir, "posts.csv")

    print("MAKING PAGES")
    make_csv(pages_dir,title_path,pages_csv_path)
    print("MAKING POSTS")
    make_csv(posts_dir,title_path,posts_csv_path)




if __name__ == '__main__':
    main()
