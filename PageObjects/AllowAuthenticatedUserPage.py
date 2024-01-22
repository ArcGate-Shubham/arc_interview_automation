import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from PageObjects.LoginPage import Login
from PageObjects.locators import *
from Utilities.Readconfigurations import *
from Utilities.return_message import *

class AllowAuthenticatedUser:
    def __init__(self, driver):
        self.driver = driver
        # self.click_on_add_user_button_xpath = 'addButton'
        # self.fill_input_username_in_authenticated_user_xpath = 'userSettingUsername'
        # self.fill_input_email_in_authenticated_user_xpath = 'userSettingEmail'
        # self.fill_input_roll_in_authenticated_user_xpath = 'userSettingRole'
        # self.fill_input_status_in_authenticated_user_xpath = 'userSettingStatus'
        # self.click_on_allow_authenticated_user_save_button_xpath = 'save-button'
        # self.display_meesage_in_notice_id_on_top_xpath = 'notice'
        # self.required_validation_for_input_type_xpath = 'parsley-required'
        # self.click_on_authenticated_user_cancel_button_xpath = 'close-button'
        # self.pattern_validation_for_input_type_xpath = 'parsley-pattern'
        # self.search_username_for_authenticated_user_section_xpath = 'id_username'
        # self.search_email_for_authenticated_user_section_xpath = 'id_email'
        # self.search_role_for_authenticated_user_section_xpath = 'id_role'
        # self.search_button_for_authenticated_user_section_xpath = '//input[@value="Search"]'
        # self.display_username_in_this_table_on_td_xpath = 'td'
        # self.display_email_in_this_table_on_td_xpath = 'email_column'
        # self.display_admin_role_in_this_table_on_td_xpath = 'role_column'
        # self.delete_row_in_table_data_xpath = 'Delete'
        # self.table_row_count_xpath = 'tbody tr'
        # self.click_on_edit_button_xpath = 'a.Edit'
        # self.click_on_close_button_based_on_edit_form_xpath = 'close-button'
        # self.click_on_edit_button_and_also_select_role_dropdown_xpath = '//select[@id="userSettingRole"]/option[1]'
        # self.click_on_edit_button_and_also_select_status_dropdown_xpath = '//select[@id="userSettingStatus"]/option[1]'
        
    def click_on_add_user_button(self):
        self.driver.find_element(*AllowAuthenticatedUserPageLocators.ADD_USER_BUTTON).click()
        
    def fill_the_form_allow_authenticated_user(self, Username, Email, Role, Status):
        login = Login(self.driver)
        login.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        login.click_on_allow_authenticated_user_section()
        self.click_on_add_user_button()
        time.sleep(2)
        username = self.driver.find_element(*AllowAuthenticatedUserPageLocators.INPUT_USERNAME).send_keys(Username)
        email = self.driver.find_element(*AllowAuthenticatedUserPageLocators.INPUT_EMAIL).send_keys(Email)
        
        wait = WebDriverWait(self.driver, 10)
        select = wait.until(EC.presence_of_element_located((AllowAuthenticatedUserPageLocators.INPUT_ROLE)))
        select = Select(select)
        role = select.select_by_visible_text(Role)
        
        select = wait.until(EC.presence_of_element_located((AllowAuthenticatedUserPageLocators.INPUT_STATUS)))
        select = Select(select)
        status = select.select_by_visible_text(Status)
        
        self.click_on_authenticated_user_save_button()
        time.sleep(2)
        return username and email and role and status
    
    def display_validation_message_yes_or_no(self):
        assert PARSLEY_REQUIRED in self.display_validation_message_for_input_type()
            
    def display_arcgate_email_validation_message(self, not_modal):
        if not_modal:
            assert USERNAME_ALREADY in self.display_message_on_top()
        else:
            assert NOT_ARCGATE_EMAIL in self.display_validation_message_for_parsley_pattern()
            
    def click_on_authenticated_user_save_button(self):
        self.driver.find_element(*Locators.SAVE_BUTTON).click()
        
    def display_message_on_top(self):
        return self.driver.find_element(*Locators.DISPLAY_MESSAGE).text
    
    def display_validation_message_for_input_type(self):
        return self.driver.find_element(*Locators.PARSLEY_REQUIRED).text
    
    def display_validation_message_for_parsley_pattern(self):
        return self.driver.find_element(*Locators.PARSLEY_PATTERN).text
    
    def click_on_authenticated_user_cancel_button(self):
        self.driver.find_element(*Locators.CLOSE_BUTTON).click()

    def search_functionality(self, Username, email, role):
        login = Login(self.driver)
        login.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        login.click_on_allow_authenticated_user_section()
        if Username:
            self.driver.find_element(*AllowAuthenticatedUserPageLocators.SEARCH_USERNAME).send_keys(Username)
        elif email:
            self.driver.find_element(*AllowAuthenticatedUserPageLocators.SEARCH_EMAIL).send_keys(email)
        elif role:
            wait = WebDriverWait(self.driver, 10)
            select = wait.until(EC.presence_of_element_located((AllowAuthenticatedUserPageLocators.SEARCH_ROLE)))
            select = Select(select)
            role = select.select_by_visible_text(role)
            
        self.driver.find_element(*AllowAuthenticatedUserPageLocators.SEARCH_BUTTON).click()
        time.sleep(2)
        
    def display_username_in_table_in_td_tag(self):
        return self.driver.find_element(*AllowAuthenticatedUserPageLocators.DISPLAY_USERNAME_TABLE).text
    
    def display_no_data_found_validation_in_message(self):
        return self.driver.find_element(*Locators.DISPLAY_MESSAGE).text
    
    def display_email_in_table(self):
        return self.driver.find_element(*AllowAuthenticatedUserPageLocators.DISPLAY_EMAIL_TABLE).text
    
    def display_role_for_admin_role_in_table(self):
        return self.driver.find_element(*AllowAuthenticatedUserPageLocators.DISPLAY_ROLE_TABLE).text
    
    def search_functionality_from_diffrent_types(self, Username, email, role):
        login = Login(self.driver)
        login.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        login.click_on_allow_authenticated_user_section()
        if Username and email:
            self.driver.find_element(*AllowAuthenticatedUserPageLocators.SEARCH_USERNAME).send_keys(Username)
            self.driver.find_element(*AllowAuthenticatedUserPageLocators.SEARCH_EMAIL).send_keys(email)
        elif Username and role:
            self.driver.find_element(*AllowAuthenticatedUserPageLocators.SEARCH_USERNAME).send_keys(Username)
            wait = WebDriverWait(self.driver, 10)
            select = wait.until(EC.presence_of_element_located((AllowAuthenticatedUserPageLocators.SEARCH_ROLE)))
            select = Select(select)
            role = select.select_by_visible_text(role)
        elif email and role:
            self.driver.find_element(*AllowAuthenticatedUserPageLocators.SEARCH_EMAIL).send_keys(email)
            wait = WebDriverWait(self.driver, 10)
            select = wait.until(EC.presence_of_element_located((AllowAuthenticatedUserPageLocators.SEARCH_ROLE)))
            select = Select(select)
            role = select.select_by_visible_text(role)
        else:
            self.driver.find_element(*AllowAuthenticatedUserPageLocators.SEARCH_USERNAME).send_keys(Username)
            self.driver.find_element(*AllowAuthenticatedUserPageLocators.SEARCH_EMAIL).send_keys(email)
            wait = WebDriverWait(self.driver, 10)
            select = wait.until(EC.presence_of_element_located((AllowAuthenticatedUserPageLocators.SEARCH_ROLE)))
            select = Select(select)
            role = select.select_by_visible_text(role)
            
        self.driver.find_element(*AllowAuthenticatedUserPageLocators.SEARCH_BUTTON).click()
        time.sleep(2)
        
    def click_on_delete_button(self):
        time.sleep(2)
        self.driver.find_element(*Locators.DELETE_BUTTON).click()
        time.sleep(2)

    def delete_any_row_of_authenticated_user_in_table_data(self):
        login = Login(self.driver)
        login.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        login.click_on_allow_authenticated_user_section()
        self.click_on_delete_button()
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        assert USER_DELETED in self.display_no_data_found_validation_in_message()
            
    def row_count_of_authenticated_user(self):
        return self.driver.find_elements(*Locators.TABLE_ROW_COUNT)
            
    def not_delete_any_row_of_authenticated_user_in_table_data_using_cancel_button(self):
        login = Login(self.driver)
        login.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        login.click_on_allow_authenticated_user_section()
        old_row = 0
        for old_row_data in self.row_count_of_authenticated_user():
            old_row = old_row + 1
        self.click_on_delete_button()
        self.driver.switch_to.alert.dismiss()
        new_row = 0
        for new_row_data in self.row_count_of_authenticated_user():
            new_row = new_row + 1
        assert old_row == new_row
            
    def click_on_edit_button_on_table(self):
        self.driver.find_element(*Locators.EDIT_BUTTON).click()
        
    def click_of_close_button_for_edit_allow_authentication_form(self):
        time.sleep(2)
        return self.driver.find_element(*Locators.CLOSE_BUTTON)
            
    def click_on_edit_button_and_without_changes_click_on_cancel_button(self):
        login = Login(self.driver)
        login.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        login.click_on_allow_authenticated_user_section()
        self.click_on_edit_button_on_table()
        self.click_of_close_button_for_edit_allow_authentication_form()
        time.sleep(2)
        
    def username(self):
        return self.driver.find_element(*AllowAuthenticatedUserPageLocators.INPUT_USERNAME)
        
    def email(self):
        return self.driver.find_element(*AllowAuthenticatedUserPageLocators.INPUT_EMAIL)
    
    def role(self):
        self.driver.find_element(*AllowAuthenticatedUserPageLocators.CLICK_EDIT_BUTTON_SELECT_ROLE_DROPDOWN).click()
        time.sleep(3)
        
    def status(self):
        self.driver.find_element(*AllowAuthenticatedUserPageLocators.CLICK_EDIT_BUTTON_SELECT_STATUS_DROPDOWN).click()
        time.sleep(3)
        
    def click_on_edit_button_and_update_all_input_type(self):
        login = Login(self.driver)
        login.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        login.click_on_allow_authenticated_user_section()
        self.click_on_edit_button_on_table()
        time.sleep(2)
        
    def click_on_edit_button_then_click_on_save_button(self):
        login = Login(self.driver)
        login.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        login.click_on_allow_authenticated_user_section()
        self.click_on_edit_button_on_table()
        time.sleep(2)
        self.click_on_authenticated_user_save_button()
        time.sleep(2)
        assert USER_UPDATED in self.display_no_data_found_validation_in_message()
