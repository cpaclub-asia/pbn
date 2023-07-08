import os
from urllib.parse import urlparse
from shared import args_src_dst

def extract_external_domains(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            content = file.read()
    except UnicodeDecodeError:
        return set()

    # Здесь также рекомендуется использовать библиотеки для парсинга HTML,
    # так как регулярные выражения могут быть недостаточно точными
    import re
    pattern = re.compile(r'href=[\'"]?([^\'" >]+)')
    matches = pattern.findall(content)

    external_domains = set()
    for match in matches:
        parsed_url = urlparse(match)
        if parsed_url.netloc:  # Проверяем, является ли ссылка внешней
            external_domains.add(parsed_url.netloc)

    return external_domains

def find_external_domains(directory):
    external_domains = set()

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            domains = extract_external_domains(file_path)
            external_domains.update(domains)

    return external_domains



directory_path = 'links'
domains = find_external_domains(directory_path)

for domain in domains:
    print(domain)