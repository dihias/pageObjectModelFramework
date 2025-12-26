from Pages.BasePage import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_new_cars(self):
        self.move_to("new_cars_XPATH")
        self.click("find_new_cars")

    def go_to_compare_cars(self):
        pass

    def go_to_used_cars(self):
        pass