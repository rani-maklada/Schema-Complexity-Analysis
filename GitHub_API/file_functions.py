import os
import requests

def save_dbml_file(dbml_file, repo_name, repositories_dir, access_token=None):

    # Make an additional request to get the download_url
    headers = {'Authorization': 'Token ' + access_token}
    response = requests.get(dbml_file['url'], headers=headers)

    if response.status_code != 200:
        print(f"Error fetching file info: {response.status_code}")
        print(response.json())
        return

    file_info = response.json()
    if 'download_url' not in file_info:
        print(f"No download_url in file info: {file_info}")
        return

    dbml_content = requests.get(file_info['download_url']).content

    try:
        dbml_content = dbml_content.decode('utf-8')
    except UnicodeDecodeError:
        print(f"Error decoding DBML file: {dbml_file['name']}")
        return

    dir_path = f"{repositories_dir}/{repo_name}"
    os.makedirs(dir_path, exist_ok=True)
    
    with open(f'{dir_path}/{dbml_file["name"]}', 'w', encoding='utf-8') as file:
        file.write(dbml_content)

