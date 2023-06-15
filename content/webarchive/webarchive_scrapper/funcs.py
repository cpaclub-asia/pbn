import os
from urllib.parse import urlparse, urlunparse

def is_root_path(original_url):
    parsed_url = urlparse(original_url)
    path = parsed_url.path
    port = parsed_url.port
    return (path == '/' or path == '') and (not port or port == 80)
    
def add_trailing_slash(url):

    parsed_url = os.path.splitext(url)  # Разбиваем URL на путь и расширение
    path = parsed_url[0]  # Получаем путь из разбитого URL

    if not path.endswith('/') and not parsed_url[1]:  # Проверяем условия
        url += '/'  # Добавляем слеш в конец URL

    return url

'''    
def add_index_html(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    if url=="":
        return "index.html"
    #if not ends with / but have no extension:
    #    path += '/index.html'
    #    return path

    if path.endswith('/'):
        path += 'index.html'
        return path
        #return urlunparse(parsed_url._replace(path=path))

    return url
'''

def add_index_html(url):
    from urllib.parse import urlparse
    import os

    parsed_url = urlparse(url)
    path = parsed_url.path

    if url == "":
        return "index.html"

    if path.endswith('/'):
        path += 'index.html'
    elif os.path.splitext(path)[1] == '':
        path += '/index.html'
    return path

'''
print(add_index_html(""))  # ожидаемый результат: "index.html"
print(add_index_html("path"))  # ожидаемый результат: "path/index.html"
print(add_index_html("path/"))  # ожидаемый результат: "path/index.html"
print(add_index_html("path/file"))  # ожидаемый результат: "path/file/index.html"
print(add_index_html("path/file.ext"))  # ожидаемый результат: "path/file.ext"
print(add_index_html("path/index.html"))  # ожидаемый результат: "index.html"
'''

def get_path(url):
    if "/" not in url:
        return ""
    return os.path.join(*url.split('/')[:-1])

    
def add_slash_index(url):
    return add_index_html(add_trailing_slash(url))

def file_name_slash_index(url):
    parsed_url = os.path.splitext(url)  # Разбиваем URL на путь и расширение
    path = parsed_url[0]  # Получаем путь из разбитого URL

    if path.endswith('/'):
        return "index.html"

    if not path.endswith('/') and not parsed_url[1]:  # Проверяем условия
        file_name = url.split('/')[-1]
        file_name = file_name[:255]
        file_name += "/index.html"
        return file_name


    file_name = url.split('/')[-1]
    file_name = file_name[:255]
    return file_name

def url_slash_index(url):
    parsed_url = os.path.splitext(url)  # Разбиваем URL на путь и расширение
    path = parsed_url[0]  # Получаем путь из разбитого URL

    if path.endswith('/'):
        return url+"index.html"

    if not path.endswith('/') and not parsed_url[1]:    # Без расширения
        #file_name = url.split('/')[-1]
        #file_name = file_name[:255]
        return url+ "/index.html" 


    #file_name = url.split('/')[-1]
    #file_name = file_name[:255]
    return url



'''
url1 = 'http://example.com/test'  # URL без слеша в конце и без расширения
url2 = 'http://example.com/test/'  # URL с слешем в конце
url3 = 'http://example.com/test.html'  # URL с расширением
url4 = 'http://example.com/?fp=123'  # URL с расширением

print(add_slash_index(url1))  # http://example.com/test/
print(add_slash_index(url2))  # http://example.com/test/
print(add_slash_index(url3))  # http://example.com/test.html

print(file_name_slash_index(url1))  # http://example.com/test/
print(file_name_slash_index(url2))  # http://example.com/test/
print(file_name_slash_index(url3))  # http://example.com/test.html
print(file_name_slash_index(url4))  # http://example.com/test.html


'''