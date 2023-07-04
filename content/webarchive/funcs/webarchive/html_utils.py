import os
import re
from bs4 import BeautifulSoup,Comment

def remove_web_archive_links(soup):
    # Удаление тегов <link> с web.archive.org из <head>
    head_tag = soup.head
    if head_tag:
        css_links = soup.find_all('link', attrs={'rel': 'stylesheet', 'href': lambda href: href and '_static' in href})
        for link in css_links:
            link.extract()
        
    tags = soup.find_all()
    for tag in tags:
        for attr, value in tag.attrs.items():
            if isinstance(value, str):
                updated_value = re.sub(r'https://web\.archive\.org/web/\d+/', '', value)
                updated_value = re.sub(r'https://web\.archive\.org/web/\d+im_/', '', updated_value)
                updated_value = re.sub(r'https://web\.archive\.org/web/\d+cs_/', '', updated_value)
                #https://web.archive.org/web/20230130234931im_
                updated_value = re.sub(r'//web\.archive\.org/web/\d+/', '', value)
                updated_value = re.sub(r'//web\.archive\.org/web/\d+im_/', '', updated_value)
                updated_value = re.sub(r'//web\.archive\.org/web/\d+cs_/', '', updated_value)

                updated_value = re.sub(r'/web/\d+/', '', updated_value)
                updated_value = re.sub(r'/web/\d+im_/', '', updated_value)
                updated_value = re.sub(r'/web/\d+cs_/', '', updated_value)

                tag[attr] = updated_value


    return soup


def remove_scripts(soup):
    # Удаление скриптов
    scripts = soup.find_all('script')
    for script in scripts:
        script.extract()
    return soup

comments_to_remove = [
    'FILE ARCHIVED ON',
    'playback timings',
    'End Wayback Rewrite JS Include'
]

def remove_comments(soup):
    comments = soup.find_all(text=lambda text: isinstance(text, Comment))

    for comment in comments:
        if any(keyword in comment for keyword in comments_to_remove):
            comment.extract()
    return soup








def remove_some(file_name,input_dir,output_dir,relative_dir):
    html_file = os.path.join(input_dir,relative_dir,file_name)

    with open(html_file, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    removed_html = remove_web_archive_links(soup)
    removed_html2 = remove_scripts(removed_html)
    removed_html3 = remove_comments(removed_html2)

    output_subdir = os.path.join(output_dir,relative_dir)
    os.makedirs(output_subdir, exist_ok=True)
    file = os.path.join(output_subdir, os.path.basename(html_file))
    with open(file, 'w') as file:
        file.write(str(removed_html3))




