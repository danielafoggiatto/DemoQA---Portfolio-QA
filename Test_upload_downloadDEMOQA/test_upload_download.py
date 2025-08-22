from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def test_upload_download(driver):
   
    driver.get("https://demoqa.com/upload-download")

    file_path = r"C:\Users\danie\Desktop\TestFile.txt" 
    upload_input = driver.find_element(By.ID, "uploadFile")
    upload_input.send_keys(file_path)

    uploaded_file_name = driver.find_element(By.ID, "uploadedFilePath").text
    assert "TestFile.txt" in uploaded_file_name

    download_btn = driver.find_element(By.ID, "downloadButton")
    download_btn.click()

    download_path = r"C:\Users\danie\Downloads\TestFiles\sampleFile.jpeg"
    WebDriverWait(driver, 10).until(lambda d: os.path.exists(download_path))
    assert os.path.exists(download_path)
