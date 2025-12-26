import time

from Pages.BasePage import BasePage
from Pages.NewCarsPage import NewCarsPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_new_cars(self):
        self.move_to("new_cars_XPATH")
        self.click("find_new_cars_XPATH")
        self.wait_for_element("new_cars_page_identifier_XPATH")
        return NewCarsPage(self.driver)

    def go_to_compare_cars(self):
        pass

    def go_to_used_cars(self):
        pass