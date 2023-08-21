from GitHub_API.search_dbml import main as search_dbml
from GitHub_API.extract_dbml import main as extract_dbml
from dbdiagram.xml_dbml import main as xml_dbml
from dbdiagram.automate_dbdiagram_and_upload import main as automate_dbdiagram_and_upload
from data_analyze.count_tables import main as count_tables

access_token = "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"
repository_dir = "repositories"
def main():
    search_dbml(access_token)
    extract_dbml(access_token)
    xml_dbml(repository_dir)
    automate_dbdiagram_and_upload(repository_dir)
    count_tables(repository_dir)    
if __name__ == '__main__':
    main()
