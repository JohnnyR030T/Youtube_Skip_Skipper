# Import dependencies...
from selenium import webdriver
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Make sure you have the correct driver for the browser... In this case Chrome.
# https://selenium-python.readthedocs.io/installation.html

# Goes to the Youtube Channel specified here...
url = 'https://www.youtube.com/channel/UC09GemGjss3hPdljwtJ8TPA'
browser = webdriver.Chrome()
browser.get(url)
# Clicks on the Youtube video specified here by xpath
browser.find_element_by_xpath('//*[@id="thumbnail"]').click()

# Uses seleniums explicit WebDriverWait method to wait for skip button to be clickable...
wait = WebDriverWait(browser, 20*60)
element = wait.until(EC.element_to_be_clickable(
    # Because Integer changes for the skip button I had to list multiple choices here...
    (By.XPATH, "//*[@id='skip-button:6']/span/button") or (By.XPATH, "//*[@id='skip-button:5']/span/button") or (By.XPATH, "//*[@id='skip-button:4']/span/button") or (By.XPATH, "//*[@id='skip-button:3']/span/button") or (By.XPATH, "//*[@id='skip-button:2']/span/button") or (By.XPATH, "//*[@id='skip-button:1']/span/button")))
element.click()
