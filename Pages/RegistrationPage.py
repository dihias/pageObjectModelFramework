from Pages.BasePage import BasePage

from Utilities import configReader

from selenium.webdriver.common.by import By
class RegistrationPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)



    def fill_form(self, name,phone_num,email,country,city,username,password):
        self.type("name_CSS",name)
        self.type("phone_CSS",phone_num)
        self.type("email_XPATH",email)

        self.select("country_XPATH",country)

        self.type("city_XPATH",city)
        self.type("username_XPATH",username)
        self.type("password_XPATH",password)
        self.click("submit_XPATH")

