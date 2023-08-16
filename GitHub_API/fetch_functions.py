import requests

def search_dbml_repositories(access_token=None):
    api_url = 'https://api.github.com/search/code'  # Search API endpoint for code
    repos = set()
    page = 1

    while True:
        search_params = {
            'q': 'extension:dbml',
            'per_page': 100,
            'page': page
        }

        headers = {}
        if access_token:
            headers['Authorization'] = f'Token {access_token}'

        response = requests.get(api_url, params=search_params, headers=headers)

        if response.status_code == 200:
            results = response.json()
            items = results['items']
            for item in items:
                repo_name = item['repository']['full_name']
                repos.add(repo_name)

            # if there is no link for the next page in the response or we've found 10 repositories, stop
            if 'next' not in response.links or len(repos) >= 10:
                break

            page += 1
        else:
            break

    return list(repos)



def fetch_dbml_files(owner, repo, access_token=None):
    dbml_files = []

    # Make API request to get repository contents
    url = f'https://api.github.com/search/code?q=extension:dbml+repo:{owner}/{repo}'
    headers = {}
    if access_token:
        headers['Authorization'] = f'Token {access_token}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        contents = response.json()

        for item in contents['items']:
            file_info = item
            # Construct the download_url
            file_info['download_url'] = f"https://raw.githubusercontent.com/{owner}/{repo}/master/{file_info['path']}"
            dbml_files.append(file_info)

    return dbml_files



