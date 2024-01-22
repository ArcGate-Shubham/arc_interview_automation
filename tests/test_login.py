import allure
import pytest

from Utilities.constants import *
from Utilities.Readconfigurations import *

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_001(self):
        self.log.getthelogs().info('TEST CASE, test_001')
        self.login.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        self.login.display_successfully_login_message()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_002(self):
        self.log.getthelogs().info('TEST CASE, test_002')
        self.login.fill_username_password_input(read_configuration("crediential","login_invalid_username"), read_configuration("crediential","login_password"))
        self.login.display_invalid_crediential_message()
    
    @allure.severity(allure.severity_level.CRITICAL)        
    def test_003(self):
        self.log.getthelogs().info('TEST CASE, test_003')
        self.login.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_invalid_password"))
        self.login.display_invalid_crediential_message()
    
    @allure.severity(allure.severity_level.CRITICAL)        
    def test_004(self):
        self.log.getthelogs().info('TEST CASE, test_004')
        self.login.fill_username_password_input(read_configuration("crediential","login_invalid_username"), read_configuration("crediential","login_invalid_password"))
        self.login.display_invalid_crediential_message()
    
    @allure.severity(allure.severity_level.CRITICAL)        
    def test_005(self):
        self.log.getthelogs().info('TEST CASE, test_005')
        self.login.fill_username_password_input(read_configuration("crediential","login_username"),BLANK)
        self.login.display_admin_login_text()
    
    @allure.severity(allure.severity_level.CRITICAL)        
    def test_006(self):
        self.log.getthelogs().info('TEST CASE, test_006')
        self.login.fill_username_password_input('', read_configuration("crediential","login_password"))
        self.login.display_admin_login_text()
    
    @allure.severity(allure.severity_level.CRITICAL)        
    def test_007(self):
        self.log.getthelogs().info('TEST CASE, test_007')
        self.login.fill_username_password_input(read_configuration("crediential","login_invalid_username"),BLANK)
        self.login.display_admin_login_text()
    
    @allure.severity(allure.severity_level.CRITICAL)
    def test_008(self):
        self.log.getthelogs().info('TEST CASE, test_008')
        self.login.fill_username_password_input('', read_configuration("crediential","login_invalid_password"))
        self.login.display_admin_login_text()
    
    @allure.severity(allure.severity_level.CRITICAL)
    def test_009(self):
        self.log.getthelogs().info('TEST CASE, test_009')
        self.login.fill_username_password_input(BLANK, BLANK)
        self.login.display_admin_login_text()
