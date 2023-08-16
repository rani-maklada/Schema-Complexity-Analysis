import sys
from gitana.gitana import Gitana

def main():
    project_name = sys.argv[1]
    db_name = sys.argv[2]
    repo_name = sys.argv[3]
    git_repo_path = sys.argv[4]

    CONFIG = {
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'port': '3306',
        'raise_on_warnings': False,
        'buffered': True
    }
    GH_TOKENS = ['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']

    g = Gitana(CONFIG, None)
    g.delete_previous_logs()
    g.init_db(db_name)
    g.create_project(db_name, project_name)

    g.import_git_data(db_name, project_name, repo_name, git_repo_path, import_type=2)
    g.import_github_issue_data(db_name, project_name, repo_name, project_name + "_it",
                               git_repo_path, GH_TOKENS)

if __name__ == "__main__":
    main()
