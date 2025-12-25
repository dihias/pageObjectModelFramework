import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import openpyxl
import logging
from Utilities.LogUtil import Logger

log = Logger(__name__,logging.INFO)

from TestCases.BaseTest import BaseTest
from Utilities import dataProvider

from Pages.RegistrationPage import RegistrationPage


class TestSignUpTest(BaseTest):
    @pytest.mark.parametrize("name,phone_num,email,country,city,username,password", dataProvider.get_data("LoginTest"))
    def test_do_signup(self,name,phone_num,email,country,city,username,password):
        log.logger.info("Testing Sign Up")
        reg_page = RegistrationPage(self.driver)
        reg_page.fill_form(name,phone_num,email,country,city,username,password)
        log.logger.info("Successfully Signed Up")
