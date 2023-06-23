# PBN (Private Blog Network) Project

### check_domains_google


Основной полу ручной проверялщик

- ADD (Miron) - загрузка инфы сколько страниц в вебархиве
- ADD(???) Параллельно открывать во втором браузере - index web.archive
- ADD(???) количество страниц web.archive - тоже можно в третьем , чтобы видеть.
- ADD(???) В четвертом браузере - кеш гугла первой страницы


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
