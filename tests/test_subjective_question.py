import allure
import pytest
from Utilities.constants import *
from Utilities.return_message import *
from Utilities.generate_email import *

@pytest.mark.usefixtures("setup_and_teardown")
class TestSubjectiveQuestion:
    
    @allure.severity(allure.severity_level.CRITICAL)
    def test_001(self):
        self.log.getthelogs().info('TEST CASE, test_001')
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), ADD, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_002(self):
        self.log.getthelogs().info('TEST CASE, test_002')
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, BLANK, generate_random_string_subject(), generate_random_string_subject(), ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.CRITICAL)
    def test_003(self):
        self.log.getthelogs().info('TEST CASE, test_003')
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), BLANK, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_004(self):
        self.log.getthelogs().info('TEST CASE, test_004')
        self.subjective_question.add_subjective_question(BLANK, PASSAGE_VALUE, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_005(self):
        self.log.getthelogs().info('TEST CASE, test_005')
        self.subjective_question.add_subjective_question(HINDI, BLANK, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), ADD, BLANK)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_006(self):
        self.log.getthelogs().info('TEST CASE, test_006')
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), BLANK, generate_random_string_subject(), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_007(self):
        self.log.getthelogs().info('TEST CASE, test_007')
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), generate_random_string_subject(), BLANK, ADD, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_008(self):
        self.log.getthelogs().info('TEST CASE, test_008')
        self.subjective_question.add_subjective_question(BLANK, BLANK, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_009(self):
        self.log.getthelogs().info('TEST CASE, test_009')
        self.subjective_question.add_subjective_question(BLANK, PASSAGE_VALUE, BLANK, generate_random_string_subject(), generate_random_string_subject(), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_010(self):
        self.log.getthelogs().info('TEST CASE, test_010')
        self.subjective_question.add_subjective_question(BLANK, PASSAGE_VALUE, generate_random_string_subject(), BLANK, generate_random_string_subject(), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_011(self):
        self.log.getthelogs().info('TEST CASE, test_011')
        self.subjective_question.add_subjective_question(BLANK, PASSAGE_VALUE, generate_random_string_subject(), generate_random_string_subject(), BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_012(self):
        self.log.getthelogs().info('TEST CASE, test_012')
        self.subjective_question.add_subjective_question(HINDI, BLANK, BLANK, generate_random_string_subject(), generate_random_string_subject(), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_013(self):
        self.log.getthelogs().info('TEST CASE, test_013')
        self.subjective_question.add_subjective_question(HINDI, BLANK, generate_random_string_subject(), BLANK, generate_random_string_subject(), ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_014(self):
        self.log.getthelogs().info('TEST CASE, test_014')
        self.subjective_question.add_subjective_question(HINDI, BLANK, generate_random_string_subject(), generate_random_string_subject(), BLANK, ADD, BLANK)

    @allure.severity(allure.severity_level.NORMAL)
    def test_015(self):
        self.log.getthelogs().info('TEST CASE, test_015')
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, BLANK, BLANK, generate_random_string_subject(), ADD, VALIDATION)
