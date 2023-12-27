import time
import configparser

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from PageObjects.LoginPage import Login
from Utilities.return_message import *
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

class MultipleChoiceQuestion:
    def __init__(self, driver):
        self.driver = driver
        self.add_multiple_choice_question_button_xpath = 'add_mcq'
        self.input_subject_xpath = '//select[@id="MCQ_subject"]/option[5]'
        self.subject_input_xpath = 'MCQ_subject'
        self.passage_input_xpath = 'MCQ_passage'
        self.question_title_xpath = 'MCQ_title'
        self.optionA_xpath = 'MCQ_optionA'
        self.optionB_xpath = 'MCQ_optionB'
        self.optionC_xpath = 'MCQ_optionC'
        self.optionD_xpath = 'MCQ_optionD'
        self.save_button_xpath = 'add_question_btn'
        self.click_on_right_answer_xpath = 'chkboxOption2'
        self.cancel_button_xpath = 'close-dialoge'
        self.display_message_xpath = 'notice'
        self.row_count_xpath = 'tbody#demo tr'
        self.parsley_required_validation_xpath = 'parsley-required'
        
    def add_multiple_choice_question_button(self):
        time.sleep(2)
        self.driver.find_element(By.ID, self.add_multiple_choice_question_button_xpath).click()
        
    def input_subject(self, subject):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        select = wait.until(EC.presence_of_element_located((By.ID, self.subject_input_xpath)))
        select = Select(select)
        subject = select.select_by_visible_text(subject)
        return subject
    
    def input_passage(self, passage):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        select = wait.until(EC.presence_of_element_located((By.ID, self.passage_input_xpath)))
        select = Select(select)
        passage = select.select_by_visible_text(passage)
        return passage
    
    def input_question_title(self):
        return self.driver.find_element(By.ID, self.question_title_xpath)
    
    def input_optionA(self):
        return self.driver.find_element(By.ID, self.optionA_xpath)
    
    def input_optionB(self):
        return self.driver.find_element(By.ID, self.optionB_xpath)
    
    def input_optionC(self):
        return self.driver.find_element(By.ID, self.optionC_xpath)
    
    def input_optionD(self):
        return self.driver.find_element(By.ID, self.optionD_xpath)
    
    def click_on_save_button(self):
        self.driver.find_element(By.ID, self.save_button_xpath).click()
        
    def click_on_right_answer_button(self):
        self.driver.find_element(By.ID, self.click_on_right_answer_xpath).click()
        
    def click_on_close_button(self):
        self.driver.find_element(By.ID, self.cancel_button_xpath).click()
        
    def display_message_section(self):
        return self.driver.find_element(By.ID, self.display_message_xpath)
    
    def row_count_multiple_choice_question(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.row_count_xpath)
    
    def required_validation(self):
        return self.driver.find_element(By.CLASS_NAME, self.parsley_required_validation_xpath)

    def section_open_of_multiple_choice_question_section(self):
        login = Login(self.driver)
        login.fill_username_password_input(config.get("crediential","login_username"), config.get("crediential","login_password"))
        login.click_on_multiple_choice_question_section()
        
    def add_question_multiple_choice_question(self, subject, passage, question_title, optionA, optionB, optionC, optionD, add_question, validation, screenshot):
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
            if PARSLEY_REQUIRED in self.required_validation().text:
                assert True
            else:
                self.driver.save_screenshot(screenshot)
                assert False
        elif add_question:
            self.click_on_save_button()            
            try:
                WebDriverWait(self.driver, 2).until(EC.text_to_be_present_in_element((By.ID, self.display_message_xpath), QUESTION_ADDED))
                assert True
            except Exception as e:
                self.driver.save_screenshot(screenshot)
                assert False
        else:
            self.click_on_close_button()
            new_row_length = len(self.row_count_multiple_choice_question())
            if previous_row_length == new_row_length:
                assert True
            else:
                self.driver.save_screenshot(screenshot)
                assert False
