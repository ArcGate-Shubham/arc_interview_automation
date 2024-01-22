import allure
import pytest
from Utilities.constants import *
from Utilities.return_message import *
from Utilities.generate_email import *

@pytest.mark.usefixtures("setup_and_teardown")
class TestSubjectiveQuestion:
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
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
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_016(self):
        self.log.getthelogs().info('TEST CASE, test_016')
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, BLANK, generate_random_string_subject(), BLANK, ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_017(self):
        self.log.getthelogs().info('TEST CASE, test_017')
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_018(self):
        self.log.getthelogs().info('TEST CASE, test_018')
        self.subjective_question.add_subjective_question(BLANK, BLANK, BLANK, generate_random_string_subject(), generate_random_string_subject(), ADD, VALIDATION)

    @allure.severity(allure.severity_level.NORMAL)
    def test_019(self):
        self.log.getthelogs().info('TEST CASE, test_019')
        self.subjective_question.add_subjective_question(BLANK, BLANK, generate_random_string_subject(), BLANK, generate_random_string_subject(), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_020(self):
        self.log.getthelogs().info('TEST CASE, test_020')
        self.subjective_question.add_subjective_question(BLANK, BLANK, generate_random_string_subject(), generate_random_string_subject(), BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_021(self):
        self.log.getthelogs().info('TEST CASE, test_021')
        self.subjective_question.add_subjective_question(BLANK, PASSAGE_VALUE, BLANK, BLANK, generate_random_string_subject(), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_022(self):
        self.log.getthelogs().info('TEST CASE, test_022')
        self.subjective_question.add_subjective_question(BLANK, PASSAGE_VALUE, generate_random_string_subject(), BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_023(self):
        self.log.getthelogs().info('TEST CASE, test_023')
        self.subjective_question.add_subjective_question(HINDI, BLANK, BLANK, BLANK, generate_random_string_subject(), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_024(self):
        self.log.getthelogs().info('TEST CASE, test_024')
        self.subjective_question.add_subjective_question(HINDI, BLANK, generate_random_string_subject(), BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_024(self):
        self.log.getthelogs().info('TEST CASE, test_024')
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_025(self):
        self.log.getthelogs().info('TEST CASE, test_025')
        self.subjective_question.add_subjective_question(BLANK, BLANK, BLANK, BLANK, generate_random_string_subject(), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_026(self):
        self.log.getthelogs().info('TEST CASE, test_026')
        self.subjective_question.add_subjective_question(BLANK, BLANK, BLANK, generate_random_string_subject(), BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_026(self):
        self.log.getthelogs().info('TEST CASE, test_026')
        self.subjective_question.add_subjective_question(BLANK, BLANK, generate_random_string_subject(), BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_027(self):
        self.log.getthelogs().info('TEST CASE, test_027')
        self.subjective_question.add_subjective_question(BLANK, PASSAGE_VALUE, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_028(self):
        self.log.getthelogs().info('TEST CASE, test_028')
        self.subjective_question.add_subjective_question(HINDI, BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_029(self):
        self.log.getthelogs().info('TEST CASE, test_029')
        self.subjective_question.add_subjective_question(BLANK, BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_030(self):
        self.log.getthelogs().info('TEST CASE, test_030')
        self.subjective_question.add_subjective_question(TYPING_TEST, PASSAGE_VALUE, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), ADD, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_031(self):
        self.log.getthelogs().info('TEST CASE, test_031')
        self.subjective_question.add_subjective_question(EXCEL, PASSAGE_VALUE, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), ADD, BLANK)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_032(self):
        self.log.getthelogs().info('TEST CASE, test_032')
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, generate_random_dynamic_string(INVALID_LENGTH_STRING), generate_random_string_subject(), generate_random_string_subject(), ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_033(self):
        self.log.getthelogs().info('TEST CASE, test_033')
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), generate_random_dynamic_string(INVALID_LENGTH_STRING), generate_random_string_subject(), ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_034(self):
        self.log.getthelogs().info('TEST CASE, test_034')
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), generate_random_string_subject(), generate_random_dynamic_string(INVALID_LENGTH_STRING), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_035(self):
        self.log.getthelogs().info('TEST CASE, test_035')
        self.subjective_question.search_functionality(QUESTION_MICQ, BLANK, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_036(self):
        self.log.getthelogs().info('TEST CASE, test_036')
        self.subjective_question.search_functionality(BLANK, HINDI, BLANK)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_037(self):
        self.log.getthelogs().info('TEST CASE, test_037')
        self.subjective_question.search_functionality(QUESTION_MICQ, HINDI, BLANK)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_038(self):
        self.log.getthelogs().info('TEST CASE, test_038')
        self.subjective_question.search_functionality(BLANK, BLANK, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_039(self):
        self.log.getthelogs().info('TEST CASE, test_039')
        self.subjective_question.search_functionality(WRONG_SEARCH, BLANK, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_040(self):
        self.log.getthelogs().info('TEST CASE, test_040')
        self.subjective_question.search_functionality(BLANK, MATHS, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_041(self):
        self.log.getthelogs().info('TEST CASE, test_041')
        self.subjective_question.search_functionality(WRONG_SEARCH, MATHS, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_042(self):
        self.log.getthelogs().info('TEST CASE, test_042')
        self.subjective_question.delete_row_in_table(ACCEPT)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_043(self):
        self.log.getthelogs().info('TEST CASE, test_043')
        self.subjective_question.delete_row_in_table(BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_044(self):
        self.log.getthelogs().info('TEST CASE, test_044')
        self.subjective_question.edit_row_of_existing_table()
