# PBN (Private Blog Network) Project

### check_domains_google


## TODO
### check_domains_google



### check_domains_whois
This subfolder includes scripts for checking whois data for the domains.
The main script to check whois data for a list of domains.

- ADD(???) На вход сейчас принимает домен пробел 30 нужно поправить чтобы принимало CSV в любом формате, Имя столбца "Domain" указано как параметр командной строки. На выходе должен получаться CSV с исходными данными плюс в самом начале идут (добавлены если их не было) столбцы Status;Expiration Days;Expiration Date;Check date.Expiration Date в случае если были данные ранее, а домен стал Free и данные пропали - должна браться их исходного файла. Expiration Days отсчитывается от сохраненного Expiration Date. Отрицательное значение - значит что домен просрочен, Положительное - сколько дней до просрочки. Плюс небольшая корректировка по статусам. Если осталось до +30 дней - статус Soon, Если от 0 до -29 то Expiring ,если от -30 до -80 то Pending, Если от -80 до -бесконечности, то Free. Если он Free, но сколько дней назад закончилось, поле Expiration Days - пустое.

Основной полу ручной проверялщик

- ADD (Miron) - загрузка инфы сколько страниц в вебархиве
- ADD(Miron) Параллельно открывать во втором браузере - index web.archive
- ADD(Miron) количество страниц web.archive - тоже можно в третьем , чтобы видеть.
- ADD(Miron) В четвертом браузере - кеш гугла первой страницы

- ADD(Miron) Сохранение скриншота каждого окна через driver.save_screenshot('screenshot.png')
- ADD(???) Мультипоточность как в lookup чекерк


Регламент:
- (Denis) Проверяет собственные домены free и expired (их не много, за один день)
- (Denis) Проверяет ежедневно домены из expireddomains с указанными фильтрами за последние 5 дней (перепроверять не нужно, то есть каждый день добавляется пятый день, в первый день доменов много) и СРАЗУ же выкладвает результат (потому что через 12 часов домены уже будут не актуальны). Начиная с 5 дневного срока идущего к сейчас
- (Denis) Проверяет ежедневно домены из диапазона 0 -30, которые еще работают, но скоро начнут expire.Начиная с -30. И делает их полный wget
- Важно: Домены должны быть сразу выложены другим для обозрения плюс маякнуть в телеге что и где выложено каждый день



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
