import time

from Pages.BasePage import BasePage

class NewCarsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def selectHyundai(self):
        self.wait_for_element("hyundai_XPATH")
        self.click("hyundai_XPATH")

    def selectToyota(self):
        self.wait_for_element("toyota_XPATH")
        self.click("toyota_XPATH")

    def selectBMW(self):
        self.wait_for_element("Bmw_XPATH")
        self.click("Bmw_XPATH")

    def selectHonda(self):
        self.wait_for_element("honda_XPATH")
        self.click("honda_XPATH")