import time
import configparser

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from PageObjects.LoginPage import Login
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

class Subject:
    def __init__(self, driver):
        self.driver = driver
        self.click_on_add_new_subject_button_xpath = 'addButton'
        self.add_new_subject_input_type_xpath = 'subject'
        self.new_subject_add_save_button_xpath = 'save-button'
        self.display_message_xpath = 'notice'
        self.display_error_message_on_modal_xpath = 'parsley-required'
        self.display_error_message_for_pattern_xpath = 'parsley-pattern'
        self.total_row_count_of_table_xpath = 'tbody tr'
        self.click_on_cancel_button_xpath = 'close-button'
        self.click_on_delete_button_xpath = 'Delete'
        self.click_on_edit_button_xpath = 'span.editButton'
        self.get_text_on_table_of_subject_xpath = '//*[@id="demo"]/tr[1]/td[1]'
        
    def click_on_add_new_subject_button(self):
        self.driver.find_element(By.ID, self.click_on_add_new_subject_button_xpath).click()
        
    def add_new_subject_input_type(self,subject_data):
        time.sleep(2)
        self.driver.find_element(By.NAME, self.add_new_subject_input_type_xpath).send_keys(subject_data)
        
    def new_subject_add_save_button(self):
        time.sleep(1)
        self.driver.find_element(By.ID, self.new_subject_add_save_button_xpath).click()
        
    def display_message_respect_of_subject(self):
        return self.driver.find_element(By.ID, self.display_message_xpath).text
    
    def display_error_message_respect_of_subject(self):
        return self.driver.find_element(By.CLASS_NAME, self.display_error_message_on_modal_xpath).text
    
    def display_error_message_respect_of_parsley_pattern(self):
        return self.driver.find_element(By.CLASS_NAME, self.display_error_message_for_pattern_xpath).text
    
    def row_count_of_subject_table(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.total_row_count_of_table_xpath)
    
    def click_on_delete_button(self):
        self.driver.find_element(By.ID, self.click_on_delete_button_xpath).click()
        
    def click_on_edit_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_on_edit_button_xpath).click()
        
    def get_text_on_table_of_subject(self):
        element = self.driver.find_element(By.XPATH, self.get_text_on_table_of_subject_xpath).text
        return element
    
    def click_on_cancel_button(self):
        time.sleep(2)
        self.driver.find_element(By.ID, self.click_on_cancel_button_xpath).click()
        
    def section_open_of_subject_section(self):
        login = Login(self.driver)
        login.fill_username_password_input(config.get("crediential","login_username"), config.get("crediential","login_password"))
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
        if new_row == old_row:
            assert True
        else:
            assert False
            
    def delete_row_in_the_subject_table(self):
        self.section_open_of_subject_section()
        self.click_on_delete_button()
        self.driver.switch_to.alert.accept()
        if 'Subject deleted successfully' in self.display_message_respect_of_subject():
            assert True
        else:
            assert False
            
    def not_delete_row_in_subject_table(self, screenshot):
        self.section_open_of_subject_section()
        element = self.get_text_on_table_of_subject()
        self.click_on_delete_button()
        time.sleep(3)
        self.driver.switch_to.alert.dismiss()
        data = self.get_text_on_table_of_subject()
        if element == data:
            assert True
        else:
            self.driver.save_screenshot(screenshot)
            assert False

    def update_existing_data_in_the_subject_table_without_change(self, screenshot):
        self.section_open_of_subject_section()
        previous_subject = self.get_text_on_table_of_subject()
        self.click_on_edit_button()
        self.click_on_cancel_button()
        time.sleep(2)
        new_subject = self.get_text_on_table_of_subject()
        if previous_subject == new_subject:
            assert True
        else:
            self.driver.save_screenshot(screenshot)
            assert False
            
    def update_existing_subject_click_on_edit_button(self, subject_data):
        self.section_open_of_subject_section()
        self.click_on_edit_button()
        time.sleep(2)
        if subject_data:
            self.driver.find_element(By.NAME, self.add_new_subject_input_type_xpath).clear()
            self.add_new_subject_input_type(subject_data)
        else:
            self.driver.find_element(By.NAME, self.add_new_subject_input_type_xpath).clear()
        self.new_subject_add_save_button()

    def validation_message_for_subject(self, screenshot):
        if 'This field should start with a letter' in self.display_error_message_respect_of_parsley_pattern():
            assert True
        else:
            self.driver.save_screenshot(screenshot)
            assert False

    def validation_message_for_required_subject(self, screenshot):
        if 'This field is required.' in self.display_error_message_respect_of_subject():
            assert True
        else:
            self.driver.save_screenshot(screenshot)
            assert False
            
    def success_message_for_subject(self, message ,screenshot):
        if message in self.display_message_respect_of_subject():
            assert True
        else:
            self.driver.save_screenshot(screenshot)
            assert False
