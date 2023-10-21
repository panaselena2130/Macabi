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
driver.screenshot_now("passport was sent")

#checking of element of input field of date birth is visible and click
driver.do_click('id', driver.locator_birthday_date_id)
driver.screenshot_now("input field of birth click")

# click of year input field
driver.do_click('class', driver.year_input_field_class)

#checking of element dropdown triangle of year
driver.is_visible('xpath', driver.year_xpath_1975).click()

# click of month input field
driver.do_click('class',driver.month_input_field_class)


#checking of element dropdown triangle of month
driver.is_visible('xpath', driver.month_xpath_april).click()



#checking of element dropdown triangle of day
driver.is_visible('xpath', driver.day_xpath_20).click()









#
# time.sleep(5)
#
# driver.is_visible('class', driver.locator_keep_on)
# time.sleep(5)
#
# driver.click()
#
# driver.send_keys(driver.birthday)



time.sleep(5)







