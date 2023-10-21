import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pom.Base_page  import Driver_Base

from pom.home_page import HomePage



dr = webdriver.Chrome()

#create object of class HomePage and putting variable -  driver as attribute to HomePage(BasePage)
driver = HomePage(dr)

#open homepage of necessery wibsite
driver.load_page()

#  *********************************************************
# checking verification of page

# driver.verific_page()
#  *********************************************************

#checking of element of sending number passport is visible
driver.is_visible('id',driver.locator_passport_id).send_keys(driver.passport_keys)


#checking of element of input field of date birth is visible and click
driver.do_click('id', driver.locator_birthday_date_id)


# click of year input field
driver.do_click('class', driver.year_input_field_class)

#checking of element dropdown triangle of year
driver.is_visible('xpath', driver.year_xpath_1975).click()

# click of month input field
driver.do_click('class',driver.month_input_field_class)


#checking of element dropdown triangle of month
driver.is_visible('xpath', driver.month_xpath_april).click()



#checking of element  day of month is visible
driver.is_visible('xpath', driver.day_xpath_20).click()



#checking of element continue is visible
driver.is_visible('xpath', driver.continue_xpath).click()

#making screenshot
driver.screenshot_now('arrived to Sign in to personal account')









