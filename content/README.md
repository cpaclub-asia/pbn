# PBN (Private Blog Network) Project


## 🌐 Overview
The content folder consists of several directories and scripts dedicated to content parsing and restoration. It is an essential part of the Private Blog Network (PBN) project, which helps in retrieving website content for both ongoing and dropped domains. Let's take a look at the details.

### ✨  Sub-folders and Files Description

### wget
`./wget/wget.sh` is a shell script that uses the wget command to download website content. `.gitignore` is present to prevent certain files from being tracked by git.

### webarchive

The webarchive folder contains a suite of scripts used to interact with web.archive.org. The scripts within the `./webarchive` directory allow us to download, parse, compare, and convert the historical website data into a usable CSV format. Each `.sh` file represents a different phase in this process.

- `./webarchive/1_webarchive_scrapper.sh`: This shell script is responsible for scraping historical website data from the web archive.
- `./webarchive/2_webarchive_parser.sh`: This script parses the downloaded web archive files.
- `./webarchive/3_webarchive_compare.sh`: This script compares the parsed web archive data.
- `./webarchive/4_webarchive_csv.sh`: This script converts the compared web archive data into a CSV format.


### webarchive_scrapper

This directory contains the scripts to download data from web.archive.org. 

```
All files downloaded as is and puts in folders by months.

Important!
Only one replacement occured
domain.com/path/subpath REPLACED TO domain.com/path/subpath/index.html
```

### webarchive_parser

This directory contains scripts to parse the downloaded web archives. 
```
Remove all web.archive.org links
```


### webarchive_compare

This directory contains scripts to compare the parsed data. 

```
Find uniquie and common elements.
From each page remove common elements
```

### manula work
```

manual remove some month with bad content -> make all again
manual make categories.txt
manual make pages.txt
manual make redirects

```


### webarchive_csv

This directory contains scripts to convert the compared web archives data to CSV format.

```
make csv to load on wordpress
```


## How to Use

Please make sure to execute scripts in their sequential order, starting from `1_webarchive_scrapper.sh`, then `2_webarchive_parser.sh`, followed by `3_webarchive_compare.sh`, and lastly `4_webarchive_csv.sh`.

Before running these scripts, make sure to set the correct permissions with chmod if necessary, and ensure all the dependencies are installed and up-to-date. 

For a more detailed instruction on how to use each script, please refer to the specific README.md files within each directory, if available.
