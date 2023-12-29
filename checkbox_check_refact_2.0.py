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
comparing_values, not_aligned_values, report_dict = comparing_selected_selectors(driver,checkbox_list, green_checkbox_list)
time.sleep(1)

report_json(driver, "checkbox_errors_on_turn_on.json", report_dict) #Saving report of not aligned checkbox names
time.sleep(1)

    # Unselecting main selectors in a category and checking if it does not affect other selected checkboxes
get_checkbox_elemen(driver, "Home").click() # turn on all checkboxes

time.sleep(1)
 # Scroll down 
driver.execute_script("window.scrollTo(0, 200);")
time.sleep(1)

Selectors = ["'Downloads'", "'Office'", "'WorkSpace'", "'Desktop'"]
get_affected_checkboxes(driver, Selectors)

time.sleep(1)
