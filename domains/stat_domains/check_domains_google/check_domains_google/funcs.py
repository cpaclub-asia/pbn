import requests
import time

import csv
import base64





def get_domains_from_file(file_path):
    #with open(file_path, 'r') as file:
    #    return [line.strip() for line in file]
    
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Считываем заголовки столбцов

        if 'Domain' in headers:
            domain_index = headers.index('Domain')
        else:
            domain_index = 0  # Если столбец "Domain" не найден, читаем из первого столбца

        data = {}
        domains = []
        for row in reader:
            if domain_index < len(row):
                domain = row[domain_index]
                domains.append(domain)
                data[domain]=row

    return domains,data
    


def append_domain_and_results_to_file(file_path, domain,data1, results, favicon, titles, snippets):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["Domain", "Results", "Favicon", "Titles", "Snippets"])  # Записываем заголовки
        row=[domain, results, favicon, titles, snippets]
        row.append(data1)
        writer.writerow(row)


def save_favicon(favicon_url, domain):
    if favicon_url.startswith("data:image/png;base64,"):
        # Remove the "data:image/png;base64," prefix
        favicon_base64 = favicon_url[len("data:image/png;base64,"):]

        # Decode the base64 image data
        favicon_data = base64.b64decode(favicon_base64)

        # Generate the file name
        file_name = f"{domain}.png"

        # Save the favicon image as a file
        with open(file_name, "wb") as file:
            file.write(favicon_data)

        return file_name
    else:
        return None