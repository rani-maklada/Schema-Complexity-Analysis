import mysql.connector
import os
repositories_dir = "repositories"
# Database configuration
CONFIG = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'port': '3306',
    'raise_on_warnings': False,
    'buffered': True
}

def get_db_names():
    """
    Return the list of database names (repositories).
    """
    connection = mysql.connector.connect(**CONFIG)
    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES")
    dbs = cursor.fetchall()
    connection.close()
    return [db[0] for db in dbs if db[0].startswith("db_")]  # Assuming that Gitana's database names start with "db_"

def find_db(db_name):
    connection = mysql.connector.connect(**CONFIG)
    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES")
    dbs = cursor.fetchall()
    connection.close()
    for (name,) in dbs:
        if name == db_name:
            return True
    return False


def analyze_repository(db_name):
    """
    Analyze the given repository.
    """
    config_with_db = CONFIG.copy()
    config_with_db['database'] = db_name
    connection = mysql.connector.connect(**config_with_db)
    cursor = connection.cursor()

    # Count commits
    cursor.execute("SELECT COUNT(*) FROM commit")
    num_commits = cursor.fetchone()[0]

    # Count issues
    cursor.execute("SELECT COUNT(*) FROM issue")
    num_issues = cursor.fetchone()[0]

    # Count users
    cursor.execute("SELECT COUNT(*) FROM user")
    num_users = cursor.fetchone()[0]

    connection.close()

    return num_commits, num_issues, num_users

def extract_data(repo,repo_path):
    commits, issues, users = analyze_repository(repo)
    print("Analysis for repository {}:".format(repo))
    # print("\tNumber of commits: {}".format(commits))
    # print("\tNumber of issues: {}".format(issues))
    # print("\tNumber of users: {}\n".format(users))

    # Create summary text file
    summary_path = '{}/{}'.format(repositories_dir, repo_path) + '/summary-new.txt'
    summary_dir = os.path.dirname(summary_path)

    # Check if directory exists, if not, create it
    if not os.path.exists(summary_dir):
        os.makedirs(summary_dir)

    with open(summary_path, 'w') as summary_file:
        summary_file.write('Number of Commits: {}\n'.format(commits))
        summary_file.write('Number of Issues: {}\n'.format(issues))

    print("Summary file saved for repository: {}".format(repo))

    
def main():
    repos = get_db_names()
    
    for repo in repos:
        commits, issues, users = analyze_repository(repo)
        print("Analysis for repository {}:".format(repo))
        print("\tNumber of commits: {}".format(commits))
        print("\tNumber of issues: {}".format(issues))
        print("\tNumber of users: {}\n".format(users))


if __name__ == "__main__":
    main()
