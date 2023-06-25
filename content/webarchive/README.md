# PBN (Private Blog Network) Project

Самая главная задача - чтобы файлы, которые были в индексе в гугле и внешние ссылки вели на страницы с контентом, который уже был. ЧТОБЫ НЕ ПОТЕРЯТЬ СТАРЫЙ ТРАФИК И ЛЮДЕЙ
- Винод после выкладывания сайта проверяет, что все исторические внешние ссылки работают используя
    - https://ahrefs.com/ru/backlink-checker
    - https://www.google.com/search?q=site%3Acpaclub.asia&oq=site%3Acpaclub.asia&aqs=chrome..69i57j69i58.13513j0j7&sourceid=chrome&ie=UTF-8
    - https://www.google.com/search?q=info%3Acpaclub.asia&sxsrf=APwXEdfK9O-yypa8XGiP7dm_edOsIY82CA%3A1687660933494&ei=hamXZJm2HaOZseMPntauiAw&ved=0ahUKEwjZjMTzst3_AhWjTGwGHR6rC8EQ4dUDCA8&uact=5&oq=info%3Acpaclub.asia&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQA0oECEEYAFAAWLEDYIoFaABwAHgAgAFEiAGLApIBATSYAQCgAQHAAQE&sclient=gws-wiz-serp
    - semrush external links
- Винод каждый день контролирует
    - ежедневные изменения залиты в github
    - В README.md сразу описан функционал внесенных изменений
    - Примечание: ребята, не стесняйтесь делать сразу частые коммиты(даже если частичное решение), это полезная практика, мне будет видно правильно идете или нет и смогу уберечь вас от ошибок и траты времени

Workflow:


Добавляем список доменов в webarch-data/domains.txt, не забываем возврат каретки в конце файла
В webarch-data лежит скопированный сайт из вебархива. Хранится как локальный архив чтобы если что не нужно бывло перезагружать

The webarchive folder contains a suite of scripts used to interact with web.archive.org. The scripts within the `./webarchive` directory allow us to download, parse, compare, and convert the historical website data into a usable CSV format. Each `.sh` file represents a different phase in this process.

- `./webarchive/1.1_webarchive_scrapper.sh`: This shell script is responsible for scraping historical website data from the web archive.
    - ADD (Gleb) 1.1.sh ПЕРЕД скачкой страниц, СРАЗУ после загрузки списка с webarchive.org - создавать в корне файл /filelist.csv, в котором лежат
    - url оригинальный;url как сохранили;url как будет отображаться slug в wordpress;timestamp



    - ADD (Gleb) 1.2.sh просто полностью скопировать из  webarch-data в site-data, чтобы можно было не бояться удалять и работать с этой папкой
- `./webarchive/2_webarchive_parser.sh`: This script parses the downloaded web archive files.
    - ADD (GLEB) заменить чтобы скрипт 2 работал с папкой site-data и брал данные оттуда, а не из webarh
    - ADD (GLEB) 3.1 analyzec (язык, ключи из черного списка - выдавать сводное количество на всю папку)
    - ADD (GLEB) 3.2 all
- `./webarchive/4_webarchive_compare.sh`: This script compares the parsed web archive data.
    - ADD (Miron) Придумать и предложить вариант описания прямо сюда как работать с картинками
    - ADD (Miron) Создавать папочки content/page content/posts автоматически, чтобы не забыть
    - ADD (Miron) Написать вариант описания кратенько(не более 1 абзаца) прямо сюда как перемещать файлы posts и pages
    - ADD LATER(???)categories
    - ADD LATER(???)tags
    - ADD LATER LATER (???)подумать, как более эффективно выдергивать текст статей ничего не теряя и не приобретая ничего лишнего

- `./webarchive/5_webarchive_csv.sh`: This script converts the compared web archive data into a CSV format.
    - ADD LATER (???) создавать content/redirects.txt на базе filelist.csv для того, чтобы редиректить оригинальные ссылки на правильные slug
    - например:
    - ?p=about_us -> /about_us/
    - contacts/index.html -> /contacts/

    - ADD LATER (Miron) Написать вариант описания кратенько(не более 1 абзаца) прямо сюда про то, как грузим в Wordpress
    - ADD (Denis) нарезанное видеоописание


## 🌐 Overview
The content folder consists of several directories and scripts dedicated to content parsing and restoration. It is an essential part of the Private Blog Network (PBN) project, which helps in retrieving website content for both ongoing and dropped domains. Let's take a look at the details.

### ✨  Sub-folders and Files Description

### wget
`./wget/wget.sh` is a shell script that uses the wget command to download website content. `.gitignore` is present to prevent certain files from being tracked by git.

### webarchive



### webarchive_scrapper

This directory contains the scripts to download data from web.archive.org. 

```
All files downloaded as is and puts in folders by months.

Important!
Only one replacement occured
domain.com/path/subpath REPLACED TO domain.com/path/subpath/index.html
```

### webarchive_parser

This directory contains scripts to parse the downloaded web archives. 
```
Remove all web.archive.org links
```


### webarchive_compare

This directory contains scripts to compare the parsed data. 

```
Find uniquie and common elements.
From each page remove common elements
```



### webarchive_csv

This directory contains scripts to convert the compared web archives data to CSV format.

```
make csv to load on wordpress
```


## How to Use

Please make sure to execute scripts in their sequential order, starting from `1_webarchive_scrapper.sh`, then `2_webarchive_parser.sh`, followed by `3_webarchive_compare.sh`, and lastly `4_webarchive_csv.sh`.

Before running these scripts, make sure to set the correct permissions with chmod if necessary, and ensure all the dependencies are installed and up-to-date. 

For a more detailed instruction on how to use each script, please refer to the specific README.md files within each directory, if available.
