import time
import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from PageObjects.LoginPage import Login
from PageObjects.locators import *
from Utilities.logger import logclass
from Utilities.return_message import *
from Utilities.Readconfigurations import *

class MultipleImageChoiceQuestion(logclass):
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Click on add new question button')    
    def click_on_add_new_question_button(self):
        time.sleep(1)
        self.driver.find_element(*Locators.ADD_NEW_QUESTION_BUTTON).click()
    
    @allure.step('Table row count of table')       
    def row_count_of_existing_table(self):
        return self.driver.find_elements(*Locators.TABLE_ROW_COUNT)
    
    @allure.step('Click on close button')   
    def click_on_close_button(self):
        time.sleep(1)
        self.driver.find_element(*SubjectiveQuestionPageLocators.CLOSE_BUTTON).click()
        
    def input_question_title(self, question_title):
        time.sleep(1)
        return self.driver.find_element(*MultipleImageChoiceQuestionPageLocators.INPUT_QUESTION_TITLE).send_keys(question_title)
    
    def input_optionA(self,optionA):
        time.sleep(1)
        return self.driver.find_element(*MultipleImageChoiceQuestionPageLocators.INPUT_OPTION_A).send_keys(optionA)
    
    def input_optionB(self,optionB):
        time.sleep(2)
        return self.driver.find_element(*MultipleImageChoiceQuestionPageLocators.INPUT_OPTION_B).send_keys(optionB)
    
    def input_optionC(self, optionC):
        time.sleep(2)
        return self.driver.find_element(*MultipleImageChoiceQuestionPageLocators.INPUT_OPTION_C).send_keys(optionC)
    
    def input_optionD(self, optionD):
        time.sleep(2)
        return self.driver.find_element(*MultipleImageChoiceQuestionPageLocators.INPUT_OPTION_D).send_keys(optionD)
    
    @allure.step('Click on save button')   
    def add_question_button(self):
        time.sleep(2)
        self.driver.find_element(*SubjectiveQuestionPageLocators.SAVE_BUTTON).click()
    
    @allure.step('Checked on correct answer')       
    def checked_right_answer_options(self):
        time.sleep(1)
        self.driver.find_element(*MultipleImageChoiceQuestionPageLocators.CHECKED_ON_CORRECT_OPTION).click()
    
    @allure.step('After click on save button then display message')       
    def display_success_message(self):
        time.sleep(1)
        return self.driver.find_element(*Locators.DISPLAY_MESSAGE).text
    
    @allure.step('After click on save button then display required validation message')   
    def display_validation_message(self):
        time.sleep(1)
        return self.driver.find_element(*Locators.PARSLEY_REQUIRED).text
    
    def search_by_question_title(self):
        return self.driver.find_element(*SubjectiveQuestionPageLocators.INPUT_QUESTION_TITLE)
    
    def search_by_subject(self):
        return self.driver.find_element(*ImageBasedMultipleChoiceQuestionPageLocators.SEARCH_BY_SUBJECT)
    
    @allure.step('Click on search button')
    def click_on_search_button(self):
        time.sleep(2)
        self.driver.find_element(*AllowAuthenticatedUserPageLocators.SEARCH_BUTTON).click()
    
    @allure.step('Click on delete button')    
    def click_on_delete_button(self):
        time.sleep(2)
        self.driver.find_element(*Locators.DELETE_BUTTON).click()
    
    @allure.step('Click on edit button')    
    def click_on_edit_button(self):
        time.sleep(2)
        self.driver.find_element(*Locators.EDIT_BUTTON).click()
    
    @allure.step('get existing question text')    
    def get_text_of_questions(self):
        time.sleep(2)
        return self.driver.find_element(*MultipleImageChoiceQuestionPageLocators.GET_QUESTION_TEXT).text

    def section_open_of_multiple_image_choice_question_section(self):
        login = Login(self.driver)
        login.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        login.click_on_multiple_image_choice_question_section()
        
    def add_new_question_multiple_image_choice_question(self):
        self.section_open_of_multiple_image_choice_question_section()
        old_row = 0
        for old_row_data in self.row_count_of_existing_table():
            old_row = old_row + 1
        self.click_on_add_new_question_button()
        self.click_on_close_button()
        new_row = 0
        for new_row_data in self.row_count_of_existing_table():
            new_row = new_row + 1
        assert old_row == new_row
            
    def add_new_question_with_all_valid_input(self,question_title, optionA, optionB, optionC, optionD, add_question):
        self.section_open_of_multiple_image_choice_question_section()
        self.click_on_add_new_question_button()
        self.input_question_title(question_title)
        self.driver.find_element(*MultipleImageChoiceQuestionPageLocators.INPUT_SUBJECT).click()
        if optionA: 
            self.input_optionA(optionA)
        if optionB:
            self.input_optionB(optionB)
        if optionC:
            self.input_optionC(optionC)
        if optionD:
            self.input_optionD(optionD)
        if optionA and optionC:
            self.input_optionA(optionA)
            self.input_optionC(optionC)
        if optionA and optionB:
            self.input_optionA(optionA)
            self.input_optionB(optionB)
        if optionA and optionD:
            self.input_optionA(optionA)
            self.input_optionD(optionD)
        if optionA and optionB and optionC:
            self.input_optionA(optionA)
            self.input_optionB(optionB)
            self.input_optionC(optionC)
        if optionA and optionB and optionC and optionD:
            self.input_optionA(optionA)
            self.input_optionB(optionB)
            self.input_optionC(optionC)
            self.input_optionD(optionD)
        self.checked_right_answer_options()
        if add_question:
            self.add_question_button()
        else:
            self.click_on_close_button()
        time.sleep(1)
        
    def display_validation_messsage_required(self):
        assert PARSLEY_REQUIRED in self.display_validation_message()
            
    def display_success_message_for_multiple_image_choice_question(self, message):
        assert message in self.display_success_message()

    def search_functionality_for_multiple_image_choice_question(self, question_title, subject):
        self.section_open_of_multiple_image_choice_question_section()
        if question_title:
            self.search_by_question_title().send_keys(question_title)
        if subject:
            wait = WebDriverWait(self.driver, 10)
            select = wait.until(EC.presence_of_element_located((ImageBasedMultipleChoiceQuestionPageLocators.SEARCH_BY_SUBJECT)))
            select = Select(select)
            subject = select.select_by_visible_text(subject)
        self.click_on_search_button()
        time.sleep(2)
        return subject
    
    def search_after_row_count(self):
        assert self.row_count_of_existing_table()

    def delete_row_in_existing_table(self, accept):
        self.section_open_of_multiple_image_choice_question_section()
        old_row = 0
        for old_row_data in self.row_count_of_existing_table():
            old_row = old_row + 1
        self.click_on_delete_button()
        if accept:
            self.driver.switch_to.alert.accept()
            assert QUESTION_DELETED in self.display_success_message()
        else:
            self.driver.switch_to.alert.dismiss()
            new_row = 0
            for new_row_data in self.row_count_of_existing_table():
                new_row = new_row + 1
            assert old_row == new_row
                
    def edit_row_in_existing_table(self, close, clear,clear_subject):
        self.section_open_of_multiple_image_choice_question_section()
        previous_question = self.get_text_of_questions()
        self.click_on_edit_button()
        if close:
            self.click_on_close_button()
            new_question = self.get_text_of_questions()
            assert previous_question == new_question
        else:
            if clear and clear_subject:
                time.sleep(5)
                self.driver.find_element(*MultipleImageChoiceQuestionPageLocators.INPUT_QUESTION_TITLE).clear()
                self.driver.find_element(*MultipleImageChoiceQuestionPageLocators.CLICK_EDIT_BUTTON_SELECT_SUBJECT_DROPDOWN).click()
                self.add_question_button()
                time.sleep(2)
                assert PARSLEY_REQUIRED in self.display_validation_message()
            elif clear:
                time.sleep(5)
                self.driver.find_element(*MultipleImageChoiceQuestionPageLocators.INPUT_QUESTION_TITLE).clear()
                self.add_question_button()
                time.sleep(2)
                assert PARSLEY_REQUIRED in self.display_validation_message()
            elif clear_subject:
                time.sleep(5)
                self.driver.find_element(*MultipleImageChoiceQuestionPageLocators.CLICK_EDIT_BUTTON_SELECT_SUBJECT_DROPDOWN).click()
                self.add_question_button()
                time.sleep(2)
                assert PARSLEY_REQUIRED in self.display_validation_message()
            else:
                self.add_question_button()
                assert QUESTION_UPDATE in self.display_success_message()
                    
    def edit_question_of_existing_table_using_change_question(self, question_title, subject):
        self.section_open_of_multiple_image_choice_question_section()
        self.click_on_edit_button()
        time.sleep(2)
        if question_title and subject:
            self.driver.find_element(*MultipleImageChoiceQuestionPageLocators.INPUT_QUESTION_TITLE).clear()
            self.driver.find_element(*MultipleImageChoiceQuestionPageLocators.INPUT_QUESTION_TITLE).send_keys(question_title)
            self.driver.find_element(*MultipleImageChoiceQuestionPageLocators.UPDATE_INPUT_SUBJECT).click()
        elif question_title:
            self.driver.find_element(*MultipleImageChoiceQuestionPageLocators.INPUT_QUESTION_TITLE).clear()
            self.driver.find_element(*MultipleImageChoiceQuestionPageLocators.INPUT_QUESTION_TITLE).send_keys(question_title)
        elif subject:
            self.driver.find_element(*MultipleImageChoiceQuestionPageLocators.UPDATE_INPUT_SUBJECT).click()
        self.add_question_button()
        assert QUESTION_UPDATE in self.display_success_message()
