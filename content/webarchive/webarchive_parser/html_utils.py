import os
import re
from bs4 import BeautifulSoup

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


def extract_head_and_body(file_name,input_dir,output_dir,relative_dir):
    html_file = os.path.join(input_dir,relative_dir,file_name)

    with open(html_file, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    cleaned_html = remove_scripts_and_css(soup)
    cleaned_html = remove_web_archive_links(cleaned_html)

    head_tag = cleaned_html.head
    body_tag = cleaned_html.body

    if head_tag is None:
        print(f"Invalid HTML format: <head> tag is missing in {html_file}")
        head_tag=""
    if body_tag is None:
        print(f"Invalid HTML format: <body> tag is missing in {html_file}")
        body_tag=""

    head_content = str(head_tag)
    body_content = str(body_tag)

    output_subdir = os.path.join(output_dir, 'head',relative_dir)
    os.makedirs(output_subdir, exist_ok=True)
    head_file = os.path.join(output_subdir, os.path.basename(html_file))
    with open(head_file, 'w') as file:
        file.write(head_content)

    output_subdir = os.path.join(output_dir, 'body',relative_dir)
    os.makedirs(output_subdir, exist_ok=True)
    body_file = os.path.join(output_subdir, os.path.basename(html_file))
    with open(body_file, 'w') as file:
        file.write(body_content)

    text_content=extract_text_from_body(body_content)
    output_subdir = os.path.join(output_dir, 'text',relative_dir)
    os.makedirs(output_subdir, exist_ok=True)
    text_file = os.path.join(output_subdir, os.path.basename(html_file))
    with open(text_file, 'w') as file:
        file.write(text_content)

    images_content=extract_images_from_body(body_content)
    output_subdir = os.path.join(output_dir, 'images',relative_dir)
    os.makedirs(output_subdir, exist_ok=True)
    images_file = os.path.join(output_subdir, os.path.basename(html_file))
    with open(images_file, 'w') as file:
        file.write(images_content)


def extract_text_from_body(body_content):

    soup = BeautifulSoup(body_content, 'html.parser')

    tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'ul', 'i', 'b', 'strong', 'u', 'hr','div','img'])

    text = ''
    for tag in tags:
        if tag.has_attr('color'):
            text += f'<{tag.name} color="{tag["color"]}">{tag.get_text()}</{tag.name}>'
        else:
            text += f'<{tag.name}>{tag.get_text()}</{tag.name}>'

    return text


def extract_images_from_body(body_content):

    soup = BeautifulSoup(body_content, 'html.parser')

    image_tags = soup.find_all('img')

    images = [tag['src'] for tag in image_tags]

    return '\n'.join(images)
