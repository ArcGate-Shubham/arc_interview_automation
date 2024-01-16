import allure
import pytest
from Utilities.constants import *
from Utilities.return_message import *
from Utilities.generate_email import *

@pytest.mark.usefixtures("setup_and_teardown")
class TestImageBasedSubjectiveQuestion:
    
    @allure.severity(allure.severity_level.CRITICAL)
    def test_001(self):
        self.log.getthelogs().info('TEST CASE, test_001')
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, generate_random_string_subject(), HINDI, IMAGE, ADD, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_002(self):
        self.log.getthelogs().info('TEST CASE, test_002')
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, generate_random_string_subject(), HINDI, IMAGE, BLANK, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_003(self):
        self.log.getthelogs().info('TEST CASE, test_003')
        self.image_based_subjective_question.add_new_image_based_subjective_question(BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_004(self):
        self.log.getthelogs().info('TEST CASE, test_004')
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, BLANK, BLANK, BLANK, ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_005(self):
        self.log.getthelogs().info('TEST CASE, test_005')
        self.image_based_subjective_question.add_new_image_based_subjective_question(BLANK, HINDI, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_006(self):
        self.log.getthelogs().info('TEST CASE, test_006')
        self.image_based_subjective_question.add_new_image_based_subjective_question(BLANK, BLANK, HINDI, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_007(self):
        self.log.getthelogs().info('TEST CASE, test_007')
        self.image_based_subjective_question.add_new_image_based_subjective_question(BLANK, BLANK, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_008(self):
        self.log.getthelogs().info('TEST CASE, test_008')
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, generate_random_string_subject(), BLANK, BLANK, ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_009(self):
        self.log.getthelogs().info('TEST CASE, test_009')
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, BLANK, generate_random_string_subject(), BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_010(self):
        self.log.getthelogs().info('TEST CASE, test_010')
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, BLANK, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_011(self):
        self.log.getthelogs().info('TEST CASE, test_011')
        self.image_based_subjective_question.add_new_image_based_subjective_question(BLANK, generate_random_string_subject(), generate_random_string_subject(), BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_012(self):
        self.log.getthelogs().info('TEST CASE, test_012')
        self.image_based_subjective_question.add_new_image_based_subjective_question(BLANK, generate_random_string_subject(), BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_013(self):
        self.log.getthelogs().info('TEST CASE, test_013')
        self.image_based_subjective_question.add_new_image_based_subjective_question(BLANK, BLANK, generate_random_string_subject(), IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_014(self):
        self.log.getthelogs().info('TEST CASE, test_014')
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, generate_random_string_subject(), generate_random_string_subject(), BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_015(self):
        self.log.getthelogs().info('TEST CASE, test_015')
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, generate_random_string_subject(), BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_016(self):
        self.log.getthelogs().info('TEST CASE, test_016')
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, BLANK, generate_random_string_subject(), IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_017(self):
        self.log.getthelogs().info('TEST CASE, test_017')
        self.image_based_subjective_question.add_new_image_based_subjective_question(BLANK, generate_random_string_subject(), generate_random_string_subject(), IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_018(self):
        self.log.getthelogs().info('TEST CASE, test_018')
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, generate_random_string_subject(), generate_random_string_subject(), OTHER_IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.CRITICAL)
    def test_019(self):
        self.log.getthelogs().info('TEST CASE, test_019')
        self.image_based_subjective_question.add_new_image_based_subjective_question(TYPING_TEST, generate_random_string_subject(), generate_random_string_subject(), IMAGE, ADD, BLANK)
        
    @allure.severity(allure.severity_level.CRITICAL)
    def test_020(self):
        self.log.getthelogs().info('TEST CASE, test_020')
        self.image_based_subjective_question.add_new_image_based_subjective_question(EXCEL, generate_random_string_subject(), generate_random_string_subject(), IMAGE, ADD, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_021(self):
        self.log.getthelogs().info('TEST CASE, test_021')
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, generate_random_string_subject(), generate_random_string_subject(), ANOTHER_IMAGE, ADD, VALIDATION)
