#! /usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def open_website():
    chrome_path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chrome.exe'  # Укажите свой путь к Chrome
    chrome_driver_path = r'C:\QA\chromedriver.exe'  # Укажите свой путь к chromedriver.exe

    options = webdriver.ChromeOptions()
    options.binary_location = chrome_path
    options.add_argument('--disable-gpu')
    options.add_argument(f'--webdriver-path={chrome_driver_path}')  # Замените executable_path на эту опцию

    browser = webdriver.Chrome(options=options)

    try:
        browser.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=ASKXGp3UMk4fMEAviIzGVzC-lNS7wM2JwfFCLO6sC4NH1Nn7iUaf7XAGd7Vhi5sbChZT8WTjE_7v6A&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1257304344%3A1701982820617281&theme=glif")

        time.sleep(2)

        username_input = browser.find_element(By.XPATH, '//input[@name="identifier"]')
        username_input.send_keys("dispatch.kimpho@gmail.com")

        time.sleep(2)

        next_button = browser.find_element(By.XPATH, '//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]')
        time.sleep(2)
        next_button.click()
        time.sleep(5)
    finally:
        browser.quit()

if __name__ == "__main__":
    open_website()
