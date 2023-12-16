#! /usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from checkbox_finctions import *
import time

def open_website():
        # Create a new browser instance
    driver = webdriver.Chrome()    
    driver.maximize_window() # Fullscrin browser       
    driver.get("https://demoqa.com/checkbox") # Open the website  

        # Waiting for the page to load
    try:
        wait = WebDriverWait(driver, 10) 
        wait.until(lambda driver: driver.find_element(By.XPATH, '//span[@class="rct-title"]'))  # Wait for the page to load
    except TimeoutException:
        print("Сpage loading error")

            #Checking if 1 checkbox is selected on loaded page
    checkbox = driver.find_element(By.XPATH, '//span[@class="rct-checkbox"]') #loocking for checkbox
    checkbox_staus = checkbox.get_attribute("checked") 
    time.sleep(2)
    if checkbox_staus == "true":
        print("checkbox is active")
    else :
        print("checkbox is not active")
    time.sleep(2)

    expand_all = driver.find_element(By.XPATH, '//button[@aria-label="Expand all"]') #expand all checbox tree
    expand_all.click()

    checkbox_list = driver.find_elements(By.XPATH, '//span[@class="rct-checkbox"]')
    amount_of_checkboxes_on_the_page = len(checkbox_list)
    print(amount_of_checkboxes_on_the_page)
    # time.sleep(2)
    check_box_values = get_checkbox_value(driver)
    print(check_box_values)
       
    time.sleep(2)
if __name__ == "__main__":
    open_website()