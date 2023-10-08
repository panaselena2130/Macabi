# locator_passport_id ="identifyWithOtpCitizenId"
locator_birthday_date_id = "birthDate"


from pom.Base_page import Driver_Base
#
class HomePage(Driver_Base):


    def __init__(self,something):
        super(HomePage, self).__init__(something)


        self.locator_passport_id = "identifyWithOtpCitizenId"



