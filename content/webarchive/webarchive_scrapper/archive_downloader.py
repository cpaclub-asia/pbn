import requests
from bs4 import BeautifulSoup
import re
import os
from urllib.parse import urlparse
from webarchive_scrapper.file_downloader import create_folder_structure
from shared.webarchive.webarchive_downloader import webarchive_get_list



def download_archive_data(domain, save_folder=None):
    index_files, system_files, html_files, image_files, other_files=webarchive_get_list(domain)

    # Create a folder to save data for the domain
    domain_folder = os.path.join(save_folder, domain) if save_folder else domain
    os.makedirs(domain_folder, exist_ok=True)

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
    print("\nOther Files:")
    print("\n".join(other_files))
    print("\nImage Files:")
    print("\n".join(image_files))


    # Create the folder structure and download files based on priority
    create_folder_structure(domain_folder, index_files)
    create_folder_structure(domain_folder, system_files)
    create_folder_structure(domain_folder, html_files)
    create_folder_structure(domain_folder, other_files)
    create_folder_structure(domain_folder, image_files)


    print("Download completed.")
