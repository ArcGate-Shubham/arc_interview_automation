import pytest
import configparser
from selenium import webdriver
from PageObjects.AllowAuthenticatedUserPage import AllowAuthenticatedUser
from PageObjects.LoginPage import Login
from PageObjects.SubjectPage import Subject
from PageObjects.MultipleImageChoiceQuestionPage import MultipleImageChoiceQuestion
from Utilities.logger import logclass
driver = None
config = configparser.ConfigParser()
config.read("Utilities/input.properties")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(config.get("Url", "base_url"))
    request.cls.driver = driver
    request.cls.log = logclass(driver)
    request.cls.multiple_image_choice_question = MultipleImageChoiceQuestion(request.cls.driver)
    request.cls.subject = Subject(request.cls.driver)
    request.cls.authenticated_user = AllowAuthenticatedUser(request.cls.driver)
    request.cls.login = Login(request.cls.driver)
    yield
    driver.quit()
