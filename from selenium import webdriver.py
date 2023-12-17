from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def open_website():
    # Create a new browser instance
    driver = webdriver.Chrome()
    # Full screen browser
    driver.maximize_window()
    # Open the website
    driver.get("https://demoqa.com/checkbox")
    # Wait for the page to load
    time.sleep(2)

    home_checkbox = driver.find_element(By.XPATH, '//span[@class="rct-checkbox"]')
    home_checkbox.click()
    time.sleep(1)
    expand_all = driver.find_element(By.XPATH, '//button[@aria-label="Expand all"]')
    expand_all.click()
    time.sleep(1)

    checkbox_list = driver.find_elements(By.XPATH, '//span[@class="rct-title"]')
    amount_of_checkboxes_on_the_page = len(checkbox_list)

    checkbox_names = []
    for element in checkbox_list:
        checkbox_names.append(element.text)
    print(checkbox_names)

    checkboxes_dict = {}
    for index, element in enumerate(checkbox_names):
        checkboxes_dict[element] = checkbox_list[index]

    for value in checkboxes_dict.values():
        value.click()
        time.sleep(1)


open_website()