
import csv
import os
import re
import datetime
import random



def make_csv(files_dir,title_path,csv_path):
    id=1
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['ID','Title','Content','Excerpt','Date','"Post Type"','Permalink']



        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,quoting=csv.QUOTE_ALL)
        writer.writeheader()

        # Парсинг HTML-файлов и сохранение элементов в словаре
        for root, dirs, files in os.walk(files_dir):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                relative_dir = os.path.dirname(os.path.relpath(file_path,files_dir))
                filename_relative = os.path.join(relative_dir, file_name)
                title_file = os.path.join(title_path,relative_dir, file_name)
                
                slug=remove_index(filename_relative)
                
                #slug=filename_relative
                #if file_name.endswith('index.html'):
                #    slug = slug.replace('index.html', '')

                print (f"slug,file_name,file_path,relative_dir,filename_relative:{slug},{file_name},{file_path},{relative_dir},{filename_relative}")

                if file_name.endswith('.html'):
                    print(f"csv->:{file_path}")
                    with open(file_path, 'r', encoding='utf-8') as f:
                        with open(title_file, 'r', encoding='utf-8') as f2:
                            html = f.read()
                            title = f2.read()
                            writer.writerow({'ID':id,'Title':title,'Content': html,'Excerpt':'','Date':generate_random_date(),'"Post Type"':'post','Permalink':slug})
                            id+=1
 



def remove_index(url):
    # Remove "index.html" and replace with "/"
    if "index.html" in url:
        url = url.replace("index.html", "/")

    # If "?" is present, remove everything before "="
    elif "?" in url:
        url = re.sub(r'.*=', '', url) + "/"
        
    # If none of the above, return original URL with "/" appended
    else:
        url = url + "/"

    return url


'''
assert remove_index("index.html") == "/"
assert remove_index("?technology=flake8") == "flake8/"
assert remove_index("path/index.html") == "path/"
assert remove_index("path/file.ext") == "path/file.ext/"
'''






def generate_random_date():
    current_date = datetime.datetime.now()  # Get the current date and time
    random_offset = random.randint(0, 180)  # Generate a random number between 0 and 180

    # Subtract the random number of days from the current date
    random_date = current_date - datetime.timedelta(days=random_offset)

    # Format the random date in the desired format
    formatted_date = random_date.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_date










