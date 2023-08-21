from gitana.gitana import Gitana
import warnings
import argparse
from halo import Halo
from db_connect import extract_data,find_db
warnings.filterwarnings("ignore")
import signal
# Define a function to set a timeout and handle timeout exception
def timeout_handler(signum, frame):
    raise TimeoutError("Function took too long to execute")

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('project_name', type=str, help='Name of the project')
parser.add_argument('repo_path', type=str, help='github Path to the repository')
parser.add_argument('target_directory', type=str, help='local Path to the repository')
args = parser.parse_args()


CONFIG = {
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'port': '3306',
        'raise_on_warnings': False,
        'buffered': True
    }
GH_TOKENS = ['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',
             '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',
             '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',
             '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']


def import_data(g, repo_name, db_name, repo_path, target_directory):
    g.init_db(db_name)
    g.create_project(db_name, repo_name)
    spinner = Halo(text='Importing GitHub data', spinner='dots')
    spinner.start()
    g.import_git_data(db_name, repo_name, "repo_"+repo_name, target_directory+"/"+repo_path)
    spinner.stop()
    spinner = Halo(text='Importing GitHub issue data', spinner='dots')
    spinner.start()
    g.import_github_issue_data(db_name, repo_name, "repo_"+repo_name, repo_name+"_it", repo_path, GH_TOKENS)
    spinner.stop()
def update_data(g, repo_name, db_name, repo_path, target_directory):
    spinner = Halo(text='Updating GitHub data', spinner='dots')
    spinner.start()
    g.update_git_data(db_name, repo_name, "repo_"+repo_name, target_directory+"/"+repo_path)
    spinner.stop()
    spinner = Halo(text='Updating GitHub issue data', spinner='dots')
    spinner.start()
    g.update_github_issue_data(db_name, repo_name, "repo_"+repo_name, repo_name+"_it", repo_path, GH_TOKENS)
    spinner.stop()


def main():
    g = Gitana(CONFIG, None)
    g.delete_previous_logs()
    db_name = "db_"+args.project_name
    repo_name = args.project_name
    repo_path = args.repo_path
    target_directory = args.target_directory
    print("db_name="+db_name.lower())
    db_exists = find_db(db_name.lower())
    if db_exists:
        update_data(g, repo_name, db_name, repo_path, target_directory)
    else:
        print("creating new project in "+db_name)
        import_data(g, repo_name, db_name, repo_path, target_directory)

    extract_data(db_name, repo_path)
if __name__ == "__main__":
    main()