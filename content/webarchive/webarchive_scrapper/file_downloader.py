import traceback
import os
import requests
from funcs import file_name_slash_index, is_root_path,url_slash_index

def create_folder_structure(save_folder, file_list):
    for download_url in file_list:
        try:
            # Get the file name from the URL
            # download_url have format f"https://web.archive.org/web/{timestamp}/{original_url}"

            # Get the timestamp from the URL
            timestamp = download_url.split('/')[4]
            year_month = timestamp[:6]

            original_url=download_url.split('/')[5:]



            parsed_url = urlparse(original_url)
            path_url = parsed_url.path
            file_url = original_url.split('/')[-1]

            if(file_url==""):
                file_url="index.html"


            print(f"path_url,file_url:{path_url},{file_url}")


            file_path = os.path.join(save_folder, year_month,path_url)
            os.makedirs(file_path, exist_ok=True)

            file_path_all = os.path.join(save_folder,"all", path_url)
            os.makedirs(file_path_all, exist_ok=True)


            # Send a GET request to download data
            download_response = requests.get(download_url)
            print(f"Downloaded file: {download_url}")


            # Save the data in the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(download_response.text)

            with open(file_path_all, 'w', encoding='utf-8') as file:
                file.write(download_response.text)
        except Exception as e:
            print(f"An error occurred while processing file: {download_url}")
            print(str(e))
            traceback.print_exc()
