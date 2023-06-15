
import csv

def make_csv(files_dir,csv_path)
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['page']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Парсинг HTML-файлов и сохранение элементов в словаре
        for root, dirs, files in os.walk(files_dir):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                relative_dir = os.path.dirname(os.path.relpath(file_path,files_dir))
                file_extension = os.path.splitext(file_name)[1]
                if file_extension.lower() in ['.html', '.htm', '.asp', '.aspx', '']:
                    print(f"csv->:{file_path}")
                    with open(file_path, 'r', encoding='utf-8') as f:
                        html = f.read()
                        writer.writerow({'page': html})