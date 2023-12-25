import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.fill_username_input_xpath = 'username'
        self.fill_password_input_xpath = 'password'
        self.click_on_login_button_xpath = 'login_button'
        self.display_message_xpath = 'notice'
        self.click_text_allow_authenticated_user_xpath = 'Allow Authenticated User'
        self.click_text_add_subject_xpath = 'Add Subject'
        self.click_text_multiple_image_choice_question_xpath = 'Multiple Image Choice Question'
        self.click_text_multiple_choice_question_xpath = 'Multiple Choice Question'
        
    def fill_username_password_input(self, Username, Password):
        self.driver.find_element(By.NAME,self.fill_username_input_xpath).send_keys(Username)
        time.sleep(3)
        self.driver.find_element(By.NAME,self.fill_password_input_xpath).send_keys(Password)
        time.sleep(3)
        self.driver.find_element(By.ID,self.click_on_login_button_xpath).click()
        time.sleep(3)

        
    def display_successfully_login_message(self):
        return self.driver.find_element(By.ID, self.display_message_xpath).text
        
    def display_invalid_crediential_message(self):
        return self.driver.find_element(By.ID, self.display_message_xpath).text
    
    def display_admin_login_text(self):
        return self.driver.find_element(By.ID, self.click_on_login_button_xpath).text
    
    def click_on_allow_authenticated_user_section(self):
        self.driver.find_element(By.LINK_TEXT, self.click_text_allow_authenticated_user_xpath).click()
        
    def click_on_add_subject_section(self):
        return self.driver.find_element(By.LINK_TEXT, self.click_text_add_subject_xpath).click()
    
    def click_on_multiple_image_choice_question_section(self):
        return self.driver.find_element(By.LINK_TEXT, self.click_text_multiple_image_choice_question_xpath).click()
    
    def click_on_multiple_choice_question_section(self):
        return self.driver.find_element(By.LINK_TEXT, self.click_text_multiple_choice_question_xpath).click()
