import requests

def get_commit_count(owner, repo, access_token=None):
    headers = {}
    if access_token:
        headers['Authorization'] = f'Token {access_token}'

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    commit_count = 0
    page = 1

    while True:
        params = {'page': page, 'per_page': 100}
        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            commits = response.json()
            commit_count += len(commits)

            # Check if there are more pages
            if 'next' in response.links:
                page += 1
            else:
                break
        else:
            commit_count = None
            break

    return commit_count

# Example usage
owner = 'postgrespro'
repo = 'pg_pathman'
access_token = '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'  # Replace with your personal access token

commit_count = get_commit_count(owner, repo, access_token)
if commit_count is not None:
    print(f"Number of Commits: {commit_count}")
else:
    print("Failed to retrieve commit count.")
