import allure
import pytest
from Utilities.constants import *
from Utilities.return_message import *
from Utilities.generate_email import *

@pytest.mark.usefixtures("setup_and_teardown")
class TestImageBasedMultipleChoiceQuestion:
    
    @allure.severity(allure.severity_level.CRITICAL)
    def test_001(self):
        self.log.getthelogs().info('TEST CASE, test_001')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, OPTION_D, IMAGE, ADD, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_002(self):
        self.log.getthelogs().info('TEST CASE, test_002')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, OPTION_D, IMAGE, BLANK, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_003(self):
        self.log.getthelogs().info('TEST CASE, test_003')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_004(self):
        self.log.getthelogs().info('TEST CASE, test_004')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, BLANK, OPTION_A, OPTION_B, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_005(self):
        self.log.getthelogs().info('TEST CASE, test_005')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), BLANK, OPTION_B, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_006(self):
        self.log.getthelogs().info('TEST CASE, test_006')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), OPTION_A, BLANK, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_007(self):
        self.log.getthelogs().info('TEST CASE, test_007')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), OPTION_A, OPTION_B, BLANK, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_008(self):
        self.log.getthelogs().info('TEST CASE, test_008')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_009(self):
        self.log.getthelogs().info('TEST CASE, test_009')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, BLANK, OPTION_A, OPTION_B, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_010(self):
        self.log.getthelogs().info('TEST CASE, test_010')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, generate_random_string_subject(), BLANK, OPTION_B, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_011(self):
        self.log.getthelogs().info('TEST CASE, test_011')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, generate_random_string_subject(), OPTION_A, BLANK, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
