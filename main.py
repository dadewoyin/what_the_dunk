import os
import sys
import six
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

NIKE_URL = "https://www.nike.com/launch/t/react-element-87-moss/"

def start():
  browser = webdriver.Chrome("./bin/chromedriver_mac")
  browser.get(NIKE_URL)
  delay = 1  # seconds

  try:
    element_present = EC.presence_of_element_located(
        (By.XPATH, '//button[text()="M 11 / W 12.5"]'))
    element = WebDriverWait(browser, delay).until(element_present)
    element.click()
    print("We got the element!", element)
    time.sleep(60)

  except TimeoutException:
    print("Timed out waiting for page to load")

if __name__ == "__main__":
  start()
