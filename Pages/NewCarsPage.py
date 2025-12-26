from Pages.BasePage import BasePage

class HomePage:
    def __init__(self,driver):
        self.driver = driver

    def selectHyundai(self):
        self.click("hyundai_XPATH")

    def selectToyota(self):
        self.click("toyota_XPATH")

    def selectSkoda(self):
        self.click("skoda_XPATH")

    def selectKia(self):
        self.click("kia_XPATH")