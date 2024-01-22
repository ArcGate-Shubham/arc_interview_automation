import time
import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from PageObjects.LoginPage import Login
from PageObjects.locators import *
from Utilities.return_message import *
from Utilities.constants import *
from Utilities.generate_email import *
from Utilities.Readconfigurations import *

class ImageBasedMultipleChoiceQuestion:
    def __init__(self, driver):
        self.driver = driver
        
    @allure.step('click on new question button')    
    def click_on_add_question_button(self):
        self.driver.find_element(*Locators.ADD_NEW_QUESTION_BUTTON).click()
        time.sleep(2)
        
    def input_subject(self, subject):
        wait = WebDriverWait(self.driver, 10)
        select = wait.until(EC.presence_of_element_located((ImageBasedMultipleChoiceQuestionPageLocators.INPUT_SUBJECT)))
        select = Select(select)
        subject = select.select_by_visible_text(subject)
        return subject
    
    def input_question_title(self):
        return self.driver.find_element(*ImageBasedMultipleChoiceQuestionPageLocators.INPUT_QUESTION_TITLE)
    
    def input_optionA(self):
        return self.driver.find_element(*ImageBasedMultipleChoiceQuestionPageLocators.OPTIONA)
    
    def input_optionB(self):
        return self.driver.find_element(*ImageBasedMultipleChoiceQuestionPageLocators.OPTIONB)
    
    def input_optionC(self):
        return self.driver.find_element(*ImageBasedMultipleChoiceQuestionPageLocators.OPTIONC)
    
    def input_optionD(self):
        return self.driver.find_element(*ImageBasedMultipleChoiceQuestionPageLocators.OPTIOND)
    
    @allure.step('checked on correct options')
    def checked_on_correct_option(self):
        return self.driver.find_element(*ImageBasedMultipleChoiceQuestionPageLocators.CHECKED_ON_CORRECT_OPTION)
    
    @allure.step('click on save button')
    def click_on_save_button(self):
        return self.driver.find_element(*SubjectiveQuestionPageLocators.SAVE_BUTTON)
    
    def input_image_upload(self):
        return self.driver.find_element(*ImageBasedMultipleChoiceQuestionPageLocators.IMAGE_UPLOAD)
    
    @allure.step('Display message of response')    
    def display_message_section(self):
        return self.driver.find_element(*Locators.DISPLAY_MESSAGE)
    
    @allure.step('Row count of multiple choice question')
    def row_count_image_based_multiple_choice_question(self):
        return self.driver.find_elements(*Locators.TABLE_ROW_COUNT)
    
    @allure.step('click on close button')
    def click_on_close_button(self):
        return self.driver.find_element(*SubjectiveQuestionPageLocators.CLOSE_BUTTON)
    
    def required_validation(self):
        return self.driver.find_element(*Locators.PARSLEY_REQUIRED)
    
    def search_by_question_title(self):
        return self.driver.find_element(*ImageBasedMultipleChoiceQuestionPageLocators.SEARCH_BY_QUESTION_TITLE)
       
    def search_by_subject(self, subject):
        wait = WebDriverWait(self.driver, 10)
        select = wait.until(EC.presence_of_element_located((ImageBasedMultipleChoiceQuestionPageLocators.SEARCH_BY_SUBJECT)))
        select = Select(select)
        subject = select.select_by_visible_text(subject)
        return subject
    
    @allure.step('Click on search button')
    def click_on_search_button(self):
        return self.driver.find_element(*ImageBasedMultipleChoiceQuestionPageLocators.SEARCH_BUTTON)
    
    @allure.step('Click on edit button')
    def click_on_edit_button(self):
        return self.driver.find_element(*Locators.EDIT_BUTTON)
    
    @allure.step('Click on delete button')
    def click_on_delete_button(self):
        return self.driver.find_element(*Locators.DELETE_BUTTON)
    
    @allure.step('get text from question')
    def get_text_of_questions(self):
        return self.driver.find_element(*ImageBasedMultipleChoiceQuestionPageLocators.GET_QUESTION_TEXT)
    
    @allure.step('Firstly, always run login functionality')
    def section_open_of_image_based_multiple_choice_question_section(self):
        login = Login(self.driver)
        login.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        login.click_on_image_based_multiple_choice_question_section()
        
    def add_image_based_multiple_choice_question(self, subject, question_title, optionA, optionB, optionC, optionD, image, add_question, validation):
        self.section_open_of_image_based_multiple_choice_question_section()
        previous_row_length = len(self.row_count_image_based_multiple_choice_question())
        self.click_on_add_question_button()
        self.input_subject(subject)
        self.input_question_title().send_keys(question_title)
        self.input_optionA().send_keys(optionA)
        self.input_optionB().send_keys(optionB)
        self.input_optionC().send_keys(optionC)
        self.input_optionD().send_keys(optionD)
        self.checked_on_correct_option().click()
        self.input_image_upload().send_keys(image)
        if validation and add_question:
            self.click_on_save_button().click()
            if len(question_title) == LENGTH or len(optionA) == LENGTH or len(optionB) == LENGTH or len(optionC) == LENGTH or len(optionD) == LENGTH:
                assert dynamic_explicit_wait_without_message(self.driver,TIME_DURATION, *Locators.PARSLEY_MAXLENGTH).is_displayed()
            else:
                if image == OTHER_IMAGE:
                    assert dynamic_explicit_wait_without_message(self.driver,TIME_DURATION, *Locators.PARSLEY_MAXFILESIZE).is_displayed()
                else:
                    assert dynamic_explicit_wait_without_message(self.driver,TIME_DURATION, *Locators.PARSLEY_REQUIRED).is_displayed()
        elif add_question:
            self.click_on_save_button().click()
            if EXCEL in subject:
                assert dynamic_explicit_wait(self.driver, TIME_DURATION, *Locators.DISPLAY_MESSAGE, EXCEL_VALIDATION)
            elif TYPING_TEST in subject:
                assert dynamic_explicit_wait(self.driver, TIME_DURATION, *Locators.DISPLAY_MESSAGE, TYPING_VALIDATION)
            else:
                assert dynamic_explicit_wait(self.driver, TIME_DURATION, *Locators.DISPLAY_MESSAGE, QUESTION_ADDED)
        else:
            self.click_on_close_button().click()
            new_row_length = len(self.row_count_image_based_multiple_choice_question())
            assert previous_row_length == new_row_length
            
    def search_functionality(self, question_title, subject, validation):
        self.section_open_of_image_based_multiple_choice_question_section()
        if question_title and subject:
            self.search_by_question_title().send_keys(question_title)
            self.search_by_subject(subject)
        elif question_title:
            self.search_by_question_title().send_keys(question_title)
        elif subject:
            self.search_by_subject(subject)
        self.click_on_search_button().click()
        if validation:
            assert dynamic_explicit_wait(self.driver, TIME_DURATION, *Locators.DISPLAY_MESSAGE, NO_DATA)
        else:
            assert len(self.row_count_image_based_multiple_choice_question()) > ZERO
            
    def delete_row_in_table(self, accept):
        self.section_open_of_image_based_multiple_choice_question_section()
        old_row = len(self.row_count_image_based_multiple_choice_question())
        self.click_on_delete_button().click()
        if accept:
            self.driver.switch_to.alert.accept()
            assert dynamic_explicit_wait(self.driver, TIME_DURATION, *Locators.DISPLAY_MESSAGE, QUESTION_DELETED)
        else:
            self.driver.switch_to.alert.dismiss()
            new_row = len(self.row_count_image_based_multiple_choice_question())
            assert old_row == new_row
            
    def edit_row_of_existing_table(self):
        self.section_open_of_image_based_multiple_choice_question_section()
        previous_text = self.get_text_of_questions().get_attribute('innerText')
        self.click_on_edit_button()
        self.click_on_close_button()
        new_text = self.get_text_of_questions().get_attribute('innerText')
        assert previous_text == new_text
