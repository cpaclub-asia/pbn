import argparse
from webarchive_scrapper.archive_downloader import download_archive_data
from webarchive_scrapper.shared import urls_files;


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download data from the web archive for a given domain.")
    parser.add_argument("domain", help="domain to download data for")
    parser.add_argument("-f", "--folder", help="folder to save the downloaded data")
    args = parser.parse_args()
    text=args.domain
    folder=args.folder
    
    parts = text.split(";")

    domain = parts[0]
    args2 = parts[1] if len(parts) > 1 else ""

    
    download_archive_data(domain, folder,args2)
