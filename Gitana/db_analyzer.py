import mysql.connector

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

def analyze_repository(db_name):
    """
    Analyze the given repository.
    """
    connection = mysql.connector.connect(**CONFIG, database=db_name)
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

def main():
    repos = get_db_names()
    
    for repo in repos:
        commits, issues, users = analyze_repository(repo)
        print(f"Analysis for repository {repo}:")
        print(f"\tNumber of commits: {commits}")
        print(f"\tNumber of issues: {issues}")
        print(f"\tNumber of users: {users}\n")

if __name__ == "__main__":
    main()
