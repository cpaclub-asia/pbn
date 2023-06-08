import requests
from bs4 import BeautifulSoup
import re
import os
from file_downloader import create_folder_structure

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

    # Lists to store different types of files
    index_files = []
    system_files = []
    html_files = []
    image_files = []
    other_files = []

    # Process each URL address
    for row in rows:
        timestamp, original_url = row.split(' ', 1)
        clean_url = re.sub(r'[\/:*?"<>|]', '_', original_url.strip())

        # Form the URL for downloading data
        download_url = f"https://web.archive.org/web/{timestamp}/{original_url}"

        # Determine the file type based on the URL
        file_extension = os.path.splitext(clean_url)[1].lower()

        # Add the file to the appropriate list
        if file_extension == '.html':
            html_files.append(download_url)
        elif file_extension == '.jpg' or file_extension == '.jpeg' or file_extension == '.png' or file_extension == '.gif':
            image_files.append(download_url)
        elif clean_url.endswith('sitemap.xml') or file_extension.endswith('robots.txt'):
            system_files.append(download_url)
        elif file_extension == '':
            index_files.append(download_url)
        else:
            other_files.append(download_url)

        # Check if the current version is the latest
        if clean_url not in last_versions:
            last_versions[clean_url] = download_url

    # Debug information about the list of files
    print("Number of HTML files:", len(html_files))
    print("Number of image files:", len(image_files))
    print("Number of system files:", len(system_files))
    print("Number of index files:", len(index_files))
    print("Number of other files:", len(other_files))

    # Display the list of files to be downloaded
    print("\nFiles to be downloaded:")
    print("Index Files:")
    print("\n".join(index_files))
    print("\nSystem Files:")
    print("\n".join(system_files))
    print("\nHTML Files:")
    print("\n".join(html_files))
    print("\nImage Files:")
    print("\n".join(image_files))
    print("\nOther Files:")
    print("\n".join(other_files))

    # Create the folder structure and download files based on priority
    create_folder_structure(domain_folder, index_files)
    create_folder_structure(domain_folder, system_files)
    create_folder_structure(domain_folder, html_files)
    create_folder_structure(domain_folder, image_files)
    create_folder_structure(domain_folder, other_files)

    print("Download completed.")
