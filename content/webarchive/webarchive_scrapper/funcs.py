import os
from urllib.parse import urlparse, urlunparse


    
def add_trailing_slash(url):

    parsed_url = os.path.splitext(url)  # Разбиваем URL на путь и расширение
    path = parsed_url[0]  # Получаем путь из разбитого URL

    if not path.endswith('/') and not parsed_url[1]:  # Проверяем условия
        url += '/'  # Добавляем слеш в конец URL

    return url

def add_index_html(url):
    # If the URL contains query parameters, return the URL as is
    if "?" in url:
        return url
    # If the URL ends with a "/", append "index.html"
    elif url.endswith("/"):
        return url + "index.html"
    # If the URL is an empty string, return "index.html"
    elif url == "":
        return "index.html"
    # If the URL ends with a filename (i.e., contains a dot in the last segment), return the URL as is
    elif "." in url.split("/")[-1]:
        return url
    # In all other cases, append "/index.html" to the URL
    else:
        return url + "/index.html"

'''
# Run tests
assert add_index_html("") == "index.html"
assert add_index_html("?technology=flake8") == "?technology=flake8"
assert add_index_html("file.asp") == "file.asp"
assert add_index_html("file") == "file/index.html"
assert add_index_html("path/") == "path/index.html"
assert add_index_html("path/file") == "path/file/index.html"
assert add_index_html("path/file.ext") == "path/file.ext"
assert add_index_html("path/index.html") == "path/index.html"
assert add_index_html("path?technology=flake8") == "path?technology=flake8"
assert add_index_html("path/?technology=flake8") == "path/?technology=flake8"
assert add_index_html("path/file?technology=flake8") == "path/file?technology=flake8"
assert add_index_html("path/file.ext?technology=flake8") == "path/file.ext?technology=flake8"
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