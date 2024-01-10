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
        
    def dynamic_explicit_wait(self, time_duration, element_name, message):
        return WebDriverWait(self.driver, time_duration).until(EC.text_to_be_present_in_element((By.ID, element_name), message))
    
    def dynamic_explicit_wait_without_message(self, time_duration, by, element_name):
        return WebDriverWait(self.driver, time_duration).until(EC.visibility_of_element_located((by, element_name)))
    
    def dropdown_input(self, time_duration, by, locator, input_data):
        wait = WebDriverWait(self.driver, time_duration)
        select = wait.until(EC.presence_of_element_located((by, locator)))
        select = Select(select)
        input_data = select.select_by_visible_text(input_data)
        return input_data
    
    @allure.step('click on new question button')    
    def click_on_add_question_button(self):
        self.driver.find_element(By.ID, self.add_question_button_xpath).click()
        time.sleep(2)
        
    def input_question_title(self):
        return self.driver.find_element(By.ID, self.input_question_title_xpath)
    
    def input_answer_keys(self):
        return self.driver.find_element(By.ID, self.input_answer_key_xpath)
    
    def input_instructions(self):
        return self.driver.find_element(By.ID, self.input_instruction_xpath)
    
    def click_on_save_button(self):
        return self.driver.find_element(By.ID, self.save_button_xpath)
    
    def click_on_close_button(self):
        return self.driver.find_element(By.ID, self.close_button_xpath)
    
    def row_count_subjective_question(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.row_count_xpath)
        
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
            assert self.dynamic_explicit_wait_without_message(TIME_DURATION, By.CLASS_NAME, self.parsley_required_xpath).is_displayed()
        elif add_question:
            self.click_on_save_button().click()
            assert self.dynamic_explicit_wait_without_message(TIME_DURATION, By.ID, self.display_message_xpath).is_displayed()
        else:
            self.click_on_close_button().click()
            new_row = len(self.row_count_subjective_question())
            assert previous_row == new_row
