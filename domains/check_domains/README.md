# PBN (Private Blog Network) Project


## TODO

### check_whois
-ADD если запись Free - подтягивать из кеша данные когда она стала Expired и не стирать
-ADD правильно выдавать кешированнеые данные если слишком много запросов и не стирать невыданными данными
-ADD почему нет Expired записей с sav.com

### check_domains_txt_gconsole
- ADD сть ли txt запись google console


### check_domains_webarchive
- ADD csv отображение есть ли ads.txt

### check_domains_google
- ADD сохраненная копия - проверять не зеркало ли и не склейка ли


##### Регламент:
- (Denis) Проверяет собственные домены free и expired (их не много, за один день)
- (Denis) Проверяет ежедневно домены из expireddomains с указанными фильтрами за последние 5 дней (перепроверять не нужно, то есть каждый день добавляется пятый день, в первый день доменов много) и СРАЗУ же выкладвает результат (потому что через 12 часов домены уже будут не актуальны). Начиная с 5 дневного срока идущего к сейчас
- (Denis) Проверяет ежедневно домены из диапазона 0 -30, которые еще работают, но скоро начнут expire.Начиная с -30. И делает их полный wget
- Важно: Домены должны быть сразу выложены другим для обозрения плюс маякнуть в телеге что и где выложено каждый день


##### Как делать ручную проверку после автоматической
- проверить, что есть в гугле выдача site:cpaclub.asia (минимум 1 страница, желательно favicon красивый)
- проверить, что в сохраненной странице google (сохраненная копия) адрес совпадает (если не совпадает - домен забраковываем)
- Посмотреть как выглядел сайт https://web.archive.org/web/20230208144738/https://cpaclub.asia
- Посмотреть сколько файлов было (минимум 50 html с контентом)
- Посмотреть https://ahrefs.com/ru/backlink-checker внешние страницы, (минимум сайтов 30, минимум рейтинг ?, посмотреть качество и что склеек нет)
- Посмотреть Semrush
- https://www.name.com/whois-lookup/cpaclub.asia проверить что домен действительно свободен (даже если показывает Free, бывает ошибка)

#### Как покупать очень качественные домены из pending
Только для реально дорогих и качественных
- Размещать backorder одновременно
    - https://www.name.com/deleting-domains/
    - https://www.sav.com/my_backorders/domain_list
    - godaddy
    - dropcatch
Если домен интересный, то если за него идет конкуренция - сначала случайным образом побеждает регистратор. А потом внутри регистратора смотрится, были ли другие заявки. У каждого геристратора одновременно оставляют заявки не многие, поэтому это увеличивает шансы на то, что конкурентов будет меньше.

#### Как покупать Free
    - .info -> 1$ -> https://www.123-reg.co.uk/
    - .com и другие -> sav.com(самое дешевое), но в принципе без разницы

#### Где списки pending
- name.com: https://www.name.com/domain/deleting/download
- sav.com: https://www.sav.com/domains/auctions https://d2yienn5xwenuj.cloudfront.net/sav_active_auctions_export.csv https://d1zluldjsudbem.cloudfront.net/sav_pending_delete_2023_06_26.csv

#### Где аукционы
- https://www.sav.com/domains/auctions

##### Регламент:
- (Винод прставить и котролировать задачу) Еженедельно автоматом (к утру понедельника) чекинг нашей базы доменов на expired
    - google_domes
    - crawler2015, crawler текущий (позже crawler 2019, 2011)
    - majesctic текущий, majestic2021# PBN (Private Blog Network) Project

## 🌐 Overview
This folder contains scripts related to domain management in the PBN project. It includes scripts for making domain lists, checking domains, and processing domain data. 

### 📂  Sub-folders and Files Description

## make_domains_lists
This subfolder contains scripts for creating a list of potential domains.

### scrap_google_by_keywords
This subfolder includes scripts to scrape Google by keywords.

#### `google.py`
The python script to scrape Google SERP (Search Engine Results Pages) based on given keywords.

## check_domains
This subfolder includes scripts for checking domain data. There are three subfolders inside: 

### check_domains_lookup
This subfolder contains scripts for domain lookup.

#### `check_domains_lookup.py`
The main script that checks domain availability using domain lookup.

### check_domains_whois
This subfolder includes scripts for checking whois data for the domains.

#### `ddec.py`
The main script to check whois data for a list of domains.

### domains_csv_to_txt
This subfolder contains scripts to process domain data, specifically converting domains data from CSV format to TXT format.

#### `make_txt.py`
The main script to convert domains data from CSV to TXT format.
