#! /usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from checkbox_finctions import *
import time
import json


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
        print("page loading error")
    time.sleep(1)

    expand_all = driver.find_element(By.XPATH, '//button[@aria-label="Expand all"]') #expand all checbox tree
    expand_all.click()
    checkbox_list = driver.find_elements(By.XPATH, '//span[@class="rct-checkbox"]')
    time.sleep(1)

    # turn on all checkboxes
    main_checkbox = checkbox_list[0] #looking for 1 checkbox in list
    main_checkbox.click() #click on the main checkbox to mark all checkboxes
    time.sleep(2)

    # Downloads = driver.find_element(By.XPATH,'//span[@class="rct-title" and text()="Downloads"]')
    # Downloads.click()
    

    element, xpath_selector = get_checkbox_elemen(driver, "Documents")
    print(xpath_selector)
    time.sleep(3)
if __name__ == "__main__":
    open_website()