import pytest
import logging
from Utilities.LogUtil import Logger
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider

from Pages.RegistrationPage import RegistrationPage

log = Logger(__name__,logging.INFO)

class TestSignUpTest(BaseTest):
    @pytest.mark.parametrize("name,phone_num,email,country,city,username,password", dataProvider.get_data("LoginTest"))
    def test_do_signup(self,name,phone_num,email,country,city,username,password):
        log.logger.info("Testing Sign Up")
        reg_page = RegistrationPage(self.driver)
        reg_page.fill_form(name,phone_num,email,country,city,username,password)
        log.logger.info("Successfully Signed Up")
