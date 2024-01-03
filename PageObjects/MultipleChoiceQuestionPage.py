import time
import allure
import configparser

from allure_commons.types import AttachmentType
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
        self.parsley_maxlength_validation_xpath = 'li.parsley-maxlength'
        self.click_on_delete_button_xpath = 'btn-danger'
        self.search_for_question_title_xpath = 'MCQ_title_search'
        self.search_for_subject_xpath = 'MCQ_subject_search'
        self.click_on_search_button_xpath = 'Search'
        self.click_on_edit_button_xpath = 'a.edit_mcq'
        self.get_question_text_xpath = 'td h5'
     
    @allure.step('click on add multiple choice question')    
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
    
    @allure.step('Fill all detail of multiple choice question form after that click on save button')
    def click_on_save_button(self):
        self.driver.find_element(By.ID, self.save_button_xpath).click()
    
    @allure.step('Checked on correct answer check box of muliple choice question options')    
    def click_on_right_answer_button(self):
        self.driver.find_element(By.ID, self.click_on_right_answer_xpath).click()
    
    @allure.step('Click on close button')    
    def click_on_close_button(self):
        self.driver.find_element(By.ID, self.cancel_button_xpath).click()
    
    @allure.step('Display message of response')    
    def display_message_section(self):
        return self.driver.find_element(By.ID, self.display_message_xpath)
    
    @allure.step('Row count of multiple choice question')
    def row_count_multiple_choice_question(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.row_count_xpath)
    
    @allure.step('Display required validation message')
    def required_validation(self):
        return self.driver.find_element(By.CLASS_NAME, self.parsley_required_validation_xpath)
    
    @allure.step('Maxlength is 500 only')
    def maxlength_validation(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.parsley_maxlength_validation_xpath)
    
    @allure.step('click on delete button')
    def click_on_delete_button(self):
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, self.click_on_delete_button_xpath).click()
        
    @allure.step('search by question_title')    
    def search_for_question_title(self):
        return self.driver.find_element(By.ID, self.search_for_question_title_xpath)
    
    @allure.step('search by subject')
    def search_for_subject(self, subject):
        wait = WebDriverWait(self.driver, 10)
        select = wait.until(EC.presence_of_element_located((By.ID, self.search_for_subject_xpath)))
        select = Select(select)
        subject = select.select_by_visible_text(subject)
        return subject
    
    @allure.step('click on search button')
    def click_on_search_button(self):
        return self.driver.find_element(By.ID, self.click_on_search_button_xpath).click()
    
    @allure.step('click on edit button')
    def click_on_edit_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.click_on_edit_button_xpath).click()
    
    @allure.step('get existing question text')
    def get_text_of_questions(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.get_question_text_xpath).text
        
    @allure.step('Firstly, always run login functionality')
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
                allure.attach(self.driver.get_screenshot_as_png(), name=screenshot, attachment_type=AttachmentType.PNG)
                assert False
        elif add_question:
            self.click_on_save_button()            
            try:
                WebDriverWait(self.driver, 2).until(EC.text_to_be_present_in_element((By.ID, self.display_message_xpath), QUESTION_ADDED))
                assert True
            except Exception as e:
                allure.attach(self.driver.get_screenshot_as_png(), name=screenshot, attachment_type=AttachmentType.PNG)
                assert False
        else:
            self.click_on_close_button()
            new_row_length = len(self.row_count_multiple_choice_question())
            if previous_row_length == new_row_length:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name=screenshot, attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot(screenshot)
                assert False

    def add_question_multiple_choice_question_with_maxlength_validation(self, subject, passage, question_title, optionA, optionB, optionC, optionD, add_question, validation, screenshot):
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
            if self.maxlength_validation().is_displayed():
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name=screenshot, attachment_type=AttachmentType.PNG)
                assert False
        
    def delete_row_in_existing_table(self, accept, screenshot):
        self.section_open_of_multiple_choice_question_section()
        previous_row_length = len(self.row_count_multiple_choice_question())
        self.click_on_delete_button()
        if accept:
            self.driver.switch_to.alert.accept()
            if self.display_message_section().is_displayed():
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name=screenshot, attachment_type=AttachmentType.PNG)
                assert False
        else:
            self.driver.switch_to.alert.dismiss()
            new_row_length = len(self.row_count_multiple_choice_question())
            if previous_row_length == new_row_length:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name=screenshot, attachment_type=AttachmentType.PNG)
                assert False
                
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
        
    def row_count_table(self, screenshot):
        if len(self.row_count_multiple_choice_question()) > 0:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot, attachment_type=AttachmentType.PNG)
            assert False
            
    def no_data_found_validation(self, screenshot):
        if self.display_message_section().is_displayed():
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot, attachment_type=AttachmentType.PNG)
            assert False

    def edit_row_of_existing_table(self, screenshot):
        self.section_open_of_multiple_choice_question_section()
        previous_text = self.get_text_of_questions()
        self.click_on_edit_button()
        time.sleep(2)
        self.click_on_close_button()
        new_text = self.get_text_of_questions()
        if previous_text == new_text:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot, attachment_type=AttachmentType.PNG)
            assert False
