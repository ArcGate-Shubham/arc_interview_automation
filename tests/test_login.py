import allure
import pytest

from Utilities.constants import *
from Utilities.Readconfigurations import *

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_001(self):
        self.login.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        self.login.display_successfully_login_message()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_002(self):
        self.login.fill_username_password_input(read_configuration("crediential","login_invalid_username"), read_configuration("crediential","login_password"))
        self.login.display_invalid_crediential_message()
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression        
    def test_003(self):
        self.login.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_invalid_password"))
        self.login.display_invalid_crediential_message()
    
    @allure.severity(allure.severity_level.CRITICAL)        
    @pytest.mark.regression
    def test_004(self):
        self.login.fill_username_password_input(read_configuration("crediential","login_invalid_username"), read_configuration("crediential","login_invalid_password"))
        self.login.display_invalid_crediential_message()
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression        
    def test_005(self):
        self.login.fill_username_password_input(read_configuration("crediential","login_username"),BLANK)
        self.login.display_admin_login_text()
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression        
    def test_006(self):
        self.login.fill_username_password_input('', read_configuration("crediential","login_password"))
        self.login.display_admin_login_text()
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression        
    def test_007(self):
        self.login.fill_username_password_input(read_configuration("crediential","login_invalid_username"),BLANK)
        self.login.display_admin_login_text()
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_008(self):
        self.login.fill_username_password_input('', read_configuration("crediential","login_invalid_password"))
        self.login.display_admin_login_text()
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_009(self):
        self.login.fill_username_password_input(BLANK, BLANK)
        self.login.display_admin_login_text()
