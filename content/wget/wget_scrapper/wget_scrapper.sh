PATH=$1
DOMAIN=$2

/bin/mkdir $PATH/$DOMAIN
/usr/local/bin/wget --recursive --adjust-extension --page-requisites --recursive --span-hosts --restrict-file-names=windows --domains $DOMAIN --directory-prefix $PATH/$DOMAIN $DOMAIN  2> $PATH/$DOMAIN/wget.log

#wget --mirror --convert-links --adjust-extension --page-requisites --no-parent <URL>

#+ --mirror - рекурсивно загружает весь сайт.
#- [НЕЛЬЗЯ! нужно потом поменять вручную на slug WP]--convert-links - преобразует ссылки, чтобы они работали локально.
#- [НЕЛЬЗЯ! Не поймем, папка или HTML] --adjust-extension - добавляет расширения к файлам, если это необходимо.
#+ --page-requisites - загружает все необходимые элементы страницы, такие как изображения и стили.
#- --no-parent - не переходить на родительские директории при рекурсивной загрузке.

#wget \
#     --domains yoursite.com \ # Do not follow links outside this domain.
#     --no-parent \ # Don't follow links outside the directory you pass in.
#         yoursite.com/whatever/path # The URL to download
#@realowded

#    --recursive \
#    --adjust-extension \
#    --page-requisites \
#    --recursive \ # Download the whole site.
#    --span-hosts \ # Include necessary assets from offsite as well.
#    --convert-links \ # Update links to still work in the static version.
#    --restrict-file-names=windows \ # Modify filenames to work in Windows as well.
