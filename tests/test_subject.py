import time
import pytest
import configparser

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Utilities.logger import logclass
from Utilities.generate_email import generate_random_string_subject
from PageObjects.LoginPage import Login
from PageObjects.SubjectPage import Subject
from PageObjects.AllowAuthenticatedUserPage import AllowAuthenticatedUser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")


@pytest.mark.usefixtures("setup_and_teardown")
class TestSubject(logclass):
    def test_add_new_subject_with_valid_data(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_add_new_subject_with_valid_data')
        subject = Subject(self.driver)
        subject.fill_the_form_add_new_subject(generate_random_string_subject())
        subject.success_message_for_subject('Subject added successfully', 'Screenshots/test_add_new_subject_with_valid_data.png')
    
    def test_add_new_subject_without_data(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_add_new_subject_without_data')
        subject = Subject(self.driver)
        subject.fill_the_form_add_new_subject('')
        subject.validation_message_for_required_subject('Screenshots/test_add_new_subject_without_data.png')
            
    def test_add_new_subject_with_numeric_data(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_add_new_subject_with_numeric_data')
        subject = Subject(self.driver)
        subject.fill_the_form_add_new_subject('1234')
        subject.validation_message_for_subject('Screenshots/test_add_new_subject_with_numeric_data.png')

    def test_add_new_subject_with_special_character_data(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_add_new_subject_with_special_character_data')
        subject = Subject(self.driver)
        subject.fill_the_form_add_new_subject('####')
        subject.validation_message_for_subject('Screenshots/test_add_new_subject_with_special_character_data.png')
    
    def test_add_new_subject_with_numeric_data_along_with_string(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_add_new_subject_with_numeric_data_along_with_string')
        subject = Subject(self.driver)
        subject.fill_the_form_add_new_subject('shubha111')
        subject.validation_message_for_subject('Screenshots/test_add_new_subject_with_numeric_data_along_with_string.png')
    
    def test_add_new_subject_with_alterat_along_with_string(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_add_new_subject_with_alterat_along_with_string')
        subject = Subject(self.driver)
        subject.fill_the_form_add_new_subject('shubha@@@@')
        subject.validation_message_for_subject('Screenshots/test_add_new_subject_with_alterat_along_with_string.png')
            
    def test_add_new_subject_with_special_character_along_with_string(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_add_new_subject_with_special_character_along_with_string')
        subject = Subject(self.driver)
        subject.fill_the_form_add_new_subject('shubha!!!!')
        subject.success_message_for_subject('Subject added successfully', 'Screenshots/test_add_new_subject_with_special_character_along_with_string.png')
            
    def test_add_new_subject_with_add_new_subject_and_click_on_cancel_button(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_add_new_subject_with_add_new_subject_and_click_on_cancel_button')
        subject = Subject(self.driver)
        subject.not_save_new_subject_click_on_cancel_button()
        
    def test_successfully_deleted_row_in_the_subject_table(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_successfully_deleted_row_in_the_subject_table')
        subject = Subject(self.driver)
        subject.delete_row_in_the_subject_table()
        
    def test_not_deleted_row_from_subject_table(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_not_deleted_row_from_subject_table')
        subject = Subject(self.driver)
        subject.not_delete_row_in_subject_table('Screenshots/test_not_deleted_row_from_subject_table.png')

    def test_existing_data_update_using_edit_button(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_existing_data_update_using_edit_button')
        subject = Subject(self.driver)
        subject.update_existing_data_in_the_subject_table_without_change('Screenshots/test_existing_data_update_using_edit_button.png')
        
    def test_click_edit_button_and_then_subject_clear_and_click_save_button(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_click_edit_button_and_then_subject_clear_and_click_save_button')
        subject = Subject(self.driver)
        subject.update_existing_subject_click_on_edit_button('')
        subject.validation_message_for_required_subject('Screenshots/test_click_edit_button_and_then_subject_clear_and_click_save_button.png')
    
    def test_click_edit_button_and_then_subject_clear_and_change_subject_then_click_save_button(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_click_edit_button_and_then_subject_clear_and_change_subject_then_click_save_button')
        subject = Subject(self.driver)
        subject.update_existing_subject_click_on_edit_button(generate_random_string_subject())
        subject.success_message_for_subject('Subject updated successfully', 'Screenshots/test_click_edit_button_and_then_subject_clear_and_change_subject_then_click_save_button.png')
            
    def test_click_edit_button_and_then_subject_clear_and_change_subject_data_with_number_then_click_save_button(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_click_edit_button_and_then_subject_clear_and_change_subject_data_with_number_then_click_save_button')
        subject = Subject(self.driver)
        subject.update_existing_subject_click_on_edit_button('asdfghj1')
        subject.validation_message_for_subject('Screenshots/test_click_edit_button_and_then_subject_clear_and_change_subject_data_with_number_then_click_save_button.png')

    def test_click_edit_button_and_then_subject_clear_and_change_subject_data_with_special_character_then_click_save_button(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_click_edit_button_and_then_subject_clear_and_change_subject_data_with_special_character_then_click_save_button')
        subject = Subject(self.driver)
        subject.update_existing_subject_click_on_edit_button('asdfghj@')
        subject.validation_message_for_subject('Screenshots/test_click_edit_button_and_then_subject_clear_and_change_subject_data_with_special_character_then_click_save_button.png')
