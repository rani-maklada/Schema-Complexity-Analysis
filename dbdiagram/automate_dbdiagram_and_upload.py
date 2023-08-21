import os
import time
import tempfile
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def screenshot_element(driver, css_selector, filename):
    """Capture a screenshot of a specific element on the page."""
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    element.screenshot(filename)

def automate_dbdiagram_and_upload(dbml_file_path):
    service_obj = Service("/Users/rani/Documents/chromedriver")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=service_obj, options=chrome_options)

    try:
        print(f"\nOpening dbdiagram.io for file: {dbml_file_path}")
        driver.get('https://dbdiagram.io/d')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'editor-container')))
        print("Editor loaded.")

        editor_container = driver.find_element(By.ID, 'editor-container')
        editor = WebDriverWait(editor_container, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'editor')))
        actions = ActionChains(driver)
        actions.click(editor).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
        print("Editor cleared.")
        time.sleep(5)

        import_button = driver.find_element(By.ID, 'import-btn')
        import_button.click()
        print("Clicked 'Import' button.")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'import-postgres-btn')))
        postgres_button = driver.find_element(By.ID, 'import-postgres-btn')
        postgres_button.click()
        print("Selected 'Import from PostgreSQL' option.")

        sql_output = convert_dbml_to_sql(dbml_file_path, "postgres")
        temp_sql_filename = create_temp_sql_file(sql_output)
        print(f"Saved SQL to temporary file: {temp_sql_filename}")

        upload_sql_input = driver.find_element(By.ID, 'sql_upload')
        upload_sql_input.send_keys(temp_sql_filename)
        print("Uploaded SQL file.")

        submit_button = driver.find_element(By.ID, 'import-submit-btn')
        submit_button.click()
        print("Clicked 'Submit' button.")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'diagram')))
        time.sleep(5)

        script = "document.getElementById('editor-container').style.width = '6px';"
        driver.execute_script(script)
        time.sleep(1)

        folder_path, dbml_filename = os.path.split(dbml_file_path)
        base_filename, _ = os.path.splitext(dbml_filename)

        diagram_screenshot_filename = os.path.join(folder_path, base_filename + '_diagram.png')
        screenshot_element(driver, '.diagram-container.flex-1', diagram_screenshot_filename)
        print(f"Screenshot of the entire diagram saved as {diagram_screenshot_filename}")

    except Exception as e:
        print(f"Error occurred for {dbml_file_path}: {e}")
    finally:
        driver.quit()
        print(f"Finished processing for {dbml_file_path}")

def convert_dbml_to_sql(dbml_filename, target_db):
    dbml2sql_path = "/Users/rani/AppData/Roaming/npm/dbml2sql.cmd"
    command = [dbml2sql_path, dbml_filename, f"--{target_db}"]
    try:
        sql_output = subprocess.check_output(command, text=True)
        print("SQL generation successful.")
        return sql_output
    except subprocess.CalledProcessError as e:
        print("Error during SQL generation:", e)
        return None

def create_temp_sql_file(sql_output):
    try:
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.sql') as temp_sql_file:
            temp_sql_file.write(sql_output)
        return temp_sql_file.name
    except Exception as e:
        print("Error creating temporary SQL file:", e)
        return None

def main(directory_path):
    print(f"Processing repository directory: {directory_path}\n")
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.dbml'):
                dbml_file_path = os.path.join(root, file)
                automate_dbdiagram_and_upload(dbml_file_path)

if __name__ == "__main__":
    repository_dir = "sample"
    main(repository_dir)
