import requests
import logging

API_URL = 'https://api.github.com/search/code'
RESULTS_PER_PAGE = 100
MAX_REPOSITORIES = 10

def search_dbml_repositories(access_token=None):
    repos = set()
    page = 1

    while True:
        search_params = {
            'q': 'extension:dbml',
            'sort': 'random',
            'per_page': RESULTS_PER_PAGE,
            'page': page
        }

        headers = {}
        if access_token:
            headers['Authorization'] = f'Token {access_token}'

        try:
            response = requests.get(API_URL, params=search_params, headers=headers)
            response.raise_for_status()  # Raise HTTPError for bad responses

            results = response.json()
            items = results['items']
            for item in items:
                repo_name = item['repository']['full_name']
                repos.add(repo_name)

            if 'next' not in response.links or len(repos) >= MAX_REPOSITORIES:
                break

            page += 1
        except requests.RequestException as e:
            logging.error("Request error: %s", e)
            break

    return list(repos)

def save_repositories_to_txt(repositories):
    with open('Gitana/dbml_repositories.txt', 'w') as file:
        for repo in repositories:
            file.write(f"{repo}\n")

if __name__ == "__main__":
    # access_token = input("Enter your GitHub access token: ")
    access_token = "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"
    
    try:
        print("Searching for repositories with .dbml files...")
        dbml_repositories = search_dbml_repositories(access_token)
        print(f"Found {len(dbml_repositories)} repositories.")

        if dbml_repositories:
            print("Saving results to dbml_repositories.txt...")
            save_repositories_to_txt(dbml_repositories)
            print("Results saved successfully in dbml_repositories.txt.")
        else:
            print("No repositories with .dbml files found.")
    except requests.RequestException as e:
        print("Error occurred during the search:", e)
