import os

repositories_dir = 'repositories'
summary_file_path = 'summary_all_repos.txt'

# Get all repository directories
repo_directories = [
    directory for directory in os.listdir(repositories_dir)
    if os.path.isdir(os.path.join(repositories_dir, directory))
]

with open(summary_file_path, 'w') as summary_all_file:
    for repo_directory in repo_directories:
        summary_file = os.path.join(repositories_dir, repo_directory, 'summary.txt')
        if os.path.exists(summary_file):
            with open(summary_file, 'r') as repo_summary_file:
                summary_content = repo_summary_file.read()
                # Extract the number of CREATE TABLE commands from the summary content
                create_table_count = int(summary_content.split(':')[-1].strip())

                if create_table_count > 0:
                    summary_all_file.write(summary_content)
                    summary_all_file.write('\n')

print("Summary file for all repositories saved:", summary_file_path)
