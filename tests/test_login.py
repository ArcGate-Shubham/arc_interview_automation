import time
import pytest
import configparser

from selenium.webdriver.common.by import By
from Utilities.logger import logclass
from PageObjects.LoginPage import Login
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin(logclass):
    def test_login_with_valid_username_valid_password(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_login_with_valid_username_valid_password')
        log.info("Test Case Starting")
        login = Login(self.driver)
        login.fill_username_password_input(config.get("crediential","login_username"), config.get("crediential","login_password"))
        if 'Logged in successfully' in login.display_successfully_login_message():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_login_with_valid_username_valid_password.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_login_with_invalid_username_valid_password(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_login_with_invalid_username_valid_password')
        log.info("Test Case Starting")
        login = Login(self.driver)
        login.fill_username_password_input(config.get("crediential","login_invalid_username"), config.get("crediential","login_password"))
        if 'Invalid username or password' in login.display_invalid_crediential_message():
            assert True
            log.info('Test Case Pass')  
        else:
            self.driver.save_screenshot('Screenshots/test_login_with_invalid_username_valid_password.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_login_with_valid_username_invalid_password(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_login_with_valid_username_invalid_password')
        log.info("Test Case Starting")
        login = Login(self.driver)
        login.fill_username_password_input(config.get("crediential","login_username"), config.get("crediential","login_invalid_password"))
        if 'Invalid username or password' in login.display_invalid_crediential_message():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_login_with_valid_username_invalid_password.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_login_with_invalid_username_invalid_password(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_login_with_invalid_username_invalid_password')
        log.info("Test Case Starting")
        login = Login(self.driver)
        login.fill_username_password_input(config.get("crediential","login_invalid_username"), config.get("crediential","login_invalid_password"))
        if 'Invalid username or password' in login.display_invalid_crediential_message():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_login_with_invalid_username_invalid_password.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_login_with_valid_username_without_password(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_login_with_invalid_username_without_password')
        log.info("Test Case Starting")
        login = Login(self.driver)
        login.fill_username_password_input(config.get("crediential","login_username"),'')
        if 'Log In' in login.display_admin_login_text():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_login_with_valid_username_without_password.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_login_without_username_with_valid_password(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_login_without_username_with_valid_password')
        log.info("Test Case Starting")
        login = Login(self.driver)
        login.fill_username_password_input('',config.get("crediential","login_password"))
        if 'Log In' in login.display_admin_login_text():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_login_without_username_with_valid_password.png')
            log.critical('Test Case Fail')
            assert False
            
    def test_login_with_invalid_username_without_password(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_login_with_invalid_username_without_password')
        log.info("Test Case Starting")
        login = Login(self.driver)
        login.fill_username_password_input(config.get("crediential","login_invalid_username"),'')
        if 'Log In' in login.display_admin_login_text():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_login_with_invalid_username_without_password.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_login_without_username_with_invalid_password(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_login_without_username_with_invalid_password')
        log.info("Test Case Starting")
        login = Login(self.driver)
        login.fill_username_password_input('',config.get("crediential","login_invalid_password"))
        if 'Log In' in login.display_admin_login_text():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_login_without_username_with_invalid_password.png')
            log.critical('Test Case Fail')
            assert False
    
    def test_login_without_username_without_password(self):
        log = self.getthelogs()
        log.info('TEST CASE, test_login_without_username_without_password')
        log.info("Test Case Starting")
        login = Login(self.driver)
        login.fill_username_password_input('','')
        if 'Log In' in login.display_admin_login_text():
            assert True
            log.info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_login_without_username_without_password.png')
            log.critical('Test Case Fail')
            assert False
