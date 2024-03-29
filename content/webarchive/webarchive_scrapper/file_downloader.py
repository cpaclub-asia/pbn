import traceback
import os
import requests



from shared.file_processor import is_root_path, add_index_html, get_path, is_binary

from urllib.parse import urlparse
from webarchive_scrapper.shared import urls_files;
from shared.inet import try_get_bin

import pprint

import tldextract

def get_second_level_domain(full_domain):
    extracted = tldextract.extract(full_domain)
    return f"{extracted.domain}.{extracted.suffix}"

#import requests_cache
#cache_dir = os.path.abspath("data/cache/webarchive/content")
#requests_cache.install_cache(cache_dir,backend="filesystem", serializer='json', expire_after=None)

# session = CachedSession(cache_dir)
#cache = requests_cache.get_cache()
#pprint.pprint(vars(cache.responses  ))


def create_folder_structure(save_folder, file_list):
    for download_url in file_list:
        try:
            # Get the file name from the URL
            # download_url have format f"https://web.archive.org/web/{timestamp}/{original_url}"
            # download_url have format f"https://web.archive.org/web/{timestamp}/http://{domain_url}/{path_url}"

            # Get the timestamp from the URL
            timestamp = download_url.split('/')[4]
            year_month = timestamp[:6]

            domain_url = download_url.split('/')[7]
            domain_c_url = domain_url.split(':')[0]
            domain2=get_second_level_domain(domain_c_url)

            path_url_ni = os.path.join(*download_url.split('/')[8:])
            
            path_url = add_index_html(path_url_ni)

            print(f"path_url: {path_url}")
            dir_url = get_path(path_url)

            file_path = os.path.join(save_folder, year_month, dir_url)
            file_path_all = os.path.join(save_folder, "all", dir_url)

            file_name = os.path.join(save_folder, year_month, path_url)
            file_name_all = os.path.join(save_folder, "all", path_url)

            #if(file_name==""):
            #    file_name="index.html"





            file_path = os.path.join(save_folder, year_month,dir_url)
            file_path_all = os.path.join(save_folder,"all", dir_url)

            file_name = os.path.join(save_folder, year_month,path_url)
            file_name_all = os.path.join(save_folder,"all", path_url)
            rel_file_name = os.path.join(year_month,path_url)

            #print(f"save_folder,year_month,domain_url,file_path,dir_url,path_url:{save_folder},{year_month},{domain_url},{path_url},{dir_url},{file_path}")
            print(f"domain_url:{domain_url}")
            print(f"path_url:{path_url}")
            print(f"dir_url:{dir_url}")
            print(f"file_path:{file_path}")
           

            os.makedirs(file_path, exist_ok=True)
            os.makedirs(file_path_all, exist_ok=True)

            # Send a GET request to download data

            print(f"Downloading url: {download_url}")
            
            code, content = try_get_bin(download_url  ,f"webarchive_sites/{domain2}")
            #code=200
            #content=session.get(download_url)

            if code==200:
              print("OK")
              with open(file_name, 'wb') as file:
                file.write(content)

              with open(file_name_all, 'wb') as file:
                file.write(content)

						# Determine the write mode based on the file extension
            '''
            if is_binary(file_name) :
              write_mode = 'wb'  # Binary mode for image files

								# Save the image files using the chosen write mode
              with open(file_name, write_mode) as file:
                file.write(download_response.content)

              with open(file_name_all, write_mode) as file:
                file.write(download_response.content)
            else:
              write_mode = 'w'  # Text mode for HTML files
              encoding = 'utf-8'

								# Save the HTML files using the chosen write mode and encoding
              with open(file_name, write_mode, encoding=encoding) as file:
                file.write(download_response.text)

              with open(file_name_all, write_mode, encoding=encoding) as file:
                file.write(download_response.text)
            '''

                
        except Exception as e:
            print(f"An error occurred while processing file: {download_url}")
            print(str(e))
            traceback.print_exc()