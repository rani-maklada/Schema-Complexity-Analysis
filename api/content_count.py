import requests

def get_issue_count(owner, repo, access_token=None):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {}
    if access_token:
        headers['Authorization'] = f'Token {access_token}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get("open_issues_count", 0)
    else:
        print(f"Failed to fetch repo info: {response.status_code}")
        return 0

def get_commit_count(owner, repo, access_token=None):
    page = 1
    commit_count = 0

    while True:
        url = f'https://api.github.com/repos/{owner}/{repo}/commits?per_page=100&page={page}'
        headers = {}
        if access_token:
            headers['Authorization'] = f'Token {access_token}'

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to fetch page {page}")
            break

        commits = response.json()
        if not commits:
            break

        commit_count += len(commits)
        page += 1

    return commit_count

