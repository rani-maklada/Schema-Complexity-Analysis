from GitHub_API.search_dbml import main as search_dbml
from GitHub_API.extract_dbml import main as extract_dbml
from dbdiagram.xml_dbml import main as xml_dbml
from dbdiagram.automate_dbdiagram_and_upload import main as automate_dbdiagram_and_upload
from data_analyze.count_tables import main as count_tables

def run_all():
    search_dbml()
    extract_dbml()
    xml_dbml()
    automate_dbdiagram_and_upload()
    count_tables()    
if __name__ == '__main__':
    run_all()
