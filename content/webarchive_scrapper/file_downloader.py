def create_folder_structure(save_folder, file_list):
    for download_url in file_list:
        try:
            # Get the file name from the URL
            file_name=file_name_slash_index(download_url)


            # Get the timestamp from the URL
            timestamp = download_url.split('/')[4]

            # Determine the file path and create folder structure
            path_segments = download_url.split('/')[8:-1]

            path_segments2 = file_name.split('/')[:-1]

            file_path = os.path.join(save_folder, timestamp, *path_segments,*path_segments2)
            os.makedirs(file_path, exist_ok=True)

            print(file_name)
            print(file_path)

            file_path_all = os.path.join(save_folder,"all", *path_segments,*path_segments2)
            os.makedirs(file_path_all, exist_ok=True)
            print(file_path_all)


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
        except Exception as e:
            print(f"An error occurred while processing file: {download_url}")
            print(str(e))
