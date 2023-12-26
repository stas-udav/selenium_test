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
    
    time.sleep(0.5) 
# Checking behavior after unselected checkbox 1 by 1
    
    #Reciving checkbox status 
       
        # Create the XPath selector
    check_box_values = get_checkbox_value(driver)         
             
    for value in check_box_values:
        
        xpath_selector = f"//span[contains(text(), {value})]/preceding-sibling::span[(@class='rct-node-icon')]/preceding-sibling::span/*"
        # Find the elements
        # elements = driver.find_elements(By.XPATH, xpath_selector)
        print(xpath_selector)
       
        #Select the checkbox from the bottom to the top
    # for box in range(len(checkbox_list) - 1, -1, -1):      
    #     driver.execute_script("arguments[0].click();", checkbox_list[box]) #click on checkbox
    #     checkbox_list_after_click = driver.find_elements(By.XPATH, '//span[contains(text(), "Home")]/preceding-sibling::span[(@class="rct-node-icon")]/preceding-sibling::span/*') 
    #     amount_of_selected_checkboxes_on_the_page = len(checkbox_list_after_click)
    #     print(amount_of_selected_checkboxes_on_the_page)
    #     checkbox_select_dict ={} #add all selected checbox in dict
    #     for checkbox in checkbox_list_after_click:
    #         if checkbox.is_displayed():
    #             checkbox_select_dict[amount_of_selected_checkboxes_on_the_page] = "Selected"
    #             print(checkbox_select_dict)
    #         else:
    #             print("Unselected")         
    # # for checkbox in checkbox_list:
    # #     icon = checkbox.find_element(By.XPATH, './span[@class="rct-icon"]')
    # #     if icon.get_attribute("class") == ".rct-icon.rct-icon-check":
    # #         print(f"Checkbox '{checkbox.text}' is selected")
    # #     else:
    # #         print(f"Checkbox '{checkbox.text}' is not selected")
    #     # compare green checkbox and selected
        
    #     # get_checkbox_name = get_green_ckeckbox_values(driver)
    #     # print(get_checkbox_name, after_click_checbox)
    #     time.sleep(0.5)
    #     driver.execute_script("arguments[0].click();", checkbox_list[box]) #click on checkbox for unselect  
    # time.sleep(2)
    
   
    time.sleep(5)


open_website()