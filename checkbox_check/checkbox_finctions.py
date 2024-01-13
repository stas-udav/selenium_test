#! /usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time
import json
    # getting all checkbox name on page 
def get_checkbox_value(driver):
    check_box_names = driver.find_elements(By.XPATH, '//span[@class="rct-title"]')
    check_box_values = []
    list_length = len(check_box_names)
    for checkbox in check_box_names:
        check_box_name = checkbox.text # Get the text of the element
        check_box_values.append(check_box_name) #add text from checkbox to the list 
    return (list_length, check_box_values)

    # Getting checkbox selected status check on the bottom of the page(marked green color)
def get_green_ckeckbox_values(driver):
    green_list = driver.find_elements(By.XPATH, '//span[@class="text-success"]')
    green_list_length = len(green_list)
    # print(green_list_length)
    green_checked_values = []
    for green_value in green_list:
        green_name = green_value.text
        green_checked_values.append(green_name)
    return(green_list_length, green_checked_values)
    
def get_checkbox_selector_status(driver, value):
    # checbox_len, check_box_values = get_checkbox_value(driver)    
    xpath_selector = f"//span[contains(text(), '{value}')]/preceding-sibling::span[(@class='rct-node-icon')]/preceding-sibling::span/*"
    element = driver.find_element(By.XPATH, xpath_selector)
    class_string = element.get_attribute("class")    
    # print(class_string)
    # print(xpath_selector)
    if "rct-icon rct-icon-check" in class_string:
        status = "Selected"
    elif "rct-icon rct-icon-uncheck":
         status = "Unselected"
    else: 
        print("Not a checkbox_status")
    return(value, class_string, status)

# getting dict of selectors status key = selector, value = status(selected/unselected)
def get_selectors_status(driver, selectors_list): 
    selectors_status_dict = {}
    for selector in selectors_list:
        selector, class_string, selector_status = get_checkbox_selector_status(driver, selector)
        if selector_status == "Selected":
            selectors_status_dict[selector] = "Selected"
        else :
            selectors_status_dict[selector] = "Unselected"
    return selectors_status_dict

# getting checkbox element and xpath
def get_checkbox_elemen(driver, value): 
    xpath_selector = f"//span[contains(text(), '{value}')]/preceding-sibling::span[(@class='rct-node-icon')]/preceding-sibling::span/*"
    # Find the elements
    element = driver.find_element(By.XPATH, xpath_selector) 
    # print(xpath_selector)
    return(element)
    
def report_json(driver, path, report_dict):
    # getting data and time when report will be created
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    new_filename = f"{now}_{path}"
    with open(new_filename,"w") as json_file:
        json.dump(report_dict, json_file)
    time.sleep(2)

# Comparing the original green checkbox value(Checkbox names)
def comparing_selected_selectors(driver, checkbox_list, green_checkbox_list):
    comparing_values = {} # creating dict with original checkbox = key and green checkbox = value(receiving from function green_checked_values)
    not_aligned_values = []
    report_dict = {}  # dict for writing in json where key = checkbox name, value =   (boolean, green checkbox)
       
    for index, value in enumerate(checkbox_list): # Adding pairs of a selected checkbox and a green checkbox (should be the same)
        comparing_values[value] = green_checkbox_list[index]

    # Comparing the original checkbox (key) to the green checkbox (value)
    for checkbox_original, gren_checkbox in comparing_values.items(): 
        if checkbox_original != gren_checkbox:
            not_aligned_values.append(gren_checkbox)
    for index, original_checkbox in enumerate(checkbox_list): # getting index od checkbox_list and original_checkbox
        green_checkbox = green_checkbox_list[index] # getting green_checkbox with same index like in checkbox_list
        report_dict[original_checkbox] = [original_checkbox == green_checkbox, green_checkbox]
    return(comparing_values, not_aligned_values, report_dict)

       