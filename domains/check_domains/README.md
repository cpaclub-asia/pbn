# PBN (Private Blog Network) Project

## TODO

### check_domains_whois

This subfolder includes scripts for checking whois data for the domains.
The main script to check whois data for a list of domains.

- ADD(Gleb) На вход сейчас принимает домен пробел 30 нужно поправить чтобы принимало CSV в любом формате, Имя столбца "Domain" указано как параметр командной строки. На выходе должен получаться CSV с исходными данными плюс в самом начале идут (добавлены если их не было) столбцы Status;Expiration Days;Expiration Date;Check date.Expiration Date в случае если были данные ранее, а домен стал Free и данные пропали - должна браться их исходного файла. Expiration Days отсчитывается от сохраненного Expiration Date. Отрицательное значение - значит что домен просрочен, Положительное - сколько дней до просрочки. Плюс небольшая корректировка по статусам. Если осталось до +30 дней - статус Soon, Если от 0 до -29 то Expiring ,если от -30 до -80 то Pending, Если от -80 до -бесконечности, то Free. Если он Free, но сколько дней назад закончилось, поле Expiration Days - пустое.
- ADD(Gleb) Мультипоточность как в lookup чекерк
 
  
##### Регламент:
- (Винод прставить и котролировать задачу) Еженедельно автоматом (к утру понедельника) чекинг нашей базы доменов на expired
    - google_domes
    - crawler2015, crawler текущий (позже crawler 2019, 2011)
    - majesctic текущий, majestic2021