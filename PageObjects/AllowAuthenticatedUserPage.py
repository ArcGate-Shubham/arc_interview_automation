import time
import configparser

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from PageObjects.LoginPage import Login
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

class AllowAuthenticatedUser:
    def __init__(self, driver):
        self.driver = driver
        self.click_on_add_user_button_xpath = 'addButton'
        self.fill_input_username_in_authenticated_user_xpath = 'userSettingUsername'
        self.fill_input_email_in_authenticated_user_xpath = 'userSettingEmail'
        self.fill_input_roll_in_authenticated_user_xpath = 'userSettingRole'
        self.fill_input_status_in_authenticated_user_xpath = 'userSettingStatus'
        self.click_on_allow_authenticated_user_save_button_xpath = 'save-button'
        self.display_meesage_in_notice_id_on_top_xpath = 'notice'
        self.required_validation_for_input_type_xpath = 'parsley-required'
        self.click_on_authenticated_user_cancel_button_xpath = 'close-button'
        self.pattern_validation_for_input_type_xpath = 'parsley-pattern'
        self.search_username_for_authenticated_user_section_xpath = 'id_username'
        self.search_email_for_authenticated_user_section_xpath = 'id_email'
        self.search_role_for_authenticated_user_section_xpath = 'id_role'
        self.search_button_for_authenticated_user_section_xpath = '//input[@value="Search"]'
        self.display_username_in_this_table_on_td_xpath = 'td'
        
    def click_on_add_user_button(self):
        self.driver.find_element(By.ID, self.click_on_add_user_button_xpath).click()
        
    def fill_the_form_allow_authenticated_user(self, Username, Email, Role, Status):
        login = Login(self.driver)
        login.fill_username_password_input(config.get("crediential","login_username"), config.get("crediential","login_password"))
        login.click_on_allow_authenticated_user_section()
        self.click_on_add_user_button()
        time.sleep(2)
        username = self.driver.find_element(By.ID, self.fill_input_username_in_authenticated_user_xpath).send_keys(Username)
        email = self.driver.find_element(By.ID, self.fill_input_email_in_authenticated_user_xpath).send_keys(Email)
        
        wait = WebDriverWait(self.driver, 10)
        select = wait.until(EC.presence_of_element_located((By.ID, self.fill_input_roll_in_authenticated_user_xpath)))
        select = Select(select)
        role = select.select_by_visible_text(Role)
        
        select = wait.until(EC.presence_of_element_located((By.ID, self.fill_input_status_in_authenticated_user_xpath)))
        select = Select(select)
        status = select.select_by_visible_text(Status)
        
        self.click_on_authenticated_user_save_button()
        time.sleep(2)
        return username and email and role and status
    
    def click_on_authenticated_user_save_button(self):
        self.driver.find_element(By.ID, self.click_on_allow_authenticated_user_save_button_xpath).click()
        
    def display_message_on_top(self):
        return self.driver.find_element(By.ID, self.display_meesage_in_notice_id_on_top_xpath).text
    
    def display_validation_message_for_input_type(self):
        return self.driver.find_element(By.CLASS_NAME, self.required_validation_for_input_type_xpath).text
    
    def display_validation_message_for_parsley_pattern(self):
        return self.driver.find_element(By.CLASS_NAME, self.pattern_validation_for_input_type_xpath).text
    
    def click_on_authenticated_user_cancel_button(self):
        self.driver.find_element(By.ID, self.click_on_authenticated_user_cancel_button_xpath).click()

    def search_functionality(self, Username, email, role):
        login = Login(self.driver)
        login.fill_username_password_input(config.get("crediential","login_username"), config.get("crediential","login_password"))
        login.click_on_allow_authenticated_user_section()
        if Username:
            self.driver.find_element(By.ID,self.search_username_for_authenticated_user_section_xpath).send_keys(Username)
        elif email:
            self.driver.find_element(By.ID,self.search_email_for_authenticated_user_section_xpath).send_keys(email)
        elif role:
            wait = WebDriverWait(self.driver, 10)
            select = wait.until(EC.presence_of_element_located((By.ID, self.search_role_for_authenticated_user_section_xpath)))
            select = Select(select)
            role = select.select_by_visible_text(role)
            
        self.driver.find_element(By.XPATH,self.search_button_for_authenticated_user_section_xpath).click()
        time.sleep(2)
        
    def display_username_in_table_in_td_tag(self):
        return self.driver.find_element(By.TAG_NAME,self.display_username_in_this_table_on_td_xpath).text
    
    def display_no_data_found_validation_in_message(self):
        return self.driver.find_element(By.ID, self.display_meesage_in_notice_id_on_top_xpath).text
