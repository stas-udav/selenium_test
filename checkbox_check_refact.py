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

            #Checking if 1th checkbox is selected on loaded page
    checkbox = driver.find_element(By.XPATH, '//span[@class="rct-checkbox"]') #loocking for checkbox
    checkbox_staus = checkbox.get_attribute("checked") 
    
    if checkbox_staus == "true":
        print("checkbox is active")
    else :
        print("checkbox is not active")

    time.sleep(2)

    expand_all = driver.find_element(By.XPATH, '//button[@aria-label="Expand all"]') #expand all checbox tree
    expand_all.click()

    checkbox_list = driver.find_elements(By.XPATH, '//span[@class="rct-checkbox"]') 
    amount_of_checkboxes_on_the_page = len(checkbox_list) #checking amount of checkboxex
    print(amount_of_checkboxes_on_the_page)
    check_box_values = get_checkbox_value(driver)
    print(check_box_values)       
    
        # turn on all checkboxes and compare to previos checkbox varible 
    main_checkbox = checkbox_list[0] #looking for 1 checkbox in list
    main_checkbox.click() #click on main checkbox for marcking all checkboxes
    
    time.sleep(2)

        # Checking Amount of elements before active state and after (should be equal)
    green_checked_values, green_list_length = get_green_ckeckbox_values(driver) # getting from toople(recived in function) first value wich is checbox names on the bottom
    print(green_checked_values)
    if amount_of_checkboxes_on_the_page == green_list_length:
        print("Amount of elements before active state and after is equal")
    else:
        print("Пиздец товарищи...")

    main_checkbox.click() #unselect all checkbox by clicking on main checkbox
    time.sleep(2)

        # comparing oridginal checkbox and green checbox value
    comparing_values = {} # creating dict w original checkbox = key and green checkbox = value(reciving from funtion green_checked_values)
    not_aligned_values = []
    report_dict = {}  # dict for wrighting in json where key = ckeckbox name, value =   (boolean, green checkbox)

    for index, value in enumerate(check_box_values): 
        comparing_values[value] = green_checked_values[index]
        
    print(comparing_values)
        #comparing original checkbox = key and green checkbox = value
    for checkbox_original, gren_checkbox in comparing_values.items(): 
        if checkbox_original != gren_checkbox:
           not_aligned_values.append(gren_checkbox)
    # print (not_aligned_values)
    for index, original_checkbox in enumerate(check_box_values): 
        green_checkbox = green_checked_values[index]
        report_dict[original_checkbox] = [original_checkbox == green_checkbox, green_checkbox]

    print(report_dict)
     
        # Checking status of working checkbox for each checkbox
    for box in range(len(checkbox_list)):      
        driver.execute_script("arguments[0].click();", checkbox_list[box]) #click on checkbox
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", checkbox_list[box]) #click on checkbox for unselect    

    time.sleep(2)

        # Saving error checkbox names in json
    file_path = "checkbox_errors_on_turn_on.json"
    with open(file_path,"w") as json_file:
        json.dump(report_dict, json_file)
    time.sleep(2)
if __name__ == "__main__":
    open_website()