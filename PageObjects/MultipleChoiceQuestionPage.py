import time
import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from PageObjects.LoginPage import Login
from PageObjects.locators import *
from Utilities.return_message import *
from Utilities.Readconfigurations import *
from Utilities.constants import *

class MultipleChoiceQuestion:
    def __init__(self, driver):
        self.driver = driver
     
    @allure.step('click on add multiple choice question')    
    def add_multiple_choice_question_button(self):
        time.sleep(2)
        self.driver.find_element(*Locators.ADD_NEW_QUESTION_BUTTON).click()
        
    def input_subject(self, subject):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        select = wait.until(EC.presence_of_element_located((MultipleChoiceQuestionPageLocators.INPUT_SUBJECT)))
        select = Select(select)
        subject = select.select_by_visible_text(subject)
        return subject
    
    def input_passage(self, passage):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        select = wait.until(EC.presence_of_element_located((MultipleChoiceQuestionPageLocators.INPUT_PASSAGE)))
        select = Select(select)
        passage = select.select_by_visible_text(passage)
        return passage
    
    def input_question_title(self):
        return self.driver.find_element(*MultipleChoiceQuestionPageLocators.INPUT_QUESTION_TITLE)
    
    def input_optionA(self):
        return self.driver.find_element(*MultipleChoiceQuestionPageLocators.INPUT_OPTION_A)
    
    def input_optionB(self):
        return self.driver.find_element(*MultipleChoiceQuestionPageLocators.INPUT_OPTION_B)
    
    def input_optionC(self):
        return self.driver.find_element(*MultipleChoiceQuestionPageLocators.INPUT_OPTION_C)
    
    def input_optionD(self):
        return self.driver.find_element(*MultipleChoiceQuestionPageLocators.INPUT_OPTION_D)
    
    @allure.step('Fill all detail of multiple choice question form after that click on save button')
    def click_on_save_button(self):
        self.driver.find_element(*SubjectiveQuestionPageLocators.SAVE_BUTTON).click()
    
    @allure.step('Checked on correct answer check box of muliple choice question options')    
    def click_on_right_answer_button(self):
        self.driver.find_element(*ImageBasedMultipleChoiceQuestionPageLocators.CHECKED_ON_CORRECT_OPTION).click()
    
    @allure.step('Click on close button')    
    def click_on_close_button(self):
        self.driver.find_element(*SubjectiveQuestionPageLocators.CLOSE_BUTTON).click()
    
    @allure.step('Display message of response')    
    def display_message_section(self):
        return self.driver.find_element(*Locators.DISPLAY_MESSAGE)
    
    @allure.step('Row count of multiple choice question')
    def row_count_multiple_choice_question(self):
        return self.driver.find_elements(*Locators.TABLE_ROW_COUNT)
    
    @allure.step('Display required validation message')
    def required_validation(self):
        return self.driver.find_element(*Locators.PARSLEY_REQUIRED)
    
    @allure.step('Maxlength is 500 only')
    def maxlength_validation(self):
        return self.driver.find_element(*Locators.PARSLEY_MAXLENGTH)
    
    @allure.step('click on delete button')
    def click_on_delete_button(self):
        time.sleep(2)
        self.driver.find_element(*MultipleChoiceQuestionPageLocators.DELETE_BUTTON).click()
        
    @allure.step('search by question_title')    
    def search_for_question_title(self):
        return self.driver.find_element(*MultipleChoiceQuestionPageLocators.SEARCH_BY_QUESTION_TITLE)
    
    @allure.step('search by subject')
    def search_for_subject(self, subject):
        wait = WebDriverWait(self.driver, 10)
        select = wait.until(EC.presence_of_element_located((MultipleChoiceQuestionPageLocators.SEARCH_BY_SUBJECT)))
        select = Select(select)
        subject = select.select_by_visible_text(subject)
        return subject
    
    @allure.step('click on search button')
    def click_on_search_button(self):
        return self.driver.find_element(*SubjectiveQuestionPageLocators.SEARCH_BUTTON).click()
    
    @allure.step('click on edit button')
    def click_on_edit_button(self):
        return self.driver.find_element(*MultipleChoiceQuestionPageLocators.EDIT_BUTTON).click()
    
    @allure.step('get existing question text')
    def get_text_of_questions(self):
        return self.driver.find_element(*ImageBasedMultipleChoiceQuestionPageLocators.GET_QUESTION_TEXT).text
        
    @allure.step('Firstly, always run login functionality')
    def section_open_of_multiple_choice_question_section(self):
        login = Login(self.driver)
        login.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        login.click_on_multiple_choice_question_section()
    
    def add_question_multiple_choice_question(self, subject, passage, question_title, optionA, optionB, optionC, optionD, add_question, validation):
        self.section_open_of_multiple_choice_question_section()
        previous_row_length = len(self.row_count_multiple_choice_question())
        self.add_multiple_choice_question_button()
        if subject and passage and question_title:
            self.input_subject(subject)
            self.input_passage(passage)
            self.input_question_title().send_keys(question_title)
        elif subject and passage:
            self.input_subject(subject)
            self.input_passage(passage)
        elif subject and question_title:
            self.input_subject(subject)
            self.input_question_title().send_keys(question_title)
        elif subject:
            self.input_subject(subject)
        self.input_optionA().send_keys(optionA)
        self.input_optionB().send_keys(optionB)
        self.input_optionC().send_keys(optionC)
        self.input_optionD().send_keys(optionD)
        self.click_on_right_answer_button()
        if validation and add_question:
            self.click_on_save_button()
            time.sleep(2)
            assert PARSLEY_REQUIRED in self.required_validation().text
        elif add_question:
            self.click_on_save_button()            
            assert WebDriverWait(self.driver, 2).until(EC.text_to_be_present_in_element((Locators.DISPLAY_MESSAGE), QUESTION_ADDED))
        else:
            self.click_on_close_button()
            new_row_length = len(self.row_count_multiple_choice_question())
            assert previous_row_length == new_row_length

    def add_question_multiple_choice_question_with_maxlength_validation(self, subject, passage, question_title, optionA, optionB, optionC, optionD, add_question, validation):
        self.section_open_of_multiple_choice_question_section()
        self.add_multiple_choice_question_button()
        self.input_subject(subject)
        self.input_passage(passage)
        self.input_question_title().send_keys(question_title)
        self.input_optionA().send_keys(optionA)
        self.input_optionB().send_keys(optionB)
        self.input_optionC().send_keys(optionC)
        self.input_optionD().send_keys(optionD)
        self.click_on_right_answer_button()
        if validation and add_question:
            self.click_on_save_button()
            assert self.maxlength_validation().is_displayed()
        
    def delete_row_in_existing_table(self, accept):
        self.section_open_of_multiple_choice_question_section()
        previous_row_length = len(self.row_count_multiple_choice_question())
        self.click_on_delete_button()
        if accept:
            self.driver.switch_to.alert.accept()
            assert self.display_message_section().is_displayed()
        else:
            self.driver.switch_to.alert.dismiss()
            new_row_length = len(self.row_count_multiple_choice_question())
            assert previous_row_length == new_row_length
                
    def search_functionality(self, question_title, subject):
        self.section_open_of_multiple_choice_question_section()
        if question_title and subject:
            self.search_for_question_title().send_keys(question_title)
            self.search_for_subject(subject)
        elif question_title:
            self.search_for_question_title().send_keys(question_title)
        elif subject:
            self.search_for_subject(subject)
        self.click_on_search_button()
        
    def row_count_table(self):
        assert len(self.row_count_multiple_choice_question()) > ZERO
            
    def no_data_found_validation(self):
        assert self.display_message_section().is_displayed()

    def edit_row_of_existing_table(self):
        self.section_open_of_multiple_choice_question_section()
        previous_text = self.get_text_of_questions()
        self.click_on_edit_button()
        time.sleep(2)
        self.click_on_close_button()
        new_text = self.get_text_of_questions()
        assert previous_text == new_text
            
    def same_question_gives_on_presence_on_table(self, subject, passage, question_title, optionA, optionB, optionC, optionD):
        self.section_open_of_multiple_choice_question_section()
        self.add_multiple_choice_question_button()
        self.input_subject(subject)
        self.input_passage(passage)
        self.input_question_title().send_keys(question_title)
        self.input_optionA().send_keys(optionA)
        self.input_optionB().send_keys(optionB)
        self.input_optionC().send_keys(optionC)
        self.input_optionD().send_keys(optionD)
        self.click_on_right_answer_button()
        self.click_on_save_button()
        time.sleep(2)
        assert QUESTION_UNIQUE in self.display_message_section().text
