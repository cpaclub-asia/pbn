import os
import sys
import argparse
from bs4 import BeautifulSoup
import re


def remove_web_archive_links(soup):
    # Удаление тегов <link> с web.archive.org из <head>
    head_tag = soup.head
    if head_tag:
        links = head_tag.find_all('link', href=re.compile(r'web\.archive\.org'))
        for link in links:
            link.extract()

    # Удаление префикса "https://web.archive.org/web/XXXXXXXXXXXXXX/" из ссылок и атрибутов изображений и формы внутри <body>
    body_tag = soup.body
    if body_tag:
        tags = body_tag.find_all(['a', 'img', 'form'])
        for tag in tags:
            if tag.has_attr('href'):
                href = tag['href']
                href = re.sub(r'https://web\.archive\.org/web/\d+/', '', href)
                href = re.sub(r'https://web\.archive\.org/web/\d+im_/', '', href)
                tag['href'] = href
            if tag.has_attr('src'):
                src = tag['src']
                src = re.sub(r'https://web\.archive\.org/web/\d+/', '', src)
                src = re.sub(r'https://web\.archive\.org/web/\d+im_/', '', src)
                tag['src'] = src
            if tag.has_attr('action'):
                action = tag['action']
                action = re.sub(r'https://web\.archive\.org/web/\d+/', '', action)
                action = re.sub(r'https://web\.archive\.org/web/\d+im_/', '', action)
                tag['action'] = action

    return soup


def remove_scripts_and_css(soup):
    # Удаление скриптов
    scripts = soup.find_all('script')
    for script in scripts:
        script.extract()

    # Удаление CSS
    styles = soup.find_all('style')
    for style in styles:
        style.extract()

    return soup


def extract_head_and_body(html_file, output_dir):
    with open(html_file, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    cleaned_html = remove_scripts_and_css(soup)
    cleaned_html = remove_web_archive_links(cleaned_html)

    head_tag = cleaned_html.head
    body_tag = cleaned_html.body

    if head_tag is None:
        print(f"Invalid HTML format: <head> tag is missing in {html_file}")
        return
    if body_tag is None:
        print(f"Invalid HTML format: <body> tag is missing in {html_file}")
        return

    head_content = str(head_tag)
    body_content = str(body_tag)

    output_subdir = os.path.join(output_dir, 'head')
    os.makedirs(output_subdir, exist_ok=True)
    head_file = os.path.join(output_subdir, os.path.basename(html_file))
    with open(head_file, 'w') as file:
        file.write(head_content)

    output_subdir = os.path.join(output_dir, 'body_parsed')
    os.makedirs(output_subdir, exist_ok=True)
    body_file = os.path.join(output_subdir, os.path.basename(html_file))
    with open(body_file, 'w') as file:
        file.write(body_content)

    output_subdir = os.path.join(output_dir, 'body_original')
    os.makedirs(output_subdir, exist_ok=True)
    body_original_file = os.path.join(output_subdir, os.path.basename(html_file))
    with open(body_original_file, 'w') as file:
        file.write(html_content)

    print("Head content saved in", head_file)
    print("Body content saved in", body_file)


def extract_text_from_body(body_file, output_dir):
    with open(body_file, 'r') as file:
        body_content = file.read()

    soup = BeautifulSoup(body_content, 'html.parser')

    tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'ul', 'i', 'b', 'strong', 'u', 'hr','div'])

    text = ''
    for tag in tags:
        if tag.has_attr('color'):
            text += f'<{tag.name} color="{tag["color"]}">{tag.get_text()}</{tag.name}>'
        else:
            text += f'<{tag.name}>{tag.get_text()}</{tag.name}>'

    output_subdir = os.path.join(output_dir, 'text')
    os.makedirs(output_subdir, exist_ok=True)
    text_file = os.path.join(output_subdir, os.path.basename(body_file))
    with open(text_file, 'w') as file:
        file.write(text)

    print("Text content saved in", text_file)


def extract_images_from_body(body_file, output_dir):
    with open(body_file, 'r') as file:
        body_content = file.read()

    soup = BeautifulSoup(body_content, 'html.parser')

    image_tags = soup.find_all('img')

    images = [tag['src'] for tag in image_tags]

    output_subdir = os.path.join(output_dir, 'images')
    os.makedirs(output_subdir, exist_ok=True)
    images_file = os.path.join(output_subdir, os.path.basename(body_file) + '.txt')
    with open(images_file, 'w') as file:
        file.write('\n'.join(images))

    print("List of images saved in", images_file)


def process_files(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.html'):
                html_file = os.path.join(root, file)

                extract_head_and_body(html_file, output_dir)
                body_file = os.path.join(output_dir, 'body_parsed', os.path.basename(html_file))
                extract_text_from_body(body_file, output_dir)
                extract_images_from_body(body_file, output_dir)


def main():
    parser = argparse.ArgumentParser(description='HTML File Processor')
    parser.add_argument('input_dir', metavar='input_dir', type=str, help='Path to the input directory')
    parser.add_argument('output_dir', metavar='output_dir', type=str, help='Path to the output directory')
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir

    
    if not os.path.isdir(input_dir):
        parser.print_help()
        sys.exit(1)

    # Создание output_dir, если он не существует
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    process_files(input_dir, output_dir)


if __name__ == '__main__':
    main()
