import time
from time import sleep

import pytest
import logging

from Pages.BasePage import BasePage
from Pages.CarBase import CarBase
from Pages.HomePage import HomePage
from Utilities.LogUtil import Logger
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Pages.NewCarsPage import NewCarsPage

from Pages.RegistrationPage import RegistrationPage

log = Logger(__name__,logging.INFO)

class Test_Carwale(BaseTest):

    @pytest.mark.skip
    def test_gotoNewCar(self):
        log.logger.info("*************inside new car test******************")
        home = HomePage(self.driver)
        home.go_to_new_cars()
        time.sleep(3)

    @pytest.mark.skip
    @pytest.mark.parametrize("carBrand,carTitle", dataProvider.get_data("NewCarsTest"))
    def test_selectCars(self, carBrand,carTitle):
        log.logger.info("******Inside Select Cars Test*********")
        home = HomePage(self.driver)
        car = CarBase(self.driver)

        print("Car brand is : ",carBrand)
        if carBrand == "BMW":
           home.go_to_new_cars().selectBMW()
           title = car.getCarTitle()
           print("Car Title is : "+title)
           assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Hyundai":
           home.go_to_new_cars().selectHyundai()
           title = car.getCarTitle()
           print("Car Title is : " + title)
           assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Honda":
           home.go_to_new_cars().selectHonda()
           title = car.getCarTitle()
           print("Car Title is : " + title)
           assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Toyota":
           home.go_to_new_cars().selectToyota()
           title = car.getCarTitle()
           print("Car Title is : " + title)
           assert title == carTitle, "Not on the correct page as title is not matching"

    @pytest.mark.parametrize("carBrand,carTitle", dataProvider.get_data("NewCarsTest"))
    def test_printCarsNamesAndPrices(self, carBrand, carTitle):
        log.logger.info("******Inside Cars Names and prices Test*********")
        home = HomePage(self.driver)
        car = CarBase(self.driver)

        print("Car brand is : ", carBrand)
        if carBrand == "BMW":
            home.go_to_new_cars().selectBMW()
            title = car.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrice()
        elif carBrand == "Hyundai":
            home.go_to_new_cars().selectHyundai()
            title = car.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrice()
        elif carBrand == "Honda":
            home.go_to_new_cars().selectHonda()
            title = car.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrice()
        elif carBrand == "Toyota":
            home.go_to_new_cars().selectToyota()
            title = car.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrice()