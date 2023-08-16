import xml.etree.ElementTree as ET
import os

brackets_to_remove = "[]{}()"

def convert_dbml(xml_content):
    # Remove BOM if present
    if xml_content.startswith('\ufeff'):
        xml_content = xml_content[1:]

    # Parsing the XML content
    root = ET.fromstring(xml_content)

    # Defining the namespace
    namespace = {"dbml": "http://schemas.microsoft.com/linqtosql/dbml/2007"}

    # Extracting table and column details considering the namespace
    tables = []

    for table in root.findall("dbml:Table", namespace):
        table_name = table.attrib.get("Name", "Unknown")
        table_name = ''.join(c for c in table_name if c not in '[]{}()')
        columns = []
    
        for column in table.findall("dbml:Type/dbml:Column", namespace):
            column_name = column.attrib.get("Name", "Unknown")
            column_type = column.attrib["Type"].split('.')[-1]  # Extracting the type after the last dot
            column_details = {"name": column_name, "type": column_type}
        
            # Checking for primary key
            if column.attrib.get("IsPrimaryKey", "false") == "true":
                column_details["is_primary_key"] = True
        
            columns.append(column_details)
    
        tables.append({"name": table_name, "columns": columns})

    # Generating DBML formatted content from the extracted details
    dbml_content = ""

    for table in tables:
        dbml_content += f"Table {table['name']} {{\n"
        for column in table['columns']:
            column_name = column['name'].strip("[]")
            dbml_content += f"  {column_name} {column['type']}"
            if column.get('is_primary_key', False):
                dbml_content += " [primary key]"
            dbml_content += "\n"
        dbml_content += "}\n\n"

    return dbml_content

def process_repository_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.dbml'):
                dbml_file_path = os.path.join(root, file)
                
                # Read the content of the XML file
                with open(dbml_file_path, "r", encoding="utf-8-sig") as xml_file:
                    xml_content = xml_file.read()

                try:
                    # Convert the DBML XML content
                    dbml_content = convert_dbml(xml_content)
                    
                    # Write the converted content to a new DBML file in the same directory
                    output_path = os.path.splitext(dbml_file_path)[0] + ".dbml"
                    with open(output_path, "w") as dbml_file:
                        dbml_file.write(dbml_content)
                    
                    print(f"Converted and saved {dbml_file_path}")
                except ET.ParseError:
                    print(f"Skipping {dbml_file_path} as it is not valid XML")

if __name__ == "__main__":
    repository_dir = "repositories"
    process_repository_directory(repository_dir)