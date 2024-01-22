import allure
import pytest

from Utilities.generate_email import *
from Utilities.return_message import *
from Utilities.constants import *
@pytest.mark.usefixtures("setup_and_teardown")
class TestSubject:
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_001(self):
        self.log.getthelogs().info('TEST CASE, test_001')
        self.subject.fill_the_form_add_new_subject(generate_random_string_subject())
        self.subject.success_message_for_subject(SUBJECT_ADDED)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_002(self):
        self.log.getthelogs().info('TEST CASE, test_002')
        self.subject.fill_the_form_add_new_subject(BLANK)
        self.subject.validation_message_for_required_subject()
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_003(self):
        self.log.getthelogs().info('TEST CASE, test_003')
        self.subject.fill_the_form_add_new_subject(NUMBER)
        self.subject.validation_message_for_subject()

    @allure.severity(allure.severity_level.NORMAL)
    def test_004(self):
        self.log.getthelogs().info('TEST CASE, test_004')
        self.subject.fill_the_form_add_new_subject(HASH_DATA)
        self.subject.validation_message_for_subject()
    
    @allure.severity(allure.severity_level.MINOR)
    def test_005(self):
        self.log.getthelogs().info('TEST CASE, test_005')
        self.subject.fill_the_form_add_new_subject(NAME_WITH_NUMBER)
        self.subject.validation_message_for_subject()
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_006(self):
        self.log.getthelogs().info('TEST CASE, test_006')
        self.subject.fill_the_form_add_new_subject(NAME_WITH_ATTHERATE)
        self.subject.validation_message_for_subject()
    
    @allure.severity(allure.severity_level.NORMAL)        
    def test_007(self):
        self.log.getthelogs().info('TEST CASE, test_007')
        self.subject.fill_the_form_add_new_subject(NAME_WITH_EXCLAMINATION)
        self.subject.success_message_for_subject(SUBJECT_ADDED)
    
    @allure.severity(allure.severity_level.NORMAL)        
    def test_008(self):
        self.log.getthelogs().info('TEST CASE, test_008')
        self.subject.not_save_new_subject_click_on_cancel_button()
        
    @allure.severity(allure.severity_level.NORMAL)    
    def test_009(self):
        self.log.getthelogs().info('TEST CASE, test_009')
        self.subject.delete_row_in_the_subject_table()
    
    @allure.severity(allure.severity_level.MINOR)    
    def test_010(self):
        self.log.getthelogs().info('TEST CASE, test_010')
        self.subject.not_delete_row_in_subject_table()

    @allure.severity(allure.severity_level.MINOR)
    def test_011(self):
        self.log.getthelogs().info('TEST CASE, test_011')
        self.subject.update_existing_data_in_the_subject_table_without_change()
    
    @allure.severity(allure.severity_level.MINOR)    
    def test_012(self):
        self.log.getthelogs().info('TEST CASE, test_012')
        self.subject.update_existing_subject_click_on_edit_button(BLANK)
        self.subject.validation_message_for_required_subject()
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_013(self):
        self.log.getthelogs().info('TEST CASE, test_013')
        self.subject.update_existing_subject_click_on_edit_button(generate_random_string_subject())
        self.subject.success_message_for_subject(SUBJECT_UPDATED)
    
    @allure.severity(allure.severity_level.NORMAL)        
    def test_014(self):
        self.log.getthelogs().info('TEST CASE, test_014')
        self.subject.update_existing_subject_click_on_edit_button(TEXT_WITH_NUMBER)
        self.subject.validation_message_for_subject()

    @allure.severity(allure.severity_level.NORMAL)
    def test_015(self):
        self.log.getthelogs().info('TEST CASE, test_015')
        self.subject.update_existing_subject_click_on_edit_button(TEXT_WITH_ATTHERATE)
        self.subject.validation_message_for_subject()
