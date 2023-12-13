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
        log.info("Test Case Starting")
        subject = Subject(self.driver)
        subject.fill_the_form_add_new_subject(generate_random_string_subject())
        if 'Subject added successfully' in subject.display_message_respect_of_subject():
            assert True
        else:
            self.driver.save_screenshot('Screenshots/test_add_new_subject_with_valid_data.png')
            assert False
    
    def test_add_new_subject_without_data(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_add_new_subject_without_data')
        log.info("Test Case Starting")
        subject = Subject(self.driver)
        subject.fill_the_form_add_new_subject('')
        if 'This field is required.' in subject.display_error_message_respect_of_subject():
            assert True
        else:
            self.driver.save_screenshot('Screenshots/test_add_new_subject_without_data.png')
            assert False
            
    def test_add_new_subject_with_numeric_data(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_add_new_subject_with_numeric_data')
        log.info("Test Case Starting")
        subject = Subject(self.driver)
        subject.fill_the_form_add_new_subject('1234')
        if "This field should start with a letter and doesn't accept digits" in subject.display_error_message_respect_of_parsley_pattern():
            assert True
        else:
            self.driver.save_screenshot('Screenshots/test_add_new_subject_with_numeric_data.png')
            assert False

    def test_add_new_subject_with_special_character_data(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_add_new_subject_with_special_character_data')
        log.info("Test Case Starting")
        subject = Subject(self.driver)
        subject.fill_the_form_add_new_subject('####')
        if "This field should start with a letter and doesn't accept digits" in subject.display_error_message_respect_of_parsley_pattern():
            assert True
        else:
            self.driver.save_screenshot('Screenshots/test_add_new_subject_with_special_character_data.png')
            assert False
    
    def test_add_new_subject_with_numeric_data_along_with_string(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_add_new_subject_with_numeric_data_along_with_string')
        log.info("Test Case Starting")
        subject = Subject(self.driver)
        subject.fill_the_form_add_new_subject('shubha111')
        if "This field should start with a letter and doesn't accept digits" in subject.display_error_message_respect_of_parsley_pattern():
            assert True
        else:
            self.driver.save_screenshot('Screenshots/test_add_new_subject_with_numeric_data_along_with_string.png')
            assert False
    
    def test_add_new_subject_with_alterat_along_with_string(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_add_new_subject_with_alterat_along_with_string')
        log.info("Test Case Starting")
        subject = Subject(self.driver)
        subject.fill_the_form_add_new_subject('shubha@@@@')
        if "This field should start with a letter and doesn't accept digits" in subject.display_error_message_respect_of_parsley_pattern():
            assert True
        else:
            self.driver.save_screenshot('Screenshots/test_add_new_subject_with_alterat_along_with_string.png')
            assert False
            
    def test_add_new_subject_with_special_character_along_with_string(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_add_new_subject_with_special_character_along_with_string')
        log.info("Test Case Starting")
        subject = Subject(self.driver)
        subject.fill_the_form_add_new_subject('shubha!!!!')
        if 'Subject added successfully' in subject.display_message_respect_of_subject():
            assert True
        else:
            self.driver.save_screenshot('Screenshots/test_add_new_subject_with_special_character_along_with_string.png')
            assert False
            
    def test_add_new_subject_with_add_new_subject_and_click_on_cancel_button(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_add_new_subject_with_add_new_subject_and_click_on_cancel_button')
        log.info("Test Case Starting")
        subject = Subject(self.driver)
        subject.not_save_new_subject_click_on_cancel_button()
        
    def test_successfully_deleted_row_in_the_subject_table(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_successfully_deleted_row_in_the_subject_table')
        log.info("Test Case Starting")
        subject = Subject(self.driver)
        subject.delete_row_in_the_subject_table()
        
    def test_not_deleted_row_from_subject_table(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_not_deleted_row_from_subject_table')
        log.info("Test Case Starting")
        subject = Subject(self.driver)
        subject.not_delete_row_in_subject_table('Screenshots/test_not_deleted_row_from_subject_table.png')
