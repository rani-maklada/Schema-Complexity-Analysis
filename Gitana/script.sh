#!/bin/bash

# Directory to clone the projects into
target_directory="cloned_projects"

# Create the target directory if it doesn't exist
mkdir -p "$target_directory"

# Read project URLs from dbml_repositories.txt and clone each project
while IFS= read -r repo_url
do
  # Remove leading/trailing spaces and extra characters from the URL
  repo_url=$(echo "$repo_url" | tr -d '\r' | sed 's/\.gits//g')

  # Extract owner and repo name from the URL
  IFS='/' read -ra parts <<< "$repo_url"
  owner="${parts[0]}"
  repo="${parts[1]}"

  # Create the GitHub repository URL in the correct format
  github_url="https://github.com/$owner/$repo.git"

  # Clone the project into the target directory
  git clone "$github_url" "$target_directory/$owner/$repo"

  echo "Cloned project: $repo"
  echo "Full repo path: $owner/$repo"

  # Run the Python script
  python script.py "$repo" "$owner/$repo" "$target_directory"
done < dbml_repositories.txt
