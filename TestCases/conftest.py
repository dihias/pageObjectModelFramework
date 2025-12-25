import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager
from Utilities import configReader

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


#@pytest.fixture(params=["chrome","firefox"],scope="function")
@pytest.fixture(params=["chrome"],scope="class")
def get_browser(request):

    driver = webdriver.Chrome()
    if request.param == "chrome":
        driver = webdriver.Chrome()
    if request.param == "firefox":
        driver = webdriver.Firefox()
    request.cls.driver = driver
    driver.get("https://www.way2automation.com/way2auto_jquery/index.php")#configReader.readConfig("basic_info","test_site_url"))
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def log_on_failure(request,get_browser):
    yield
    item = request.node
    driver = get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)