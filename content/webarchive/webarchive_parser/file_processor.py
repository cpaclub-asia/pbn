import os
import re
from bs4 import BeautifulSoup
from html_utils import extract_head_and_body,extract_text_from_body,extract_images_from_body


def process_files(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            relative_dir = os.path.dirname(os.path.relpath(file_path,input_dir))
            file_extension = os.path.splitext(file_name)[1]
            if file_extension.lower() in ['.html', '.htm', '.asp', '.aspx', '']:
                print(f"Processing file_name,input_dir,output_dir,relative_dir: {file_name},{input_dir},{output_dir},{relative_dir}")
                extract_head_and_body(file_name,input_dir,output_dir,relative_dir)

