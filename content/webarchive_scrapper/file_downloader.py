import requests
import os

def create_folder_structure(save_folder, file_list):
    for download_url in file_list:
        # Get the file name from the URL
        file_name = download_url.split('/')[-1]

        # Get the timestamp from the URL
        timestamp = download_url.split('/')[4]

        # Determine the file path and create folder structure
        path_segments = download_url.split('/')[5:-1]
        file_path = os.path.join(save_folder, timestamp, *path_segments)
        os.makedirs(file_path, exist_ok=True)

        # Form the path to save the file
        file_path = os.path.join(file_path, file_name)

        # Send a GET request to download data
        download_response = requests.get(download_url)

        # Save the data in the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(download_response.text)
            print(f"Downloaded file: {file_name}")
