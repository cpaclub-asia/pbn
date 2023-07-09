import os
import re
from bs4 import BeautifulSoup,Comment
import traceback

def remove_wa_links(html):
    if "<title>Wayback Machine</title>" in html:
        raise CustomException("Пустая страница WA")

    updated_value = html
    updated_value = re.sub(r'https://web\.archive\.org/web/\d+/', '', updated_value)
    updated_value = re.sub(r'https://web\.archive\.org/web/\d+im_/', '', updated_value)
    updated_value = re.sub(r'https://web\.archive\.org/web/\d+cs_/', '', updated_value)
    
    updated_value = re.sub(r'//web\.archive\.org/web/\d+/', '', updated_value)
    updated_value = re.sub(r'//web\.archive\.org/web/\d+im_/', '', updated_value)
    updated_value = re.sub(r'//web\.archive\.org/web/\d+cs_/', '', updated_value)

    updated_value = re.sub(r'/web/\d+/', '', updated_value)
    updated_value = re.sub(r'/web/\d+im_/', '', updated_value)
    updated_value = re.sub(r'/web/\d+cs_/', '', updated_value)

    return updated_value


def remove_tags(soup):
    # Удаление тегов <link> с web.archive.org из <head>
    head_tag = soup.head
    if head_tag:
        css_links = soup.find_all('link', attrs={'rel': 'stylesheet', 'href': lambda href: href and '_static' in href})
        for link in css_links:
            link.extract()
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


def css_remove_specific_comments(text,comment):
    pattern = r'/\*[^*]*\*+(?:[^/*][^*]*\*+)*/'
    matches = re.findall(pattern, text, re.MULTILINE | re.DOTALL)
    
    for match in matches:
        if comment in match:
            text = text.replace(match, '')
    
    return text

def html_remove_specific_comments(text,comment):
    pattern = r'<!--(.*?)-->'
    matches = re.findall(pattern, text, re.MULTILINE | re.DOTALL)
    
    for match in matches:
        if comment in match:
            text = text.replace(match, '')
    
    return text



def css_remove_comments(css):
    for comment in comments_to_remove:
        css = css_remove_specific_comments(css,comment)
    return css


def html_remove_comments(html):
    for comment in comments_to_remove:
        html = html_remove_specific_comments(html,comment)
    return html

def soup_remove_comments(soup):
    comments = soup.find_all(text=lambda text: isinstance(text, Comment))

    for comment in comments:
        if any(keyword in comment for keyword in comments_to_remove):
            comment.extract()
    return soup






def clean_html(file_name,input_dir,output_dir,relative_dir):
    html_file = os.path.join(input_dir,relative_dir,file_name)

    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as file:
            html_content = file.read()

        html_content=remove_wa_links(html_content)
        #html_content=html_remove_comments(html_content)

        soup = BeautifulSoup(html_content, 'html.parser')

        removed_html = remove_tags(soup)
        removed_html2 = remove_scripts(removed_html)
        removed_html3 = soup_remove_comments(removed_html2)
        final=str(removed_html3)

        output_subdir = os.path.join(output_dir,relative_dir)
        os.makedirs(output_subdir, exist_ok=True)
        file = os.path.join(output_subdir, os.path.basename(html_file))
        with open(file, 'w') as file:
            file.write(final)
    except Exception as e:
        print(f"ERROR!!!! An error occurred while processing file: {html_file}")
        print(str(e))
        traceback.print_exc()


def clean_css(file_name,input_dir,output_dir,relative_dir):
    html_file = os.path.join(input_dir,relative_dir,file_name)

    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as file:
            html_content = file.read()

        html_content=remove_wa_links(html_content)
        html_content=css_remove_comments(html_content)

        
        final=html_content

        output_subdir = os.path.join(output_dir,relative_dir)
        os.makedirs(output_subdir, exist_ok=True)
        file = os.path.join(output_subdir, os.path.basename(html_file))
        with open(file, 'w') as file:
            file.write(final)
    except Exception as e:
        print(f"ERROR!!!! An error occurred while processing file: {html_file}")
        print(str(e))
        traceback.print_exc()




'''

BROKEN
html = '<!-- FILE ARCHIVED ON 222 22 22--> <p>Sample text</p>'; assert html_remove_comments(html) == ' <p>Sample text</p>'  # Пример 1
html = '<!-- playback timings 444 --> <div>Sample content</div>'; assert html_remove_comments(html) == ' <div>Sample content</div>'  # Пример 2
html = '<!-- End Wayback Rewrite JS Include --> <h1>Sample heading</h1>'; assert html_remove_comments(html) == ' <h1>Sample heading</h1>'  # Пример 3
html = '<div>Sample content</div>'; assert html_remove_comments(html) == '<div>Sample content</div>'  # Пример 4 (нет комментариев для удаления)
html = '<!-- FILE ARCHIVED ON --> Some text <!-- DONT DELETE -->'; assert html_remove_comments(html) == ' Some text <!-- DONT DELETE -->'  # Пример 5
'''

html = '<style>/* FILE ARCHIVED ON 4 4  */ .class { color: red; } </style>'; assert css_remove_comments(html) == '<style> .class { color: red; } </style>'  # Пример 1
html = '<style>/* playback timings 4444 */ .class { background: blue; } </style>'; assert css_remove_comments(html) == '<style> .class { background: blue; } </style>'  # Пример 2
html = '<style>/* End Wayback Rewrite JS Include */ .class { font-size: 12px; } </style>'; assert css_remove_comments(html) == '<style> .class { font-size: 12px; } </style>'  # Пример 3
html = '<style>.class { color: green; }</style>'; assert css_remove_comments(html) == '<style>.class { color: green; }</style>'  # Пример 4 (нет комментариев для удаления)
html = '/* FILE ARCHIVED ON */ Some text /* DONT DELETE */'; assert css_remove_comments(html) == ' Some text /* DONT DELETE */'  # Пример 5


