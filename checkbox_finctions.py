#! /usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

    # getting all checkbox name on page 
def get_checkbox_value(driver):
    check_box_names = driver.find_elements(By.XPATH, '//span[@class="rct-title"]')
    check_box_values = []
    for checkbox in check_box_names:
        check_box_name = checkbox.text # Get the text of the element
        check_box_values.append(check_box_name) #add text from checkbox to the list 
    return (check_box_values)

    # Getting checkbox selected status check on the bottom of the page(marked green color)
def get_green_ckeckbox_values(driver):
    green_list = driver.find_elements(By.XPATH, '//span[@class="text-success"]')
    green_list_length = len(green_list)
    # print(green_list_length)
    green_checked_values = []
    for green_value in green_list:
        green_name = green_value.text
        green_checked_values.append(green_name)
    return(green_checked_values, green_list_length)
    # checking if checkbox selected correctly 

    
def get_checkbox_status(driver):
    # Получаем значения после второго клика
    check_box_values_after_click = get_checkbox_value()
    green_checked_values_after_click = get_green_ckeckbox_values()[0]

    if check_box_values_after_click == green_checked_values:
        return "Zaebca"
    else:
        return "Pizdec"