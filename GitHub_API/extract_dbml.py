import os
from fetch_functions import fetch_dbml_files, search_dbml_repositories
from file_functions import save_dbml_file
from content_count import get_commit_count, get_issue_count

def run_code():
    access_token = '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'  # Replace with your personal access token

    repositories_dir = 'repositories'
    os.makedirs(repositories_dir, exist_ok=True)

    relevant_repos = []

    # Search for repositories with .dbml files
    print(f"Searching for random repositories...")
    repos = search_dbml_repositories(access_token=access_token)
    print("Found", len(repos), "repositories.")

    for repo in repos:
        owner, repo_name = repo.split('/')
        print(f'Owner: {owner}, Repo Name: {repo_name}')

        print("\nProcessing repository:", repo_name)

        # Fetch DBML files
        print("Fetching DBML files...")
        dbml_files = fetch_dbml_files(owner, repo_name, access_token=access_token)
        print("Found", len(dbml_files), "DBML files.")
        if len(dbml_files) < 1:
            print('pass')
            continue

        # Save DBML files
        for dbml_file in dbml_files:
            print("Saving DBML file:", dbml_file['name'].encode('utf-8', 'ignore').decode('utf-8', 'ignore'))
            save_dbml_file(dbml_file, repo_name, repositories_dir, access_token=access_token)

        # Get number of commits
        commits_count = get_commit_count(owner,repo_name,access_token)
        # Get number of issues
        issues_count = get_issue_count(owner,repo_name,access_token)

        relevant_repos.append((repo, commits_count, issues_count))

        # Create summary text file
        summary_path = f'{repositories_dir}/{repo}/summary.txt'
        summary_dir = os.path.dirname(summary_path)
        os.makedirs(summary_dir, exist_ok=True)
        with open(summary_path, 'w') as summary_file:
            summary_file.write(f'Number of Commits: {commits_count}\n')
            summary_file.write(f'Number of Issues: {issues_count}\n')
        print("Summary file saved for repository:", repo)

    # Create summary file for all relevant repositories
    summary_file_path = 'summary_all_repos.txt'
    with open(summary_file_path, 'w') as summary_all_file:
        for repo_info in relevant_repos:
            repo, total_commits, total_issues = repo_info
            summary_all_file.write(f'Repository: {repo}\n')
            summary_all_file.write(f'Number of Commits: {total_commits}\n')
            summary_all_file.write(f'Number of Issues: {total_issues}\n')
            summary_all_file.write('\n')

    print("Summary file for all repositories saved:", summary_file_path)

if __name__ == "__main__":
    run_code()

