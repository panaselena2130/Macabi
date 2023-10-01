from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from typing import List


class Driver:

    def __init__(self,dr):
        self.driver = dr
        self.wait = WebDriverWait(dr,10)
        # self.abc = abc
        # self.defg = defg




    def load_page(self):
        self.driver.get('https://mac.maccabi4u.co.il/login?SAMLRequest=rZLLboMwEEV%2FBXkPGAJJsAJV2qhqpD5Qg7roppqAk1gyY2qbPv6%2BhlRqqkpZ%0AdeGV73jOufLCQCs7tuztAR%2F5a8%2BN9T5aiYaNFznpNTIFRhiG0HLDbM02y7tb%0AFgeUdVpZVStJvJWbEwhWKMzJwdrOsDBsoQ7cqWErkj6oVSBkKNVeIPGula75%0AuDQnlHjrVU5eJpCmEd%2FxXTKZR%2FN4mvGsyWYwBbqdJXESu5gxPV%2BjsYA2JzGN%0AJz7NfJpW0YzFlKX0mXjlN9OlwEbg%2FrzA9hgy7KaqSr982FTjA2%2Bi4frepX9c%0AFEqB%2FI9OAwg%2BQghOJRwa8zk2nRJog3ovLrrcdI77iWszNuN2kmIx5Njook%2B6%0APk8KxnA91EuKf0BahCcMR6CODcLrVamkqD%2B9pZTq%2FUpzsK6EiITFceT3Tym%2B%0AAA%3D%3D%0A&RelayState=https%3A%2F%2Fonline.maccabi4u.co.il&SigAlg=http%3A%2F%2Fwww.w3.org%2F2000%2F09%2Fxmldsig%23rsa-sha1&Signature=EhNQKAKTb3qKer49nUBPelb69I9jFTb8gnBWlH3Xsc838p5dGsuW3JaEEjT3%2B2zJMEqLRG0FP97NbKU5yowzSktgr81anGvoBP3bUWdFfGThlIUyCYZJOv0WxZ8qny0%2BdBBAD3crOQIJDqMbUXquvgXqmvCw9NTAtAWbdZAjERsB7xrZOfKzaHZoXXAoj0ciicxdiSeIDkC%2BVWSS8zL15IeRW7nEqlqsFn8noj2md%2Fk1rABDcuSo7g6HExN%2B%2BbEP6iyVGH93%2FKQqGm7%2BdFgSeC5%2F6KHkpyvUlKAU4hQALJv2ucIJTjeOGW6wL%2FhXeEBwpZNIyWqScDW7VcaVrvW%2BOQ%3D%3D')

    def create_driver():
        return webdriver.Chrome()

    def verific_page(self):
        return self.get_element_title()

    def webelement_by(self, find_by: str) -> dict:

        locating = {'xpath1': By.XPATH,
                    'css': By.CSS_SELECTOR,
                    'class': By.CLASS_NAME}

        return locating[find_by.lower()]


    def are_visible(self, find_by: str, locator: str, locator_name=None) -> List[WebElement]:
        return self.wait.until(ec.visibility_of_all_elements_located((self.webelement_by(find_by), locator)),
                               locator_name)

    def do_click(self, find_by: str, locator: str, locator_name) -> List[WebElement]:
        return self.wait.until(ec.element_to_be_clickable((self.webelement_by(find_by), locator)),
                               locator_name).click()

    def get_element_title(self):

        expected_title = input('Enter_expected_name_page_title').upper()
        actual_title = self.driver.title
        try:
            assert expected_title in actual_title
            print("Assertion_Test_Pass_Verification_page")

        except Exception as e:
            print('Assertion Test_Pass_Verification_page failed,enter another name_page_title.', format(e))
            raise
        return actual_title

    def get_text_from_webelements(self, elements: List[WebElement]) -> List[str]:
        return [element.text for element in elements]

    def get_element_by_text(self, elements: List[WebElement], name: str) -> WebElement:
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]