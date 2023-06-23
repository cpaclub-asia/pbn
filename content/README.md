# PBN (Private Blog Network) Project

Самая главная задача - чтобы файлы, которые были в индексе в гугле и внешние ссылки вели на страницы с контентом, который уже был. ЧТОБЫ НЕ ПОТЕРЯТЬ СТАРЫЙ ТРАФИК И ЛЮДЕЙ

## 🌐 Overview
The content folder consists of several directories and scripts dedicated to content parsing and restoration. It is an essential part of the Private Blog Network (PBN) project, which helps in retrieving website content for both ongoing and dropped domains. Let's take a look at the details.

### ✨  Sub-folders and Files Description

### wget
`./wget/wget.sh` is a shell script that uses the wget command to download website content. `.gitignore` is present to prevent certain files from being tracked by git.

### webarchive

The webarchive folder contains a suite of scripts used to interact with web.archive.org. The scripts within the `./webarchive` directory allow us to download, parse, compare, and convert the historical website data into a usable CSV format. Each `.sh` file represents a different phase in this process.

read [content/webarchive/README.md](content/webarchive/README.md) for more details