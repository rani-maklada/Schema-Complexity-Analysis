from gitana.gitana import Gitana
import warnings
import argparse
from halo import Halo
warnings.filterwarnings("ignore")
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

def main():
    g = Gitana(CONFIG, None)
    g.delete_previous_logs()
    g.init_db("db_"+args.project_name)
    g.create_project("db_"+args.project_name, args.project_name)
    
    spinner = Halo(text='Importing GitHub data', spinner='dots')
    spinner.start()
    g.import_git_data("db_"+args.project_name, args.project_name, "repo_"+args.project_name, args.target_directory+"/"+args.project_name, import_type=2)
    spinner.stop()
    spinner = Halo(text='Importing GitHub issue data', spinner='dots')
    spinner.start()
    print("import_github_issue_data")
    g.import_github_issue_data("db_"+args.project_name, args.project_name, "repo_"+args.project_name, args.project_name+"_it", args.repo_path, GH_TOKENS)
    spinner.stop()

if __name__ == "__main__":
    main()