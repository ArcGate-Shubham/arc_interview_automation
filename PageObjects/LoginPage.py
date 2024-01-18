import time
import allure

from PageObjects.locators import *
from Utilities.return_message import *
from Utilities.constants import *
class Login:
    def __init__(self, driver):
        self.driver = driver
        
    def fill_username_password_input(self, Username, Password):
        self.driver.find_element(*LoginPageLocators.INPUT_USERNAME).send_keys(Username)
        self.driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(Password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        time.sleep(3)

    @allure.step('Display success login message')
    def display_successfully_login_message(self):
        assert SUCCESS_LOGIN in self.driver.find_element(*Locators.DISPLAY_MESSAGE).text

    @allure.step('Display invalid login message')
    def display_invalid_crediential_message(self):
        assert INVALID_CREDIENTIAL in self.driver.find_element(*Locators.DISPLAY_MESSAGE).text

    @allure.step('Display login text')
    def display_admin_login_text(self):
        assert LOGIN in self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).text

    def click_on_allow_authenticated_user_section(self):
        self.driver.find_element(*LoginPageLocators.CLICK_TEXT_ALLOW_AUTHENTICATED_USER_XPATH).click()

    def click_on_add_subject_section(self):
        return self.driver.find_element(*LoginPageLocators.CLICK_TEXT_ADD_SUBJECT_XPATH).click()

    def click_on_multiple_image_choice_question_section(self):
        return self.driver.find_element(*LoginPageLocators.CLICK_TEXT_MULTIPLE_IMAGE_CHOICE_QUESTION_XPATH).click()

    def click_on_multiple_choice_question_section(self):
        return self.driver.find_element(*LoginPageLocators.CLICK_TEXT_MULTIPLE_CHOICE_QUESTION_XPATH).click()

    def click_on_image_based_multiple_choice_question_section(self):
        return self.driver.find_element(*LoginPageLocators.CLICK_TEXT_IMAGE_BASED_MULTIPLE_CHOICE_QUESTION_XPATH).click()

    def click_on_subjective_question_section(self):
        return self.driver.find_element(*LoginPageLocators.CLICK_TEXT_SUBJECTIVE_QUESTION_XPATH).click()

    def click_on_image_based_subjective_question_section(self):
        return self.driver.find_element(*LoginPageLocators.CLICK_TEXT_IMAGE_BASED_SUBJECTIVE_QUESTION_XPATH).click()
