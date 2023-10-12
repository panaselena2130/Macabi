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
        self.birthday = "20/04/1975"



