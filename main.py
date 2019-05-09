import os
import sys
import six
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

NIKE_URL = "https://www.nike.com/launch/t/air-max-97-haven-clot-white-sail/"
delay = 3  # seconds

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-web-security")
browser = webdriver.Chrome("./bin/chromedriver_mac", chrome_options=chrome_options)
action = ActionChains(browser)

def start():
  browser.get(NIKE_URL)

  try:
    selectSize()
    addItemToCart()
    goToCheckout()
    # time.sleep(3)
    # login()
    checkoutAsGuest()
    fillOutShippingForm()
    fillOutPaymentInfo()
    # SubmitOrder()

  except TimeoutException:
    print("Timed out waiting for page to load")

def selectSize():
  size_element = EC.element_to_be_clickable(
    (By.XPATH, '//button[text()="M 11 / W 12.5"]'))
  element = WebDriverWait(browser, delay).until(size_element)
  element.click()  # select size

def addItemToCart():
  add_to_cart_button = browser.find_element_by_xpath(
      '//button[text()="ADD TO CART"]')
  action.move_to_element(add_to_cart_button).perform()
  add_to_cart = WebDriverWait(browser, delay).until(
      EC.element_to_be_clickable((By.XPATH, '//button[text()="ADD TO CART"]')))
  time.sleep(1)
  add_to_cart.click()

def goToCheckout():
  checkout_button = WebDriverWait(browser, delay).until(
      EC.element_to_be_clickable((By.XPATH, '//a[text()="Checkout"]')))
  checkout_button.click()

def checkoutAsGuest():
    checkout = WebDriverWait(browser, delay).until(
        EC.element_to_be_clickable((By.ID, 'qa-guest-checkout')))
    checkout.click()

def fillOutShippingForm():
  first_name = WebDriverWait(browser, delay).until(
    EC.presence_of_element_located((By.ID, 'firstName')))
  first_name.send_keys('David')

  password_input = WebDriverWait(browser, delay).until(
    EC.presence_of_element_located((By.ID, 'lastName')))
  password_input.send_keys('Adewoyin')

  address_1 = WebDriverWait(browser, delay).until(
      EC.presence_of_element_located((By.ID, 'address1')))
  address_1.send_keys('2590 Briggs Avenue')

  expand_line_2 = WebDriverWait(browser, delay).until(
      EC.presence_of_element_located((By.XPATH, "//button[@class='js-toggle-address-line ncss-btn text-color-grey ncss-base p0-sm']")))
  expand_line_2.click()

  city = WebDriverWait(browser, delay).until(
      EC.presence_of_element_located((By.ID, 'city')))
  city.send_keys('Bronx')

  state = WebDriverWait(browser, delay).until(
      EC.presence_of_element_located((By.XPATH, "//select[@id='state']/option[text()='New York']")))
  state.click()

  postal_code = WebDriverWait(browser, delay).until(
      EC.presence_of_element_located((By.ID, 'postalCode')))
  postal_code.send_keys('10458')

  email = WebDriverWait(browser, delay).until(
      EC.presence_of_element_located((By.ID, 'email')))
  email.send_keys('dadewoyin16@gmail.com')

  phone_number = WebDriverWait(browser, delay).until(
      EC.presence_of_element_located((By.ID, 'phoneNumber')))
  phone_number.send_keys('8457415400')

  address_2 = WebDriverWait(browser, delay).until(
      EC.presence_of_element_located((By.XPATH, '//input[@id="address2"]')))
  address_2.send_keys('Apt. 4')

  save_and_continue = WebDriverWait(browser, delay).until(
      EC.presence_of_element_located((By.XPATH, "//button[text()='Save & Continue']")))
  save_and_continue.click()

  continue_to_payment = WebDriverWait(browser, delay).until(
      EC.presence_of_element_located((By.XPATH, "//button[text()='Continue to Payment']")))
  continue_to_payment.click()

def fillOutPaymentInfo():
  print("START OF DIS DAWG")
  paymentSetup = browser.find_element_by_xpath(
      '//input[@id="creditCardNumber"]')
  print("blahhhhhh")
  action.move_to_element(paymentSetup).perform()
  print("MOVING HERE YOOOO")
  card_number = WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.XPATH, '//input[@id="creditCardNumber"]')))
  print("Another checkerrrr")
  time.sleep(1)
  print("we schleeeeeeeep")
  time.sleep(1)
  card_number.send_keys('8457415400')

  exp_date = WebDriverWait(browser, delay).until(
      EC.presence_of_element_located((By.ID, 'expirationDate')))
  exp_date.send_keys('1221')

  cvv = WebDriverWait(browser, delay).until(
      EC.presence_of_element_located((By.ID, 'cvNumber')))
  cvv.send_keys('457')


def SubmitOrder():
  submit_order = WebDriverWait(browser, delay).until(
      EC.presence_of_element_located((By.XPATH, "//button[text()='Place Order']")))
  submit_order.click()


# def login():
#   email_input = WebDriverWait(browser, delay).until(
#       EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Email"]')))
#   email_input.send_keys('david@platform.community')

#   password_input = WebDriverWait(browser, delay).until(
#       EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))
#   password_input.send_keys('dragoon1')

#   time.sleep(3)

#   add_to_cart = WebDriverWait(browser, delay).until(
#       EC.element_to_be_clickable((By.XPATH, '//input[@value="MEMBER CHECKOUT"]')))
#   add_to_cart.click()


if __name__ == "__main__":
  start()
