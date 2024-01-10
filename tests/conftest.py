import pytest
import configparser
import allure

from allure_commons.types import AttachmentType
from selenium import webdriver
from PageObjects.AllowAuthenticatedUserPage import AllowAuthenticatedUser
from PageObjects.LoginPage import Login
from PageObjects.SubjectPage import Subject
from PageObjects.MultipleImageChoiceQuestionPage import MultipleImageChoiceQuestion
from PageObjects.MultipleChoiceQuestionPage import MultipleChoiceQuestion
from PageObjects.ImageBasedMultipleChoiceQuestionPage import ImageBasedMultipleChoiceQuestion
from PageObjects.SubjectiveQuestionPage import SubjectiveQuestion
from Utilities.logger import logclass
from Utilities.constants import *
from Utilities.generate_email import *
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
    request.cls.subjective_question = SubjectiveQuestion(request.cls.driver)
    request.cls.image_based_multiple_choice_question = ImageBasedMultipleChoiceQuestion(request.cls.driver)
    request.cls.multiple_choice_question = MultipleChoiceQuestion(request.cls.driver)
    request.cls.multiple_image_choice_question = MultipleImageChoiceQuestion(request.cls.driver)
    request.cls.subject = Subject(request.cls.driver)
    request.cls.authenticated_user = AllowAuthenticatedUser(request.cls.driver)
    request.cls.login = Login(request.cls.driver)
    yield
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    result = outcome.get_result()
    if result.failed:
        allure.attach(item.cls.driver.get_screenshot_as_png(), name=SCREENSHOT + time.strftime('_%Y_%m_%d_%H_%M_%S'), attachment_type=AttachmentType.PNG)
