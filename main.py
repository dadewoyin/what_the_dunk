import os
import sys
import six
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

NIKE_URL = "https://www.nike.com/launch/t/react-element-87-moss/"
browser = webdriver.Chrome("./bin/chromedriver_mac")
delay = 3  # seconds


def start():
  browser.get(NIKE_URL)

  try:
    selectSize()
    addItemToCart()
    goToCheckout()

  except TimeoutException:
    print("Timed out waiting for page to load")

def selectSize():
  size_element = EC.presence_of_element_located(
    (By.XPATH, '//button[text()="M 11 / W 12.5"]'))
  element = WebDriverWait(browser, delay).until(size_element)
  element.click()  # select size

def addItemToCart():
  add_to_cart_button = browser.find_element_by_xpath(
      '//button[text()="ADD TO CART"]')
  action = ActionChains(browser)
  action.move_to_element(add_to_cart_button).perform()
  add_to_cart = WebDriverWait(browser, delay).until(
      EC.element_to_be_clickable((By.XPATH, '//button[text()="ADD TO CART"]')))
  add_to_cart.click()

def goToCheckout():
  checkout_button = WebDriverWait(browser, delay).until(
      EC.element_to_be_clickable((By.XPATH, '//a[text()="Checkout"]')))
  checkout_button.click()



if __name__ == "__main__":
  start()
