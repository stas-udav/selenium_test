#! /usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def open_website():
        # Create a new browser instance
    driver = webdriver.Chrome()    
       # Fullscrin browser
    driver.maximize_window()
    # Open the website
    driver.get("https://demoqa.com/checkbox")
        # Wait for the page to load
    time.sleep(2)  

        #Checking checkbox
    checkbox = driver.find_element(By.XPATH, '//span[@class="rct-checkbox"]') #loocking for checkbox
    checkbox_staus = checkbox.get_attribute("checked") 
    time.sleep(2)
    if checkbox_staus == "true":
        print("checkbox is active")
    else :
        print("checkbox is not active")
    time.sleep(3)

    expand_all = driver.find_element(By.XPATH, '//button[@aria-label="Expand all"]')
    expand_all.click()

    checkbox_list = driver.find_elements(By.XPATH, '//span[@class="rct-checkbox"]')
    amount_of_checkboxes_on_the_page = len(checkbox_list)
    print(amount_of_checkboxes_on_the_page)
    # time.sleep(2)

    check_box_names = driver.find_elements(By.XPATH, '//span[@class="rct-title"]')
    check_box_values = []
    for checkbox in check_box_names:
        check_box_name = checkbox.text # Get the text of the element
        check_box_values.append(check_box_name) #add text from checkbox to the list 
    print(check_box_values)
     # Print each checkbox name in a separate line
    for checkbox_name in check_box_values:
        print(checkbox_name)        
    time.sleep(2)

    #turn on all checkboxes and compera to previos checkbox varible 
    main_checkbox = checkbox_list[0] #looking for 1 checkbox in list
    main_checkbox.click() #click on main checkbox for marcking all checkboxes
    time.sleep(2)

    green_list = driver.find_elements(By.XPATH, '//span[@class="text-success"]')
    green_list_length = len(green_list)
    print(green_list_length)
    green_checked_values = []
    for green_value in green_list:
        green_name = green_value.text
        green_checked_values.append(green_name)
    print(green_checked_values)

    if amount_of_checkboxes_on_the_page == green_list_length:
        print("Amount of elements before active state and after is equal")
    else:
        print("Пиздец товарищи...")

    if check_box_values == green_checked_values:
        print("Zaebca")
    else:
        print("Pizdec")

    driver.close()


if __name__ == "__main__":
    open_website()