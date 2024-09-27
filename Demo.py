import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from yaml import reader

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.saucedemo.com/")
driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH," //input[@id='login-button']").click()
successText = driver.find_element(By.XPATH,"//div[@class='app_logo']").text
assert "Swag Labs" in successText
getProductName = driver.find_element(By.XPATH,"//div[normalize-space()='Sauce Labs Backpack']").text
getPrice = driver.find_element(By.XPATH,"//div[normalize-space()='$29.99']").text
with open('Text.txt','w') as file:
    content = file.write(getProductName)
    content1 = file.write(getPrice)
    print (content)
driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']").click()
driver.find_element(By.CSS_SELECTOR,".shopping_cart_link").click()
driver.find_element(By.CSS_SELECTOR,"#checkout").click()
driver.find_element(By.CSS_SELECTOR," #first-name").send_keys("Sathish")
driver.find_element(By.XPATH," //input[@id='last-name']").send_keys("B")
driver.find_element(By.XPATH,"//input[@id='postal-code']").send_keys("560075")
driver.find_element(By.XPATH,"//input[@id='continue']").click()

driver.find_element(By.XPATH," //button[@id='finish']").click()

successCart = driver.find_element(By.CSS_SELECTOR,".complete-header").text

assert "Thank you for your order!" in successCart


time.sleep(10)
