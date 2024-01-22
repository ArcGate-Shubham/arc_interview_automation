import allure
import time

from PageObjects.LoginPage import Login
from PageObjects.locators import *
from Utilities.return_message import *
from Utilities.Readconfigurations import *

class Subject:
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Click on add new subject button')    
    def click_on_add_new_subject_button(self):
        self.driver.find_element(*Locators.ADD_NEW_QUESTION_BUTTON).click()
    
    @allure.step('Fill new subject input')    
    def add_new_subject_input_type(self,subject_data):
        time.sleep(2)
        self.driver.find_element(*SubjectPageLocators.INPUT_SUBJECT).send_keys(subject_data)
    
    @allure.step('Click on save button')     
    def new_subject_add_save_button(self):
        time.sleep(1)
        self.driver.find_element(*Locators.SAVE_BUTTON).click()
        
    def display_message_respect_of_subject(self):
        return self.driver.find_element(*Locators.DISPLAY_MESSAGE).text
    
    def display_error_message_respect_of_subject(self):
        return self.driver.find_element(*Locators.PARSLEY_REQUIRED).text
    
    def display_error_message_respect_of_parsley_pattern(self):
        return self.driver.find_element(*Locators.PARSLEY_PATTERN).text
    
    @allure.step('Row count of subject table') 
    def row_count_of_subject_table(self):
        return self.driver.find_elements(*Locators.TABLE_ROW_COUNT)
    
    @allure.step('Click on delete button') 
    def click_on_delete_button(self):
        self.driver.find_element(*Locators.DELETE_BUTTON).click()
    
    @allure.step('Click on edit button')    
    def click_on_edit_button(self):
        self.driver.find_element(*SubjectPageLocators.EDIT_BUTTON).click()
        
    def get_text_on_table_of_subject(self):
        element = self.driver.find_element(*SubjectPageLocators.GET_TEXT_SUBJECT).text
        return element
    
    @allure.step('Click on cancel button') 
    def click_on_cancel_button(self):
        time.sleep(2)
        self.driver.find_element(*Locators.CLOSE_BUTTON).click()
        
    def section_open_of_subject_section(self):
        login = Login(self.driver)
        login.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        login.click_on_add_subject_section()
        
    def fill_the_form_add_new_subject(self,subject_data):
        self.section_open_of_subject_section()
        self.click_on_add_new_subject_button()
        self.add_new_subject_input_type(subject_data)
        self.new_subject_add_save_button()
        
    def not_save_new_subject_click_on_cancel_button(self):
        self.section_open_of_subject_section()
        old_row = 0
        for old_row_data in self.row_count_of_subject_table():
            old_row = old_row + 1
        self.click_on_add_new_subject_button()
        self.click_on_cancel_button()
        new_row = 0
        for new_row_data in self.row_count_of_subject_table():
            new_row = new_row + 1
        assert new_row == old_row

    def delete_row_in_the_subject_table(self):
        self.section_open_of_subject_section()
        self.click_on_delete_button()
        self.driver.switch_to.alert.accept()
        assert SUBJECT_DELETED in self.display_message_respect_of_subject()    
    
    def not_delete_row_in_subject_table(self):
        self.section_open_of_subject_section()
        element = self.get_text_on_table_of_subject()
        self.click_on_delete_button()
        time.sleep(3)
        self.driver.switch_to.alert.dismiss()
        data = self.get_text_on_table_of_subject()
        assert element == data

    def update_existing_data_in_the_subject_table_without_change(self):
        self.section_open_of_subject_section()
        previous_subject = self.get_text_on_table_of_subject()
        self.click_on_edit_button()
        self.click_on_cancel_button()
        time.sleep(2)
        new_subject = self.get_text_on_table_of_subject()
        assert previous_subject == new_subject
            
    def update_existing_subject_click_on_edit_button(self, subject_data):
        self.section_open_of_subject_section()
        self.click_on_edit_button()
        time.sleep(2)
        if subject_data:
            self.driver.find_element(*SubjectPageLocators.INPUT_SUBJECT).clear()
            self.add_new_subject_input_type(subject_data)
        else:
            self.driver.find_element(*SubjectPageLocators.INPUT_SUBJECT).clear()
        self.new_subject_add_save_button()

    def validation_message_for_subject(self):
        assert START_LETTER in self.display_error_message_respect_of_parsley_pattern()
        
    def validation_message_for_required_subject(self):
        assert PARSLEY_REQUIRED in self.display_error_message_respect_of_subject()
              
    def success_message_for_subject(self, message):
        assert message in self.display_message_respect_of_subject()
