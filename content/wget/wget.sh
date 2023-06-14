$DOMAIN=https://mspmag.com/
wget --mirror --adjust-extension --page-requisites mspmag.com --directory-prefix webarch-data/wget $DOMAIN

#wget --mirror --convert-links --adjust-extension --page-requisites --no-parent <URL>

#+ --mirror - рекурсивно загружает весь сайт.
#- --convert-links - преобразует ссылки, чтобы они работали локально.
#- [НЕЛЬЗЯ! Не поймем, папка или HTML] --adjust-extension - добавляет расширения к файлам, если это необходимо.
#+ --page-requisites - загружает все необходимые элементы страницы, такие как изображения и стили.
#- --no-parent - не переходить на родительские директории при рекурсивной загрузке.