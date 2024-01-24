import time
import allure

from PageObjects.LoginPage import Login
from PageObjects.locators import *
from Utilities.return_message import *
from Utilities.constants import *
from Utilities.generate_email import *
from Utilities.Readconfigurations import *

class ImageBasedSubjectiveQuestion:
    def __init__(self, driver):
        self.driver = driver
            
    @allure.step('Firstly, always run login functionality')
    def section_open_of_image_based_subjective_question_section(self):
        login = Login(self.driver)
        login.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        login.click_on_image_based_subjective_question_section()
        
    @allure.step('Click on new question button')    
    def click_on_new_question_button(self):
        self.driver.find_element(*Locators.ADD_NEW_QUESTION_BUTTON).click()
        time.sleep(2)
    
    @allure.step('Fill question title input type')     
    def input_question_title(self):
        return self.driver.find_element(*Locators.INPUT_QUESTION_TITLE)
    
    @allure.step('Fill answer key input type')
    def input_answer_keys(self):
        return self.driver.find_element(*Locators.INPUT_ANSWER_KEYS)
    
    @allure.step('Fill image input type')
    def input_image_upload(self):
        return self.driver.find_element(*Locators.INPUT_IMAGE)
    
    @allure.step('Click on save button')
    def click_on_save_button(self):
        return self.driver.find_element(*Locators.SAVE_BUTTON)
    
    @allure.step('Click on save button')
    def click_on_close_button(self):
        return self.driver.find_element(*Locators.CLOSE_BUTTON)
    
    @allure.step('get text of question in existing table')
    def get_question_of_existing_table(self):
        return self.driver.find_element(*Locators.GET_QUESTION_TEXT)
    
    def add_new_image_based_subjective_question(self, subject, question_title, answer_keys, image, add_question, validation):
        self.section_open_of_image_based_subjective_question_section()
        previous_text = self.get_question_of_existing_table().get_attribute('innerText')
        self.click_on_new_question_button()
        if subject:
            dropdown_input(self.driver, TIME_DURATION, *Locators.INPUT_SUBJECT, subject)
        self.input_question_title().send_keys(question_title)
        self.input_answer_keys().send_keys(answer_keys)
        if image:
            self.input_image_upload().send_keys(image)
        if validation and add_question:
            self.click_on_save_button().click()
            time.sleep(2)
            if image == OTHER_IMAGE:
                assert dynamic_explicit_wait_without_message(self.driver,TIME_DURATION, *Locators.PARSLEY_MAXFILESIZE).is_displayed()
            elif image == ANOTHER_IMAGE:
                assert dynamic_explicit_wait_without_message(self.driver,TIME_DURATION, *Locators.PARSLEY_FILEEXTENSION).is_displayed()
            else:
                assert dynamic_explicit_wait_without_message(self.driver,TIME_DURATION, *Locators.PARSLEY_REQUIRED).is_displayed()
        elif add_question:
            self.click_on_save_button().click()
            if TYPING_TEST in subject:
                assert dynamic_explicit_wait(self.driver,TIME_DURATION, *Locators.DISPLAY_MESSAGE, TYPING_VALIDATION)
            elif EXCEL in subject:
                assert dynamic_explicit_wait(self.driver,TIME_DURATION, *Locators.DISPLAY_MESSAGE, EXCEL_VALIDATION)
            else:
                assert dynamic_explicit_wait_without_message(self.driver, TIME_DURATION, *Locators.DISPLAY_MESSAGE).is_displayed()
        else:
            self.click_on_close_button().click()
            new_text = self.get_question_of_existing_table().get_attribute('innerText')
            assert previous_text == new_text
