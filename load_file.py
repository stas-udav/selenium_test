#! /usr/bin/env python3

from selenium.webdriver.common.by import By
import time
from selenium import webdriver

def open_website():
        # Create a new browser instance
    driver = webdriver.Chrome()
        # Fullscrin browser
    driver.maximize_window()
    # Open the website
    driver.get("https://demoqa.com/automation-practice-form")

        # Wait for the page to load
    time.sleep(2)  
    
        #open side bar element
    side_bar_list = driver.find_elements(By.XPATH, '//span[@class="group-header"]')
    #driver.execute_script("arguments[0].click();",upload_button) #javascipt click button all time
    #print(f"THIS IS LENTH OF THE LIST{len(side_bar_list)}")
    elements_button = side_bar_list[0]
    elements_button.click()
    time.sleep(3)

        # Scroll down 
    driver.execute_script("window.scrollTo(0, 500);")
        #click on Upload and download
    upload_download_button = driver.find_element(By.XPATH, '//span[@class="text" and contains(text(), "Upload and Download")]')
    time.sleep(2)  
    upload_download_button.click()
    time.sleep(3)

        #uploading file
    upload_file = driver.find_element(By.XPATH, '//input[@id = "uploadFile"]')
    upload_file.send_keys("C:/Users/stanh/Desktop/sampleFile.jpeg") #can't just click on button selenium do not supporting click on inpud button
    time.sleep(3)
    uploaded_file_path = driver.find_element(By.XPATH, '//input[@id="uploadFile"]').get_attribute("value")
    my_file_paths = []
    my_file_paths.append(uploaded_file_path)
    print(my_file_paths)
    
    # write path of added file in to a txt
    with open ("C:/QA/selenium_test/txt_files/my_file_paths.txt", "w") as file:
        # Convert the list to a string
        list_string = ",".join(my_file_paths)
        file.write(list_string)

    return my_file_paths
    
    
    

if __name__ == "__main__":
    open_website()