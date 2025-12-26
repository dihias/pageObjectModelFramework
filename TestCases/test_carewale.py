import time

import pytest
import logging

from Pages.HomePage import HomePage
from Utilities.LogUtil import Logger
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider

from Pages.RegistrationPage import RegistrationPage

log = Logger(__name__,logging.INFO)

class Test_Carwale(BaseTest):
    def test_gotoNewCar(self):
        log.logger.info("*************inside new car test******************")
        home = HomePage(self.driver)
        home.go_to_new_cars()
        time.sleep(3)
