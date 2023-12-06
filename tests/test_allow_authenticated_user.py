import time
import pytest
import configparser

from selenium.webdriver.common.by import By
from Utilities.logger import logclass
from Utilities.generate_email import generate_email_time_stamp, generate_username_time_stamp
from PageObjects.LoginPage import Login
from PageObjects.AllowAuthenticatedUserPage import AllowAuthenticatedUser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

@pytest.mark.usefixtures("setup_and_teardown")
class TestAllowAuthenticatedUser(logclass):
    def test_with_all_correct_input_type_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_with_all_correct_input_type_for_authenticated_user')
        log.info("Test Case Starting")        
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user(generate_username_time_stamp(),generate_email_time_stamp(),'Admin', 'Active')
        if 'User added successfully' in authenticated_user.display_message_on_top():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_with_all_correct_input_type_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_with_all_same_email_id_fill_input_type_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_with_all_same_email_id_fill_input_type_for_authenticated_user')
        log.info("Test Case Starting")        
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','visha@arcgate.com','Admin', 'Active')
        if 'This email id already taken' in authenticated_user.display_message_on_top():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_with_all_same_email_id_fill_input_type_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_with_all_same_username_fill_input_type_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_with_all_same_username_fill_input_type_for_authenticated_user')
        log.info("Test Case Starting")    
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@arcgate.com','Admin', 'Active')
        if 'Username already taken' in authenticated_user.display_message_on_top():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_with_all_same_username_fill_input_type_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_without_username_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_for_authenticated_user')
        log.info("Test Case Starting")    
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','vishala@arcgate.com','Admin', 'Active')
        if 'This field is required.' in authenticated_user.display_validation_message_for_input_type():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_username_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_without_email_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_email_for_authenticated_user')
        log.info("Test Case Starting")    
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','','Admin', 'Active')
        if 'This field is required.' in authenticated_user.display_validation_message_for_input_type():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_email_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_without_role_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_role_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@arcgate.com','---------', 'Active')
        if 'This field is required.' in authenticated_user.display_validation_message_for_input_type():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_role_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_without_status_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_status_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@arcgate.com','Admin', '---------')
        if 'This field is required.' in authenticated_user.display_validation_message_for_input_type():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_status_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_without_username_or_email_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_email_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','','Admin', 'Active')
        if 'This field is required.' in authenticated_user.display_validation_message_for_input_type():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_username_or_email_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_without_username_or_role_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_role_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','vishala@arcgate.com','---------', 'Active')
        if 'This field is required.' in authenticated_user.display_validation_message_for_input_type():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_username_or_role_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
        
    def test_without_username_or_status_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_status_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','vishala@arcgate.com','Admin', '---------')
        if 'This field is required.' in authenticated_user.display_validation_message_for_input_type():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_username_or_status_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_without_email_or_role_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_email_or_role_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','','---------', 'Active')
        if 'This field is required.' in authenticated_user.display_validation_message_for_input_type():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_email_or_role_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_without_email_or_status_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_email_or_status_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','','Admin', '---------')
        if 'This field is required.' in authenticated_user.display_validation_message_for_input_type():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_email_or_status_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_without_role_or_status_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_role_or_status_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@arcgate.com','---------', '---------')
        if 'This field is required.' in authenticated_user.display_validation_message_for_input_type():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_role_or_status_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_without_email_or_role_or_status_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_email_or_role_or_status_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','','---------', '---------')
        if 'This field is required.' in authenticated_user.display_validation_message_for_input_type():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_email_or_role_or_status_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_without_username_or_role_or_status_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_role_or_status_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','vishala@arcgate.com','---------', '---------')
        if 'This field is required.' in authenticated_user.display_validation_message_for_input_type():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_username_or_role_or_status_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_without_username_or_email_or_status_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_email_or_status_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','','Admin', '---------')
        if 'This field is required.' in authenticated_user.display_validation_message_for_input_type():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_username_or_email_or_status_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_without_username_or_email_or_role_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_email_or_role_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','','---------', 'Active')
        if 'This field is required.' in authenticated_user.display_validation_message_for_input_type():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_username_or_email_or_role_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_without_username_or_email_or_role_or_status_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_email_or_role_or_status_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','','---------', '---------')
        if 'This field is required.' in authenticated_user.display_validation_message_for_input_type():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_username_or_email_or_role_or_status_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_with_gmail_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_with_gmail_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@gmail.com','Admin', 'Active')
        if 'This is not an arcgate email.' in authenticated_user.display_validation_message_for_parsley_pattern():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_with_gmail_domain_email_address_use_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_with_hotmail_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_with_hotmail_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@hotmail.com','Admin', 'Active')
        if 'This is not an arcgate email.' in authenticated_user.display_validation_message_for_parsley_pattern():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_with_hotmail_domain_email_address_use_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_with_yahoo_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_with_yahoo_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@yahoo.com','Admin', 'Active')
        if 'This is not an arcgate email.' in authenticated_user.display_validation_message_for_parsley_pattern():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_with_yahoo_domain_email_address_use_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_with_arcgate_domain_but_without_dotcom_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_with_arcgate_domain_but_without_dotcom_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@arcgate','Admin', 'Active')
        if 'This is not an arcgate email.' in authenticated_user.display_validation_message_for_parsley_pattern():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_with_arcgate_domain_but_without_dotcom_email_address_use_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_with_arcgate_domain_but_with_codot_dotin_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_with_arcgate_domain_but_with_codot_dotin_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@arcgate.co.in','Admin', 'Active')
        if 'This is not an arcgate email.' in authenticated_user.display_validation_message_for_parsley_pattern():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_with_arcgate_domain_but_with_codot_dotin_email_address_use_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_without_username_with_gmail_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_with_gmail_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','vishala@gmail.com','Admin', 'Active')
        if 'This is not an arcgate email.' in authenticated_user.display_validation_message_for_parsley_pattern():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_username_with_gmail_domain_email_address_use_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_without_role_with_gmail_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_role_with_gmail_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@gmail.com','---------', 'Active')
        if 'This is not an arcgate email.' in authenticated_user.display_validation_message_for_parsley_pattern():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_role_with_gmail_domain_email_address_use_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_without_status_with_gmail_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_status_with_gmail_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@gmail.com','Admin', '---------')
        if 'This is not an arcgate email.' in authenticated_user.display_validation_message_for_parsley_pattern():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_status_with_gmail_domain_email_address_use_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_without_username_or_without_role_with_gmail_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_without_role_with_gmail_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','vishala@gmail.com','---------', 'Active')
        if 'This is not an arcgate email.' in authenticated_user.display_validation_message_for_parsley_pattern():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_username_or_without_role_with_gmail_domain_email_address_use_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_without_username_or_without_status_with_gmail_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_without_status_with_gmail_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','vishala@gmail.com','Admin', '---------')
        if 'This is not an arcgate email.' in authenticated_user.display_validation_message_for_parsley_pattern():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_username_or_without_status_with_gmail_domain_email_address_use_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_without_role_or_without_status_with_gmail_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_role_or_without_status_with_gmail_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@gmail.com','---------', '---------')
        if 'This is not an arcgate email.' in authenticated_user.display_validation_message_for_parsley_pattern():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_role_or_without_status_with_gmail_domain_email_address_use_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_without_username_or_without_role_or_without_status_with_gmail_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_without_role_or_without_status_with_gmail_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','vishala@gmail.com','---------', '---------')
        if 'This is not an arcgate email.' in authenticated_user.display_validation_message_for_parsley_pattern():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_without_username_or_without_role_or_without_status_with_gmail_domain_email_address_use_for_authenticated_user.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_search_with_valid_username_in_allow_authenticated_user_section(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_search_with_valid_username_in_allow_authenticated_user_section')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.search_functionality('vishal', '', '')
        if 'vishal' in authenticated_user.display_username_in_table_in_td_tag():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_search_with_valid_username_in_allow_authenticated_user_section.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_search_with_invalid_username_in_allow_authenticated_user_section(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_search_with_invalid_username_in_allow_authenticated_user_section')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.search_functionality('vishala', '', '')
        if 'No data found' in authenticated_user.display_no_data_found_validation_in_message():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_search_with_invalid_username_in_allow_authenticated_user_section.png')
            log.critical('Test Case Fail')
            assert False
