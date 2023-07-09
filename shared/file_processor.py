from bs4 import BeautifulSoup
from shared.webarchive.html_utils import clean_html,clean_css
import shutil
from urllib.parse import urlparse
import os

def process_files(input_dir, output_dir, assets_dir):
    for root, dirs, files in os.walk(input_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            relative_dir = os.path.dirname(os.path.relpath(file_path,input_dir))
            if  is_html(file_name):
                print(f"Processing file_name,input_dir,output_dir,relative_dir: {file_name},{input_dir},{output_dir},{relative_dir}")
                clean_html(file_name,input_dir,output_dir,relative_dir)
            else:
                if is_css(file_name):
                    print(f"Processing CSS file_name,input_dir,output_dir,relative_dir: {file_name},{input_dir},{output_dir},{relative_dir}")
                    clean_css(file_name,input_dir,output_dir,relative_dir)
                else:
                    print("+");
                    src_file = os.path.join(input_dir, relative_dir,file_name)
                    dst_file = os.path.join(assets_dir, relative_dir,file_name)
                    os.makedirs(os.path.dirname(dst_file), exist_ok=True)  # Создаем целевую папку, если она не существует
                    shutil.copy(src_file, dst_file)


def get_file_extension(file_name):
    return os.path.splitext(file_name.split('?')[0])[1]


def is_html(file_name):
    file_extension = get_file_extension(file_name)
    if file_extension.lower() in ['.html', '.htm', '.asp', '.aspx', '.php', '']:
        return True
    return False


def is_img(file_name):
    file_extension = get_file_extension(file_name)
    if file_extension.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
        return True
    return False


def is_css(file_name):
    file_extension = get_file_extension(file_name)
    if file_extension.lower() in ['.css']:
        return True
    return False


def is_root_path(original_url):
    parsed_url = urlparse(original_url)
    path = parsed_url.path
    port = parsed_url.port
    return (path == '/' or path == '') and (not port or port == 80)








assert is_html('index.html') == True
assert is_html('about.htm') == True
assert is_html('contact.aspx') == True
assert is_html('file.php') == True
assert is_html('script.js') == False
assert is_html('file') == True
assert is_html('index.html?ver=123') == True
assert is_html('index.html?ver=7.5') == True
assert is_html('?p=123') == True

# Тесты
assert is_img('image.jpg') == True
assert is_img('image.jpeg') == True
assert is_img('image.png') == True
assert is_img('image.gif') == True
assert is_img('image.jpg?ver=123') == True
assert is_img('image.jpg?ver=7.5') == True
assert is_img('script.js') == False


# тесты
assert is_css('style.css') == True
assert is_css('style.css?ver=123') == True
assert is_css('style.css?ver=7.5') == True
assert is_css('script.js') == False
