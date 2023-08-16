import os

repositories_dir = 'repositories'
repo_info_summary = []

# Go through each repository folder and extract data from the summary.txt file
for repo_name in os.listdir(repositories_dir):
    repo_path = os.path.join(repositories_dir, repo_name)
    summary_path = os.path.join(repo_path, 'summary.txt')
    
    if os.path.exists(summary_path):
        with open(summary_path, 'r') as summary_file:
            content = summary_file.read()
            repo_info_summary.append((repo_name, content))

# Update the summary_all_repos.txt file with the aggregated information
summary_all_path = 'summary_all_repos.txt'
with open(summary_all_path, 'w') as summary_all_file:  # 'w' mode to overwrite
    for repo_summary in repo_info_summary:
        repo_name, summary_content = repo_summary
        summary_all_file.write(f"Repository: {repo_name}\n")
        summary_all_file.write(summary_content + "\n\n")

print("summary_all_repos.txt updated with content from all individual summaries.")
