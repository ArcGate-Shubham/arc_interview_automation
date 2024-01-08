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

class ImageBasedMultipleChoiceQuestion:
    def __init__(self, driver):
        self.driver = driver
        self.click_on_add_question_button_xpath = 'AddRecordBtn'
        self.input_subject_xpath = 'image_MCQ_subject'
        self.input_question_title_xpath = 'image_MCQ_title'
        self.optionA_xpath = 'image_MCQ_optionA'
        self.optionB_xpath = 'image_MCQ_optionB'
        self.optionC_xpath = 'image_MCQ_optionC'
        self.optionD_xpath = 'image_MCQ_optionD'
        self.checked_on_correct_option_xpath = 'chkboxOption2'
        self.save_button_xpath = 'add_question_btn'
        self.image_upload_xpath = 'MCQ_image_upload'
        self.display_message_xpath = 'notice'
        self.row_count_xpath = 'tbody#demo tr'
        self.close_button_xpath = 'close-dialoge'
        self.parsley_required_xpath = 'parsley-required'
        self.search_by_question_title_xpath = 'id_question_title'
        self.search_by_subject_xpath = 'id_subject'
        self.click_on_search_button_xpath = 'input.btn-primary'
        self.edit_button_xpath = 'a.Edit'
        self.delete_button_xpath = 'Delete'
        self.get_question_text_xpath = 'td h5'
        
    def dynamic_explicit_wait(self, time_duration, element_name, message):
        return WebDriverWait(self.driver, time_duration).until(EC.text_to_be_present_in_element((By.ID, element_name), message))
    
    def dynamic_explicit_wait_without_message(self, time_duration, element_name):
        return WebDriverWait(self.driver, time_duration).until(EC.visibility_of_element_located((By.CLASS_NAME, element_name)))
        
    @allure.step('click on new question button')    
    def click_on_add_question_button(self):
        self.driver.find_element(By.CLASS_NAME, self.click_on_add_question_button_xpath).click()
        time.sleep(2)
        
    def input_subject(self, subject):
        wait = WebDriverWait(self.driver, 10)
        select = wait.until(EC.presence_of_element_located((By.ID, self.input_subject_xpath)))
        select = Select(select)
        subject = select.select_by_visible_text(subject)
        return subject
    
    def input_question_title(self):
        return self.driver.find_element(By.ID, self.input_question_title_xpath)
    
    def input_optionA(self):
        return self.driver.find_element(By.ID, self.optionA_xpath)
    
    def input_optionB(self):
        return self.driver.find_element(By.ID, self.optionB_xpath)
    
    def input_optionC(self):
        return self.driver.find_element(By.ID, self.optionC_xpath)
    
    def input_optionD(self):
        return self.driver.find_element(By.ID, self.optionD_xpath)
    
    @allure.step('checked on correct options')
    def checked_on_correct_option(self):
        return self.driver.find_element(By.ID, self.checked_on_correct_option_xpath)
    
    @allure.step('click on save button')
    def click_on_save_button(self):
        return self.driver.find_element(By.ID, self.save_button_xpath)
    
    def input_image_upload(self):
        return self.driver.find_element(By.ID, self.image_upload_xpath)
    
    @allure.step('Display message of response')    
    def display_message_section(self):
        return self.driver.find_element(By.ID, self.display_message_xpath)
    
    @allure.step('Row count of multiple choice question')
    def row_count_image_based_multiple_choice_question(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.row_count_xpath)
    
    @allure.step('click on close button')
    def click_on_close_button(self):
        return self.driver.find_element(By.ID, self.close_button_xpath)
    
    def required_validation(self):
        return self.driver.find_element(By.CLASS_NAME, self.parsley_required_xpath)
    
    def search_by_question_title(self):
        return self.driver.find_element(By.ID, self.search_by_question_title_xpath)
       
    def search_by_subject(self, subject):
        wait = WebDriverWait(self.driver, 10)
        select = wait.until(EC.presence_of_element_located((By.ID, self.search_by_subject_xpath)))
        select = Select(select)
        subject = select.select_by_visible_text(subject)
        return subject
    
    @allure.step('Click on search button')
    def click_on_search_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.click_on_search_button_xpath)
    
    @allure.step('Click on edit button')
    def click_on_edit_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.edit_button_xpath)
    
    @allure.step('Click on delete button')
    def click_on_delete_button(self):
        return self.driver.find_element(By.ID, self.delete_button_xpath)
    
    @allure.step('get text from question')
    def get_text_of_questions(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.get_question_text_xpath)
    
    @allure.step('Firstly, always run login functionality')
    def section_open_of_image_based_multiple_choice_question_section(self):
        login = Login(self.driver)
        login.fill_username_password_input(config.get("crediential","login_username"), config.get("crediential","login_password"))
        login.click_on_image_based_multiple_choice_question_section()
        
    def add_image_based_multiple_choice_question(self, subject, question_title, optionA, optionB, optionC, optionD, image, add_question, validation):
        self.section_open_of_image_based_multiple_choice_question_section()
        previous_row_length = len(self.row_count_image_based_multiple_choice_question())
        self.click_on_add_question_button()
        self.input_subject(subject)
        self.input_question_title().send_keys(question_title)
        self.input_optionA().send_keys(optionA)
        self.input_optionB().send_keys(optionB)
        self.input_optionC().send_keys(optionC)
        self.input_optionD().send_keys(optionD)
        self.checked_on_correct_option().click()
        self.input_image_upload().send_keys(image)
        if validation and add_question:
            self.click_on_save_button().click()
            assert self.dynamic_explicit_wait_without_message(TIME_DURATION, self.parsley_required_xpath).is_displayed()
        elif add_question:
            self.click_on_save_button().click()
            assert self.dynamic_explicit_wait(TIME_DURATION, self.display_message_xpath, QUESTION_ADDED)
        else:
            self.click_on_close_button().click()
            new_row_length = len(self.row_count_image_based_multiple_choice_question())
            assert previous_row_length == new_row_length
            
    def search_functionality(self, question_title, subject, validation):
        self.section_open_of_image_based_multiple_choice_question_section()
        if question_title and subject:
            self.search_by_question_title().send_keys(question_title)
            self.search_by_subject(subject)
        elif question_title:
            self.search_by_question_title().send_keys(question_title)
        elif subject:
            self.search_by_subject(subject)
        self.click_on_search_button().click()
        if validation:
            assert self.dynamic_explicit_wait(TIME_DURATION, self.display_message_xpath, NO_DATA)
        else:
            assert len(self.row_count_image_based_multiple_choice_question()) > ZERO
            
    def delete_row_in_table(self, accept):
        self.section_open_of_image_based_multiple_choice_question_section()
        old_row = len(self.row_count_image_based_multiple_choice_question())
        self.click_on_delete_button().click()
        if accept:
            self.driver.switch_to.alert.accept()
            assert self.dynamic_explicit_wait(TIME_DURATION, self.display_message_xpath, QUESTION_DELETED)
        else:
            self.driver.switch_to.alert.dismiss()
            new_row = len(self.row_count_image_based_multiple_choice_question())
            assert old_row == new_row
            
    def edit_row_of_existing_table(self):
        self.section_open_of_image_based_multiple_choice_question_section()
        previous_text = self.get_text_of_questions().get_attribute('innerText')
        self.click_on_edit_button()
        self.click_on_close_button()
        new_text = self.get_text_of_questions().get_attribute('innerText')
        assert previous_text == new_text
