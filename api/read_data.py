import pandas as pd

errors = []

# Processing the data with more checks
with open('summary_all_repos1.txt', 'r') as file:
    lines = file.readlines()
    data = []
    i = 0
    while i < len(lines):
        try:
            # Ensure the current line starts with "Repository:"
            if lines[i].startswith("Repository:"):
                repo_name = lines[i].split(':')[-1].strip()
                
                # Try to extract the values for commits, issues, and tables
                num_commits = int(lines[i+1].split(':')[-1].strip())
                num_issues = int(lines[i+2].split(':')[-1].strip())
                num_tables = int(lines[i+3].split(':')[-1].strip())
                data.append((repo_name, num_commits, num_issues, num_tables))
                
                # Jump to the next repository data
                i += 6
            else:
                errors.append(f"Unexpected line format at line {i+1}: {lines[i]}")
                i += 1  # Move to the next line to prevent infinite loops
        except (IndexError, ValueError) as e:
            errors.append(f"Error processing data at line {i+1}: {e}")
            i += 1  # Move to the next line to prevent infinite loops

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=['Repository', 'Number of Commits', 'Number of Issues', 'Number of Tables'])

# Filter out the repositories with 0 tables (this step is optional based on your requirements)
df = df[df['Number of Tables'] > 0]

# Save the data as a CSV file
filename = 'correlation_data.csv'
df.to_csv(filename, index=False)

print(f"Data saved to: {filename}")
if errors:
    print("Encountered the following errors:")
    for error in errors:
        print(error)
