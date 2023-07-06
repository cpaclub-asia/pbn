echo "На входе есть список доменов, нужно его обработать, выделить из него Free, Soon(от 0 до -30), Pending (от -30 до -80) и определить к ним статистики"

FILE=data/domains.csv

echo "Убираем дубликаты"
./check_domains/1_remove_duplicates $FILE $FILE.unique

echo "Разделяем на две группы - те которые connect и noconnect"
./check_domains/2_check_domains_lookup $FILE.unique $FILE.connect $FILE.noconnect

echo "Проверяем whois (можно в будушем параллельно) обоих групп"
./check_domains/3_check_domains_whois $FILE.connect $FILE.connect.whois
./check_domains/3_check_domains_whois $FILE.noconnect $FILE.noconnect.whois

./check_domains/4_grep_whois $FILE.connect.whois $FILE.connect.free $FILE.connect.soon
./check_domains/4_grep_whois $FILE.noconnect.whois $FILE.noconnect.free $FILE.noconnect.pending


