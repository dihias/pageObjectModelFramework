from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import configReader


class CarBase:
    def __init__(self, driver):
        self.driver = driver

    def getCarTitle(self):
        xpath = configReader.readConfig("locators", "carTitle_XPATH")
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        ).text

    def getCarNameAndPrice(self):
        names_XPATH = configReader.readConfig("locators", "carName_XPATH")
        prices_XPATH = configReader.readConfig("locators", "carPrice_XPATH")

        carNames=self.driver.find_elements(By.XPATH, names_XPATH)
        carPrices=self.driver.find_elements(By.XPATH, prices_XPATH)

        for i in range(1,len(carPrices)):
            print(carNames[i].text + "--------prices are : "+ carPrices[i].text)

