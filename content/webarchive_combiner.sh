echo "Работаем по доменам из списка domains.txt"

./webarchive/1_webarchive_scrapper.sh data data/domains.txt
./webarchive/1.1_webarchive_copy data data/domains.txt
./webarchive/2_webarchive_parser.sh data data/domains.txt
./webarchive/3.1_webarchive_analyze.sh data data/domains.txt

echo "Вручную(в отдельном шелле) удалите папки с найденными месяцами плохого контента"
echo "После этого нажмите любую клавишу для продолжения"
read -n 1

#TODO RM папку отпарсенную, чтобы хлама не осталось и запустить второй раз пункт 2
./webarchive/2_webarchive_parser.sh data data/domains.txt
./webarchive/3.2_webarchive_all.sh data data/domains.txt
./webarchive/4_webarchive_compare.sh data data/domains.txt

echo "Вручную(в отдельном шелле) разнесите файлы из папки unique в posts,pages,tags,categories"
echo "После этого нажмите любую клавишу для продолжения"
read -n 1

./webarchive/5_webarchive_csv.sh data data/domains.txt
echo "Готово, можете загружать csv и медиафайлы в wordpress"
