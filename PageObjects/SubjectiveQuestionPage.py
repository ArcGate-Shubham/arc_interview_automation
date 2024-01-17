import time
import allure
import configparser

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from PageObjects.LoginPage import Login
from Utilities.return_message import *
from Utilities.constants import *
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

class SubjectiveQuestion:
    def __init__(self, driver):
        self.driver = driver
        self.add_question_button_xpath = 'addButton'
        self.input_subject_xpath = 'id_subjects'
        self.input_passage_xpath = 'id_passage'
        self.input_question_title_xpath = 'id_question_title'
        self.input_answer_key_xpath = 'id_answer_key'
        self.input_instruction_xpath ='id_instructions'
        self.save_button_xpath = 'add_question_btn'
        self.display_message_xpath = 'notice'
        self.parsley_required_xpath = 'parsley-required'
        self.row_count_xpath = 'tbody#demo tr'
        self.close_button_xpath = 'close-dialoge'
        self.parsley_maxlength_xpath = 'parsley-maxlength'
        self.search_by_question_xpath = 'searchquestion'
        self.search_by_subject_xpath = 'id_question_id'
        self.search_button_xpath = '//button[@value="Search"]'
        self.delete_button_xpath = 'Delete'
        self.get_question_text_xpath = 'td.EditData'
        self.edit_button_xpath = 'span.editButton'
        
    def dynamic_explicit_wait(self, time_duration, by, element_name, message):
        return WebDriverWait(self.driver, time_duration).until(EC.text_to_be_present_in_element((by, element_name), message))
    
    def dynamic_explicit_wait_without_message(self, time_duration, by, element_name):
        return WebDriverWait(self.driver, time_duration).until(EC.visibility_of_element_located((by, element_name)))
    
    def dropdown_input(self, time_duration, by, locator, input_data):
        wait = WebDriverWait(self.driver, time_duration)
        select = wait.until(EC.presence_of_element_located((by, locator)))
        select = Select(select)
        input_data = select.select_by_visible_text(input_data)
        return input_data
    
    @allure.step('Click on new question button')    
    def click_on_add_question_button(self):
        self.driver.find_element(By.ID, self.add_question_button_xpath).click()
        time.sleep(2)
        
    def input_question_title(self):
        return self.driver.find_element(By.ID, self.input_question_title_xpath)
    
    def input_answer_keys(self):
        return self.driver.find_element(By.ID, self.input_answer_key_xpath)
    
    def input_instructions(self):
        return self.driver.find_element(By.ID, self.input_instruction_xpath)
    
    @allure.step('Click on save button')
    def click_on_save_button(self):
        return self.driver.find_element(By.ID, self.save_button_xpath)
    
    @allure.step('Click on close button')
    def click_on_close_button(self):
        return self.driver.find_element(By.ID, self.close_button_xpath)
    
    @allure.step('Row count of subjective question table')
    def row_count_subjective_question(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.row_count_xpath)
    
    @allure.step('Search by question_title')
    def search_by_question_title(self):
        return self.driver.find_element(By.ID, self.search_by_question_xpath)
    
    @allure.step('Search by subject')
    def search_by_subject(self):
        return self.driver.find_element(By.ID, self.search_by_subject_xpath)
    
    @allure.step('Click on search button')
    def click_on_search_button(self):
        return self.driver.find_element(By.XPATH,self.search_button_xpath)
    
    @allure.step('Click on delete button')
    def click_on_delete_button(self):
        return self.driver.find_element(By.ID, self.delete_button_xpath)
    
    @allure.step('Click on edit button')
    def click_on_edit_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.edit_button_xpath)
    
    @allure.step('get question text from existing table')
    def get_text_existing_question(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.get_question_text_xpath)
        
    @allure.step('Firstly, always run login functionality')
    def section_open_of_subjective_question_section(self):
        login = Login(self.driver)
        login.fill_username_password_input(config.get("crediential","login_username"), config.get("crediential","login_password"))
        login.click_on_subjective_question_section()
        
    def add_subjective_question(self, subject, passage, question_title, answer_keys, instructions, add_question, validation):
        self.section_open_of_subjective_question_section()
        previous_row = len(self.row_count_subjective_question())
        self.click_on_add_question_button()
        if subject:
            self.dropdown_input(TIME_DURATION, By.ID, self.input_subject_xpath, subject)
        if passage:
            self.dropdown_input(TIME_DURATION, By.ID, self.input_passage_xpath, passage)
        self.input_question_title().send_keys(question_title)
        self.input_answer_keys().send_keys(answer_keys)
        self.input_instructions().send_keys(instructions)
        if validation and add_question:
            self.click_on_save_button().click()
            if len(question_title) == LENGTH or len(answer_keys) == LENGTH or len(instructions) == LENGTH:
                assert self.dynamic_explicit_wait_without_message(TIME_DURATION, By.CLASS_NAME, self.parsley_maxlength_xpath).is_displayed()
            else:
                assert self.dynamic_explicit_wait_without_message(TIME_DURATION, By.CLASS_NAME, self.parsley_required_xpath).is_displayed()
        elif add_question:
            self.click_on_save_button().click()
            if TYPING_TEST in subject:
                assert self.dynamic_explicit_wait(TIME_DURATION, By.ID, self.display_message_xpath, TYPING_VALIDATION)
            elif EXCEL in subject:
                assert self.dynamic_explicit_wait(TIME_DURATION, By.ID, self.display_message_xpath, EXCEL_VALIDATION)
            else:
                assert self.dynamic_explicit_wait_without_message(TIME_DURATION, By.ID, self.display_message_xpath).is_displayed()
        else:
            self.click_on_close_button().click()
            new_row = len(self.row_count_subjective_question())
            assert previous_row == new_row

    def search_functionality(self, question_title, subject, validation):
        self.section_open_of_subjective_question_section()
        if question_title and subject:
            self.search_by_question_title().send_keys(question_title)
            self.dropdown_input(TIME_DURATION, By.ID, self.search_by_subject_xpath, subject)
        elif question_title:
            self.search_by_question_title().send_keys(question_title)
        elif subject:
            self.dropdown_input(TIME_DURATION, By.ID, self.search_by_subject_xpath, subject)
        self.click_on_search_button().click()
        if validation:
            assert self.dynamic_explicit_wait_without_message(TIME_DURATION, By.ID, self.display_message_xpath).is_displayed()
        else:
            assert len(self.row_count_subjective_question()) > ZERO
            
    def delete_row_in_table(self, accept):
        self.section_open_of_subjective_question_section()
        old_row = len(self.row_count_subjective_question())
        self.click_on_delete_button().click()
        if accept:
            self.driver.switch_to.alert.accept()
            assert self.dynamic_explicit_wait_without_message(TIME_DURATION, By.ID, self.display_message_xpath).is_displayed()
        else:
            self.driver.switch_to.alert.dismiss()
            new_row = len(self.row_count_subjective_question())
            assert old_row == new_row
            
    def edit_row_of_existing_table(self):
        self.section_open_of_subjective_question_section()
        previous_text = self.get_text_existing_question().get_attribute('innerText')
        self.click_on_edit_button()
        self.click_on_close_button()
        new_text = self.get_text_existing_question().get_attribute('innerText')
        assert previous_text == new_text
