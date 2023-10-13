import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pom.Base_page  import Driver_Base

from pom.home_page import HomePage


# driver_path = 'C:\\Users\Lena\pythonProject\Macabi\Source\chromedriver.exe'
dr = webdriver.Chrome()

# driver = Driver_Base(dr)

driver = HomePage(dr)
driver.load_page()

# driver.verific_page()

driver.is_visible('id',driver.locator_passport_id).send_keys(driver.passport)
print("ok")

# driver.send_keys(driver.passport)



driver.is_visible('id', driver.locator_birthday_date_id).send_keys(driver.birthday)
print("ok")

time.sleep(5)

driver.is_visible('class', driver.locator_keep_on)
time.sleep(5)

driver.click()

driver.send_keys(driver.birthday)



time.sleep(5)







