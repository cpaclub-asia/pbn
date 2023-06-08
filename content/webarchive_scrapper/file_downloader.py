import requests
import os

def create_folder_structure(save_folder, file_list):
    for download_url in file_list:
        # Get the file name from the URL
        file_name = download_url.split('/')[-1]
        file_name = file_name[:255]
        if (file_name==""):
            file_name="index.html"



        # Get the timestamp from the URL
        timestamp = download_url.split('/')[4]

        # Determine the file path and create folder structure
        path_segments = download_url.split('/')[8:-1]
        file_path = os.path.join(save_folder, timestamp, *path_segments)
        os.makedirs(file_path, exist_ok=True)

        path_segments_all = download_url.split('/')[8:-1]
        file_path_all = os.path.join(save_folder,"all", *path_segments)
        os.makedirs(file_path_all, exist_ok=True)


        # Form the path to save the file
        file_path = os.path.join(file_path, file_name)

        # Form the path to save the file
        file_path_all = os.path.join(file_path_all, file_name)


        # Send a GET request to download data
        download_response = requests.get(download_url)
        print(f"Downloaded file: {file_name}")


        # Save the data in the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(download_response.text)

        with open(file_path_all, 'w', encoding='utf-8') as file:
            file.write(download_response.text)
