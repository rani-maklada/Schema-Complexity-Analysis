import os

def main(repositories_dir = 'repositories'):
    repo_info_summary = []

    # Go through each owner directory and then each repository folder 
    # to extract data from the summary.txt file
    for owner_name in os.listdir(repositories_dir):
        owner_path = os.path.join(repositories_dir, owner_name)
        
        # Ensure that the owner_path is a directory
        if os.path.isdir(owner_path):
            for repo_name in os.listdir(owner_path):
                repo_path = os.path.join(owner_path, repo_name)
                summary_path = os.path.join(repo_path, 'summary.txt')
                
                if os.path.exists(summary_path):
                    with open(summary_path, 'r') as summary_file:
                        content = summary_file.read()
                        # Store both the owner_name and repo_name along with content for clarity
                        repo_info_summary.append((owner_name, repo_name, content))

    # Update the summary_all_repos.txt file with the aggregated information
    summary_all_path = 'summary_all_repos.txt'
    with open(summary_all_path, 'w') as summary_all_file:  # 'w' mode to overwrite
        for owner, repo, summary_content in repo_info_summary:
            summary_all_file.write(f"Owner: {owner}\n")
            summary_all_file.write(f"Repository: {repo}\n")
            summary_all_file.write(summary_content + "\n\n")

    print("summary_all_repos.txt updated with content from all individual summaries.")

# This allows you to run the script directly, and the main() function will be executed.
if __name__ == "__main__":
    main()
