#! /usr/bin/env python3
#from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from seleniumwire import webdriver

def open_website():
    # Create a new browser instance
    browser = webdriver.Chrome()

    # Open the website
    browser.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=ASKXGp3UMk4fMEAviIzGVzC-lNS7wM2JwfFCLO6sC4NH1Nn7iUaf7XAGd7Vhi5sbChZT8WTjE_7v6A&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1257304344%3A1701982820617281&theme=glif")

    # Wait for the page to load
    time.sleep(2)  

    # username_input = webdriver.find_element(By.XPATH, '//input[@type="email"]')
    username_input = browser.find_element(By.XPATH, '//input[@name="identifier"]')

    time.sleep(2)
    # Вставляем логин в поле ввода
    username_input.send_keys("dispatch.kimpho@gmail.com")
    # for letter in "dispatch.kimpho@gmail.com":
    #     username_input.send_keys(letter)
    #     time.sleep(0.2)

    time.sleep(5)
    #push "next" button
    next_button = browser.find_element(By.XPATH, '//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]')
    time.sleep(2)
     # Click the next button
    next_button.click()
    time.sleep(20)
    # Close the browser
    browser.close()

if __name__ == "__main__":
    open_website()