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

driver = Driver_Base(dr)

driver.load_page()

# driver.verific_page()

driver.are_visible('xpath1',locator_passport_id)


time.sleep(5)





