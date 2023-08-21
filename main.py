from GitHub_API.search_dbml import main as search_dbml
from GitHub_API.extract_dbml import main as extract_dbml
from dbdiagram.xml_dbml import main as xml_dbml
from dbdiagram.automate_dbdiagram_and_upload import main as automate_dbdiagram_and_upload
from data_analyze.count_tables import main as count_tables
from read_data.create_data import main as create_data
from data_analyze.analyze_all import main as analyze_all
from data_analyze.analyze_correlation import main as analyze_correlation
from data_analyze.analyze_multi import main as analyze_multi
from gitana_envirement import main as gitana_envirement
from scripts.update_summary_all import main as update_summary_all
access_token = "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"
# Prompt the user for the access token
# access_token = input("Please input your ACCESS_TOKEN: ")

repository_dir = "demo-repositories"

def main():
    # repos = search_dbml(access_token)
    # extract_dbml(access_token, repos, repository_dir)
    # xml_dbml(repository_dir)
    # automate_dbdiagram_and_upload(repository_dir)
    # Run gitana_envirement.py script and wait for it to finish
    # gitana_envirement()
    # Continue with the rest of the code
    # count_tables(repository_dir)
    update_summary_all(repository_dir)
    create_data()
    analyze_all()
    analyze_correlation()
    analyze_multi()
    print("finish")
if __name__ == '__main__':
    main()
