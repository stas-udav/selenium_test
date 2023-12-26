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
    # checking if checkbox selected correctly 
    
def get_checkbox_status(driver):
    # reciving checkbox status after second click 
    check_box_values_after_click = get_checkbox_value()
    green_checked_values_after_click = get_green_ckeckbox_values()[0]

    if check_box_values_after_click == green_checked_values:
        return "Zaebca"
    else:
        return "Pizdec"
  
def get_checkbox_selector_status(driver, value):
    checbox_len, check_box_values = get_checkbox_value(driver)    
    xpath_selector = f"//span[contains(text(), {value})]/preceding-sibling::span[(@class='rct-node-icon')]/preceding-sibling::span/*"
    element = driver.find_element(By.XPATH, xpath_selector)
    class_string = element.get_attribute("class")
    return(class_string)
    # print(class_string)
    # print(xpath_selector)
    # if "rct-icon-check" in class_string:
    #     print(True)
    # elif "rct-icon-uncheck":
    #     print(False)
    # else: 
    #     print("Not a checkbox_status")

def get_checkbox_elemen(driver, value): #getting checkbox element and xpath
    xpath_selector = f"//span[contains(text(), {value})]/preceding-sibling::span[(@class='rct-node-icon')]/preceding-sibling::span/*"
        #Find the elements
    element = driver.find_element(By.XPATH, xpath_selector)       
    return(element)
    # return checkbox_list

def report_json(driver, path, report_dict):
    with open(path,"w") as json_file:
        json.dump(report_dict, json_file)
    time.sleep(2)
