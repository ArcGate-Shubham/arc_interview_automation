import pytest
import configparser

config = configparser.ConfigParser()
config.read("Utilities/input.properties")

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_username_valid_password(self):
        self.log.getthelogs().info('TEST CASE, test_login_with_valid_username_valid_password')
        self.login.fill_username_password_input(config.get("crediential","login_username"), config.get("crediential","login_password"))
        if 'Logged in successfully' in self.login.display_successfully_login_message():
            assert True
            self.log.getthelogs().info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_login_with_valid_username_valid_password.png')
            self.log.getthelogs().critical('Test Case Fail')
            assert False
            
    def test_login_with_invalid_username_valid_password(self):
        self.log.getthelogs().info('TEST CASE, test_login_with_invalid_username_valid_password')
        self.login.fill_username_password_input(config.get("crediential","login_invalid_username"), config.get("crediential","login_password"))
        if 'Invalid username or password' in self.login.display_invalid_crediential_message():
            assert True
            self.log.getthelogs().info('Test Case Pass')  
        else:
            self.driver.save_screenshot('Screenshots/test_login_with_invalid_username_valid_password.png')
            self.log.getthelogs().critical('Test Case Fail')
            assert False
            
    def test_login_with_valid_username_invalid_password(self):
        self.log.getthelogs().info('TEST CASE, test_login_with_valid_username_invalid_password')
        self.login.fill_username_password_input(config.get("crediential","login_username"), config.get("crediential","login_invalid_password"))
        if 'Invalid username or password' in self.login.display_invalid_crediential_message():
            assert True
            self.log.getthelogs().info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_login_with_valid_username_invalid_password.png')
            self.log.getthelogs().critical('Test Case Fail')
            assert False
            
    def test_login_with_invalid_username_invalid_password(self):
        self.log.getthelogs().info('TEST CASE, test_login_with_invalid_username_invalid_password')
        self.login.fill_username_password_input(config.get("crediential","login_invalid_username"), config.get("crediential","login_invalid_password"))
        if 'Invalid username or password' in self.login.display_invalid_crediential_message():
            assert True
            self.log.getthelogs().info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_login_with_invalid_username_invalid_password.png')
            self.log.getthelogs().critical('Test Case Fail')
            assert False
            
    def test_login_with_valid_username_without_password(self):
        self.log.getthelogs().info('TEST CASE, test_login_with_invalid_username_without_password')
        self.login.fill_username_password_input(config.get("crediential","login_username"),'')
        if 'Log In' in self.login.display_admin_login_text():
            assert True
            self.log.getthelogs().info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_login_with_valid_username_without_password.png')
            self.log.getthelogs().critical('Test Case Fail')
            assert False
            
    def test_login_without_username_with_valid_password(self):
        self.log.getthelogs().info('TEST CASE, test_login_without_username_with_valid_password')
        self.login.fill_username_password_input('',config.get("crediential","login_password"))
        if 'Log In' in self.login.display_admin_login_text():
            assert True
            self.log.getthelogs().info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_login_without_username_with_valid_password.png')
            self.log.getthelogs().critical('Test Case Fail')
            assert False
            
    def test_login_with_invalid_username_without_password(self):
        self.log.getthelogs().info('TEST CASE, test_login_with_invalid_username_without_password')
        self.login.fill_username_password_input(config.get("crediential","login_invalid_username"),'')
        if 'Log In' in self.login.display_admin_login_text():
            assert True
            self.log.getthelogs().info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_login_with_invalid_username_without_password.png')
            self.log.getthelogs().critical('Test Case Fail')
            assert False
    
    def test_login_without_username_with_invalid_password(self):
        self.log.getthelogs().info('TEST CASE, test_login_without_username_with_invalid_password')
        self.login.fill_username_password_input('',config.get("crediential","login_invalid_password"))
        if 'Log In' in self.login.display_admin_login_text():
            assert True
            self.log.getthelogs().info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_login_without_username_with_invalid_password.png')
            self.log.getthelogs().critical('Test Case Fail')
            assert False
    
    def test_login_without_username_without_password(self):
        self.log.getthelogs().info('TEST CASE, test_login_without_username_without_password')
        self.login.fill_username_password_input('','')
        if 'Log In' in self.login.display_admin_login_text():
            assert True
            self.log.getthelogs().info('Test Case Pass')
        else:
            self.driver.save_screenshot('Screenshots/test_login_without_username_without_password.png')
            self.log.getthelogs().critical('Test Case Fail')
            assert False
