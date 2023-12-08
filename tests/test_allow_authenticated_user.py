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
        authenticated_user.display_validation_message_yes_or_no('Screenshots/test_without_username_for_authenticated_user.png')
            
    def test_without_email_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_email_for_authenticated_user')
        log.info("Test Case Starting")    
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','','Admin', 'Active')
        authenticated_user.display_validation_message_yes_or_no('Screenshots/test_without_email_for_authenticated_user.png')
            
    def test_without_role_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_role_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@arcgate.com','---------', 'Active')
        authenticated_user.display_validation_message_yes_or_no('Screenshots/test_without_email_for_authenticated_user.png')
            
    def test_without_status_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_status_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@arcgate.com','Admin', '---------')
        authenticated_user.display_validation_message_yes_or_no('Screenshots/test_without_status_for_authenticated_user.png')
            
    def test_without_username_or_email_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_email_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','','Admin', 'Active')
        authenticated_user.display_validation_message_yes_or_no('Screenshots/test_without_username_or_email_for_authenticated_user.png')
            
    def test_without_username_or_role_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_role_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','vishala@arcgate.com','---------', 'Active')
        authenticated_user.display_validation_message_yes_or_no('Screenshots/test_without_username_or_role_for_authenticated_user.png')
        
    def test_without_username_or_status_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_status_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','vishala@arcgate.com','Admin', '---------')
        authenticated_user.display_validation_message_yes_or_no('Screenshots/test_without_username_or_status_for_authenticated_user.png')
            
    def test_without_email_or_role_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_email_or_role_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','','---------', 'Active')
        authenticated_user.display_validation_message_yes_or_no('Screenshots/test_without_email_or_role_for_authenticated_user.png')

    def test_without_email_or_status_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_email_or_status_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','','Admin', '---------')
        authenticated_user.display_validation_message_yes_or_no('Screenshots/test_without_email_or_status_for_authenticated_user.png')
            
    def test_without_role_or_status_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_role_or_status_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@arcgate.com','---------', '---------')
        authenticated_user.display_validation_message_yes_or_no('Screenshots/test_without_role_or_status_for_authenticated_user.png')

    def test_without_email_or_role_or_status_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_email_or_role_or_status_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','','---------', '---------')
        authenticated_user.display_validation_message_yes_or_no('Screenshots/test_without_email_or_role_or_status_for_authenticated_user.png')
            
    def test_without_username_or_role_or_status_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_role_or_status_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','vishala@arcgate.com','---------', '---------')
        authenticated_user.display_validation_message_yes_or_no('Screenshots/test_without_username_or_role_or_status_for_authenticated_user.png')
            
    def test_without_username_or_email_or_status_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_email_or_status_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','','Admin', '---------')
        authenticated_user.display_validation_message_yes_or_no('Screenshots/test_without_username_or_email_or_status_for_authenticated_user.png')

    def test_without_username_or_email_or_role_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_email_or_role_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','','---------', 'Active')
        authenticated_user.display_validation_message_yes_or_no('Screenshots/test_without_username_or_email_or_role_for_authenticated_user.png')
    
    def test_without_username_or_email_or_role_or_status_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_email_or_role_or_status_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','','---------', '---------')
        authenticated_user.display_validation_message_yes_or_no('Screenshots/test_without_username_or_email_or_role_or_status_for_authenticated_user.png')
        
    def test_with_gmail_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_with_gmail_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@gmail.com','Admin', 'Active')
        authenticated_user.display_arcgate_email_validation_message('Screenshots/test_with_gmail_domain_email_address_use_for_authenticated_user.png')
            
    def test_with_hotmail_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_with_hotmail_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@hotmail.com','Admin', 'Active')
        authenticated_user.display_arcgate_email_validation_message('Screenshots/test_with_hotmail_domain_email_address_use_for_authenticated_user.png')
    
    def test_with_yahoo_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_with_yahoo_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@yahoo.com','Admin', 'Active')
        authenticated_user.display_arcgate_email_validation_message('Screenshots/test_with_yahoo_domain_email_address_use_for_authenticated_user.png')
    
    def test_with_arcgate_domain_but_without_dotcom_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_with_arcgate_domain_but_without_dotcom_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@arcgate','Admin', 'Active')
        authenticated_user.display_arcgate_email_validation_message('Screenshots/test_with_arcgate_domain_but_without_dotcom_email_address_use_for_authenticated_user.png')
    
    def test_with_arcgate_domain_but_with_codot_dotin_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_with_arcgate_domain_but_with_codot_dotin_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@arcgate.co.in','Admin', 'Active')
        authenticated_user.display_arcgate_email_validation_message('Screenshots/test_with_arcgate_domain_but_with_codot_dotin_email_address_use_for_authenticated_user.png')
    
    def test_without_username_with_gmail_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_with_gmail_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','vishala@gmail.com','Admin', 'Active')
        authenticated_user.display_arcgate_email_validation_message('Screenshots/test_without_username_with_gmail_domain_email_address_use_for_authenticated_user.png')
    
    def test_without_role_with_gmail_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_role_with_gmail_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@gmail.com','---------', 'Active')
        authenticated_user.display_arcgate_email_validation_message('Screenshots/test_without_role_with_gmail_domain_email_address_use_for_authenticated_user.png')

    def test_without_status_with_gmail_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_status_with_gmail_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@gmail.com','Admin', '---------')
        authenticated_user.display_arcgate_email_validation_message('Screenshots/test_without_status_with_gmail_domain_email_address_use_for_authenticated_user.png')
    
    def test_without_username_or_without_role_with_gmail_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_without_role_with_gmail_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','vishala@gmail.com','---------', 'Active')
        authenticated_user.display_arcgate_email_validation_message('Screenshots/test_without_username_or_without_role_with_gmail_domain_email_address_use_for_authenticated_user.png')
    
    def test_without_username_or_without_status_with_gmail_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_without_status_with_gmail_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','vishala@gmail.com','Admin', '---------')
        authenticated_user.display_arcgate_email_validation_message('Screenshots/test_without_username_or_without_status_with_gmail_domain_email_address_use_for_authenticated_user.png')
    
    def test_without_role_or_without_status_with_gmail_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_role_or_without_status_with_gmail_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('vishal','vishala@gmail.com','---------', '---------')
        authenticated_user.display_arcgate_email_validation_message('Screenshots/test_without_role_or_without_status_with_gmail_domain_email_address_use_for_authenticated_user.png')
    
    def test_without_username_or_without_role_or_without_status_with_gmail_domain_email_address_use_for_authenticated_user(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_without_username_or_without_role_or_without_status_with_gmail_domain_email_address_use_for_authenticated_user')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.fill_the_form_allow_authenticated_user('','vishala@gmail.com','---------', '---------')
        authenticated_user.display_arcgate_email_validation_message('Screenshots/test_without_username_or_without_role_or_without_status_with_gmail_domain_email_address_use_for_authenticated_user.png')
            
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

    def test_search_with_valid_email_in_allow_authenticated_user_section(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_search_with_valid_email_in_allow_authenticated_user_section')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.search_functionality('', 'visha@arcgate.com', '')
        if 'visha@arcgate.com' in authenticated_user.display_email_in_table():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_search_with_valid_email_in_allow_authenticated_user_section.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_search_with_invalid_email_in_allow_authenticated_user_section(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_search_with_invalid_email_in_allow_authenticated_user_section')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.search_functionality('', 'vishal@arcgate.com', '')
        if 'No data found' in authenticated_user.display_no_data_found_validation_in_message():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_search_with_invalid_email_in_allow_authenticated_user_section.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_search_with_valid_role_in_allow_authenticated_user_section(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_search_with_valid_role_in_allow_authenticated_user_section')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.search_functionality('', '', 'Admin')
        if 'Admin' in authenticated_user.display_role_for_admin_role_in_table():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_search_with_valid_role_in_allow_authenticated_user_section.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_search_with_invalid_role_in_allow_authenticated_user_section(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_search_with_invalid_role_in_allow_authenticated_user_section')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.search_functionality('', '', 'Interviewer')
        if 'No data found' in authenticated_user.display_no_data_found_validation_in_message():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_search_with_invalid_role_in_allow_authenticated_user_section.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_search_with_valid_username_and_email_in_allow_authenticated_user_section(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_search_with_valid_username_and_email_in_allow_authenticated_user_section')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.search_functionality('vishal', 'visha@arcgate.com', '')
        if 'vishal' in authenticated_user.display_username_in_table_in_td_tag() and 'visha@arcgate.com' in authenticated_user.display_email_in_table():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_search_with_valid_username_and_email_in_allow_authenticated_user_section.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_search_with_valid_username_and_email_in_allow_authenticated_user_section(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_search_with_valid_username_and_email_in_allow_authenticated_user_section')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.search_functionality('vishal', 'visha@arcgate.com', '')
        if 'vishal' in authenticated_user.display_username_in_table_in_td_tag() and 'visha@arcgate.com' in authenticated_user.display_email_in_table():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_search_with_valid_username_and_email_in_allow_authenticated_user_section.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_search_with_valid_username_and_role_in_allow_authenticated_user_section(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_search_with_valid_username_and_role_in_allow_authenticated_user_section')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.search_functionality('vishal', '', 'Admin')
        if 'vishal' in authenticated_user.display_username_in_table_in_td_tag() and 'Admin' in authenticated_user.display_role_for_admin_role_in_table():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_search_with_valid_username_and_role_in_allow_authenticated_user_section.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_search_with_valid_username_and_invalid_email_in_allow_authenticated_user_section(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_search_with_valid_username_and_invalid_email_in_allow_authenticated_user_section')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.search_functionality_from_diffrent_types('vishal', 'vishal@arcgate.com','')
        if 'No data found' in authenticated_user.display_no_data_found_validation_in_message():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_search_with_valid_username_and_invalid_email_in_allow_authenticated_user_section.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_search_with_valid_username_and_invalid_role_in_allow_authenticated_user_section(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_search_with_valid_username_and_invalid_role_in_allow_authenticated_user_section')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.search_functionality_from_diffrent_types('vishal', '','Administrator')
        if 'No data found' in authenticated_user.display_no_data_found_validation_in_message():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_search_with_valid_username_and_invalid_role_in_allow_authenticated_user_section.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_search_with_valid_email_and_invalid_role_in_allow_authenticated_user_section(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_search_with_valid_email_and_invalid_role_in_allow_authenticated_user_section')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.search_functionality_from_diffrent_types('', 'visha@arcgate.com','Administrator')
        if 'No data found' in authenticated_user.display_no_data_found_validation_in_message():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_search_with_valid_email_and_invalid_role_in_allow_authenticated_user_section.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_search_with_invalid_username_and_valid_role_in_allow_authenticated_user_section(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_search_with_invalid_username_and_valid_role_in_allow_authenticated_user_section')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.search_functionality_from_diffrent_types('vishala', '','Administrator')
        if 'No data found' in authenticated_user.display_no_data_found_validation_in_message():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_search_with_invalid_username_and_valid_role_in_allow_authenticated_user_section.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_search_with_valid_username_and_valid_role_and_valid_email_in_allow_authenticated_user_section(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_search_with_valid_username_and_valid_role_and_valid_email_in_allow_authenticated_user_section')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.search_functionality_from_diffrent_types('vishal', 'visha@arcgate.com','Admin')
        if 'vishal' in authenticated_user.display_username_in_table_in_td_tag() and 'Admin' in authenticated_user.display_role_for_admin_role_in_table() and 'visha@arcgate.com' in authenticated_user.display_email_in_table():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_search_with_valid_username_and_valid_role_and_valid_email_in_allow_authenticated_user_section.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_search_with_invalid_username_and_invalid_role_and_invalid_email_in_allow_authenticated_user_section(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_search_with_invalid_username_and_invalid_role_and_invalid_email_in_allow_authenticated_user_section')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.search_functionality_from_diffrent_types('vishala', 'vishal@arcgate.com','Administrator')
        if 'No data found' in authenticated_user.display_no_data_found_validation_in_message():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_search_with_invalid_username_and_invalid_role_and_invalid_email_in_allow_authenticated_user_section.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_deleted_row_in_table(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_deleted_row_in_table')
        log.info("Test Case Starting")
        authenticated_user = AllowAuthenticatedUser(self.driver)
        authenticated_user.delete_any_row_of_authenticated_user_in_table_data()
