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
        
    def section_open_of_multiple_choice_question_section(self):
        login = Login(self.driver)
        login.fill_username_password_input(config.get("crediential","login_username"), config.get("crediential","login_password"))
        login.click_on_multiple_choice_question_section()
        
    def add_question_multiple_choice_question(self, subject, passage):
        self.section_open_of_multiple_choice_question_section()
        self.add_multiple_choice_question_button()
        self.input_subject(subject)
        self.input_passage(passage)
        time.sleep(2)
 