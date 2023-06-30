import os
import re
from bs4 import BeautifulSoup
from funcs.webarchive.html_utils import remove_some
import shutil

def process_files(input_dir, output_dir, assets_dir):
    for root, dirs, files in os.walk(input_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            relative_dir = os.path.dirname(os.path.relpath(file_path,input_dir))
            if  is_html(file_name):
                print(f"Processing file_name,input_dir,output_dir,relative_dir: {file_name},{input_dir},{output_dir},{relative_dir}")
                remove_some(file_name,input_dir,output_dir,relative_dir)
            else:
                src_file = os.path.join(input_dir, relative_dir,file_name)
                dst_file = os.path.join(assets_dir, relative_dir,file_name)
                os.makedirs(os.path.dirname(dst_file), exist_ok=True)  # Создаем целевую папку, если она не существует
                shutil.copy(src_file, dst_file)


def is_html(file_name):
    file_extension = os.path.splitext(file_name)[1]
    if file_extension.lower() in ['.html', '.htm', '.asp', '.aspx', '.php', '']:
        return True
    return False

def is_img(file_name):
    file_extension = os.path.splitext(file_name)[1]
    if file_extension.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
        return True
    return False