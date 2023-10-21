# locator_passport_id ="identifyWithOtpCitizenId"
# locator_birthday_date_id = "birthDate"
# passport = '332708494'
# birthdate = '20/04/1975'

from pom.Base_page import Driver_Base
#
class HomePage(Driver_Base):


    def __init__(self,something):
        super(HomePage, self).__init__(something)


        self.locator_passport_id = "identifyWithOtpCitizenId"
        self.locator_birthday_date_id = "birthDate"
        self.passport = "332708494"
        self.birthday = "20/0*/197*"
        self.locator_keep_on = "המשך"



    def load_page(self):
        self.driver.get('https://mac.maccabi4u.co.il/login?SAMLRequest=rZLLboMwEEV%2FBXkPGAJJsAJV2qhqpD5Qg7roppqAk1gyY2qbPv6%2BhlRqqkpZ%0AdeGV73jOufLCQCs7tuztAR%2F5a8%2BN9T5aiYaNFznpNTIFRhiG0HLDbM02y7tb%0AFgeUdVpZVStJvJWbEwhWKMzJwdrOsDBsoQ7cqWErkj6oVSBkKNVeIPGula75%0AuDQnlHjrVU5eJpCmEd%2FxXTKZR%2FN4mvGsyWYwBbqdJXESu5gxPV%2BjsYA2JzGN%0AJz7NfJpW0YzFlKX0mXjlN9OlwEbg%2FrzA9hgy7KaqSr982FTjA2%2Bi4frepX9c%0AFEqB%2FI9OAwg%2BQghOJRwa8zk2nRJog3ovLrrcdI77iWszNuN2kmIx5Njook%2B6%0APk8KxnA91EuKf0BahCcMR6CODcLrVamkqD%2B9pZTq%2FUpzsK6EiITFceT3Tym%2B%0AAA%3D%3D%0A&RelayState=https%3A%2F%2Fonline.maccabi4u.co.il&SigAlg=http%3A%2F%2Fwww.w3.org%2F2000%2F09%2Fxmldsig%23rsa-sha1&Signature=EhNQKAKTb3qKer49nUBPelb69I9jFTb8gnBWlH3Xsc838p5dGsuW3JaEEjT3%2B2zJMEqLRG0FP97NbKU5yowzSktgr81anGvoBP3bUWdFfGThlIUyCYZJOv0WxZ8qny0%2BdBBAD3crOQIJDqMbUXquvgXqmvCw9NTAtAWbdZAjERsB7xrZOfKzaHZoXXAoj0ciicxdiSeIDkC%2BVWSS8zL15IeRW7nEqlqsFn8noj2md%2Fk1rABDcuSo7g6HExN%2B%2BbEP6iyVGH93%2FKQqGm7%2BdFgSeC5%2F6KHkpyvUlKAU4hQALJv2ucIJTjeOGW6wL%2FhXeEBwpZNIyWqScDW7VcaVrvW%2BOQ%3D%3D')
