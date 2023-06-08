from bs4 import BeautifulSoup
import re

def remove_web_archive_links(html):
    soup = BeautifulSoup(html, 'html.parser')

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

    return str(soup)


def remove_scripts_and_css(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Удаление скриптов
    scripts = soup.find_all('script')
    for script in scripts:
        script.extract()

    # Удаление CSS
    styles = soup.find_all('style')
    for style in styles:
        style.extract()

    return str(soup)


def extract_head_and_body(html_file, head_file, body_file, body_original_file):
    with open(html_file, 'r') as file:
        html_content = file.read()

    # Удаление скриптов, CSS, ссылок с web.archive.org и префиксов во всех атрибутах из <head> и <body>
    cleaned_html = remove_scripts_and_css(html_content)
    cleaned_html = remove_web_archive_links(cleaned_html)

    soup = BeautifulSoup(cleaned_html, 'html.parser')

    head_tag = soup.head
    body_tag = soup.body

    if head_tag is None:
        print("Invalid HTML format: <head> tag is missing.")
        return
    if body_tag is None:
        print("Invalid HTML format: <body> tag is missing.")
        return

    head_content = str(head_tag)
    body_content = str(body_tag)

    with open(head_file, 'w') as file:
        file.write(head_content)

    with open(body_file, 'w') as file:
        file.write(body_content)

    with open(body_original_file, 'w') as file:
        file.write(html_content)

    print("Head content saved in", head_file)
    print("Body content saved in", body_file)


def extract_text_from_body(body_file, text_file):
    with open(body_file, 'r') as file:
        body_content = file.read()

    soup = BeautifulSoup(body_content, 'html.parser')

    tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'ul', 'i', 'b', 'strong', 'u', 'hr'])

    text = ''
    for tag in tags:
        if tag.has_attr('color'):
            text += f'<{tag.name} color="{tag["color"]}">{tag.get_text()}</{tag.name}>'
        else:
            text += f'<{tag.name}>{tag.get_text()}</{tag.name}>'

    with open(text_file, 'w') as file:
        file.write(text)

    print("Text content saved in", text_file)


def extract_images_from_body(body_file, images_file):
    with open(body_file, 'r') as file:
        body_content = file.read()

    soup = BeautifulSoup(body_content, 'html.parser')

    image_tags = soup.find_all('img')

    images = [tag['src'] for tag in image_tags]

    with open(images_file, 'w') as file:
        file.write('\n'.join(images))

    print("List of images saved in", images_file)


# Пример использования
html_file = 'giaydabonghana.com/last/https___giaydabonghana.com__20191011013355.html'
head_file = 'head.html'
body_file = 'body_parsed.html'
body_original_file = 'body_original.html'
text_file = 'text.html'
images_file = 'images.txt'

extract_head_and_body(html_file, head_file, body_file, body_original_file)
extract_text_from_body(body_file, text_file)
extract_images_from_body(body_file, images_file)




