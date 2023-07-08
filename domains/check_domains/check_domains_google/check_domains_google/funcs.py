import csv






def get_domains_from_file(file_path):
    #with open(file_path, 'r') as file:
    #    return [line.strip() for line in file]
    
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        #reader = csv.reader(file, delimiter=';')
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
    


def append_domain_and_results_to_file(file_path, domain,wa_data,data1, results, favicon, titles, snippets):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        if file.tell() == 0:
            writer.writerow(["Domain", "Results", "Favicon", "Titles", "Snippets"])  # Записываем заголовки
        row=[domain, results, favicon, titles, snippets]
        row+=(wa_data)
        row+=(data1)
        writer.writerow(row)


