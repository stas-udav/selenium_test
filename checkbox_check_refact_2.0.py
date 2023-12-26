#! /usr/bin/env python3
from checkbox_finctions import *

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

    #Checking if 1th checkbox is selected on loaded page
checkbox_staus_Home = get_checkbox_selector_status(driver, "Home")
if checkbox_staus_Home == "rct-icon rct-icon-uncheck":
    print("Unselected")
else:
    print("Selected")

expand_all = driver.find_element(By.XPATH, '//button[@aria-label="Expand all"]') #expand all checbox tree
expand_all.click()

amount_of_checkboxes_on_the_page, checkbox_list = get_checkbox_value(driver) 
print(amount_of_checkboxes_on_the_page)
time.sleep(1)
    
get_checkbox_elemen(driver, "Home").click() # turn on all checkboxes
time.sleep(1)

# Checking Amount of elements before the active state and after (should be equal)
green_list_length, green_checkbox_list = get_green_ckeckbox_values(driver)
if amount_of_checkboxes_on_the_page == green_list_length:
    print("Amount of elements before active state and after is equal")
else:
    print("Пиздец товарищи...")

get_checkbox_elemen(driver, "Home").click() #unselect all checkboxes by clicking on the main checkbox
time.sleep(1)

    # Comparing the original checkbox and green checkbox value(Checkbox names)
comparing_values = {} # creating dict with original checkbox = key and green checkbox = value(receiving from function green_checked_values)
not_aligned_values = []
report_dict = {}  # dict for writing in json where key = checkbox name, value =   (boolean, green checkbox)

for index, value in enumerate(checkbox_list): #Adding pairs of a selected checkbox and a green checkbox (should be the same)
    comparing_values[value] = green_checkbox_list[index]
# Comparing the original checkbox (key) to the green checkbox (value)
for checkbox_original, gren_checkbox in comparing_values.items(): 
    if checkbox_original != gren_checkbox:
        not_aligned_values.append(gren_checkbox)
for index, original_checkbox in enumerate(checkbox_list): 
        green_checkbox = green_checkbox_list[index]
        report_dict[original_checkbox] = [original_checkbox == green_checkbox, green_checkbox]
time.sleep(1)

report_json(driver, "checkbox_errors_on_turn_on.json", report_dict) #Saving report of not aligned checkbox names