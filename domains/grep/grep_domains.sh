cat res/urls.txt | grep -Eo '[A-Za-z0-9.-]+\.([A-Za-z]{2,}|[A-Za-z]{2}\.[A-Za-z]{2})' > domains.csv