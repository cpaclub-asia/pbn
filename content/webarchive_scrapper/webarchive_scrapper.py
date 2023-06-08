import argparse
import requests
from bs4 import BeautifulSoup
import re
import os
import shutil

def download_archive_data(domain, save_folder=None):
    # Create a folder to save data for the domain
    domain_folder = os.path.join(save_folder, domain) if save_folder else domain
    os.makedirs(domain_folder, exist_ok=True)

    # Form the URL for requesting data from the web archive
    url = f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=xml&fl=timestamp,original&collapse=urlkey"

    # Debug print the URL
    print("Request URL:", url)

    # Send a GET request to retrieve data
    response = requests.get(url)

    # Parse the XML response
    soup = BeautifulSoup(response.content, 'lxml')
    response_text = response.text.strip()
    rows = response_text.split('\n')

    # Dictionary to store the last versions of each file
    last_versions = {}

    # Download data for each URL address
    for row in rows:
        timestamp, original_url = row.split(' ', 1)
        clean_url = re.sub(r'[\/:*?"<>|]', '_', original_url.strip())

        # Form folder structure
        date_folder = os.path.join(domain_folder, timestamp[:8])
        os.makedirs(date_folder, exist_ok=True)

        # Form the path to save the file
        file_name = f"{clean_url}_{timestamp}.html"
        file_path = os.path.join(date_folder, file_name)

        # Form the URL for downloading data
        download_url = f"https://web.archive.org/web/{timestamp}/{original_url}"

        # Send a GET request to download data
        download_response = requests.get(download_url)

        # Save the data in the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(download_response.text)
            print(f"Downloaded file: {file_name}")

        # Check if the current version is the latest
        if clean_url not in last_versions:
            last_versions[clean_url] = file_path
        else:
            # Remove the previous version of the file
            os.remove(last_versions[clean_url])
            last_versions[clean_url] = file_path

        # Update the "last" folder with the latest versions of files
        last_folder = os.path.join(domain_folder, "last")
        os.makedirs(last_folder, exist_ok=True)
        last_file_path = os.path.join(last_folder, file_name)
        shutil.copyfile(file_path, last_file_path)

    print("Download completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download data from the web archive for a given domain.")
    parser.add_argument("domain", help="domain to download data for")
    parser.add_argument("-f", "--folder", help="folder to save the downloaded data")
    args = parser.parse_args()

    download_archive_data(args.domain, args.folder)
