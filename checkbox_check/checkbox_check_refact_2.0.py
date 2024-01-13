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
print(checkbox_staus_Home)

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
time.sleep(0.5)

    # Comparing the original checkbox and green checkbox value(Checkbox names)
comparing_values, not_aligned_values, report_dict = comparing_selected_selectors(driver,checkbox_list, green_checkbox_list)
time.sleep(0.5)

report_json(driver, "checkbox_errors_on_turn_on.json", report_dict) #Saving report of not aligned checkbox names
time.sleep(0.5)

    # Unselecting main selectors in a category and checking if it does not affect other selected checkboxes
get_checkbox_elemen(driver, "Home").click() # turn on all checkboxes

time.sleep(0.5)
 # Scroll down 
driver.execute_script("window.scrollTo(0, 200);")
time.sleep(0.5)

# Checking if unselecting a checkbox affects other checkboxes
Selectors = ["Downloads", "Office", "WorkSpace", "Desktop"]
green_selectors = ["downloads", "office", "workspace", "desktop"]
check_box_errors_turn_off_checked = {} 
check_box_errors_turn_off_green_notifications = {}
for selector, green_selector in zip(Selectors, green_selectors) :    
    checkbox_statuses_before = get_selectors_status(driver, Selectors) #Get checkbox status before click  
    _, checkbox_green_statuses_before = get_green_ckeckbox_values(driver)

    get_checkbox_elemen(driver, selector).click()
    time.sleep(0.5)
    checkbox_statuses_after = get_selectors_status(driver,Selectors) #Get checkbox status after click  
    _, checkbox_green_statuses_after = get_green_ckeckbox_values(driver)
    #checking if some green checkboxes affected
    affected_green = set(checkbox_green_statuses_before) - set(checkbox_green_statuses_after) - {green_selector}
    check_box_errors_turn_off_green_notifications[selector] = list(affected_green)
    #checking if some checkboxes affected
    affected_selectors = []
    for key in checkbox_statuses_before.keys(): #checking if some checkboxes affected
        if key != selector:            
            if checkbox_statuses_before[key] != checkbox_statuses_after[key]:
                print(f"Checkbox status for {key} changed after clicking on {selector}")
                affected_selectors.append(key)
                check_box_errors_turn_off_checked[selector] = affected_selectors
report_json(driver, "check_box_errors_turn_off_checked.json", check_box_errors_turn_off_checked)
    # time.sleep(1)
report_json(driver, "check_box_errors_turn_off_green_notifications.json", check_box_errors_turn_off_green_notifications)
time.sleep(1)
