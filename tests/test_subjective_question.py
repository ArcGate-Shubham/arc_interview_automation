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
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), ADD, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_002(self):
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, BLANK, generate_random_string_subject(), generate_random_string_subject(), ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_003(self):
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), BLANK, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_004(self):
        self.subjective_question.add_subjective_question(BLANK, PASSAGE_VALUE, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_005(self):
        self.subjective_question.add_subjective_question(HINDI, BLANK, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), ADD, BLANK)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_006(self):
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), BLANK, generate_random_string_subject(), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_007(self):
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), generate_random_string_subject(), BLANK, ADD, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_008(self):
        self.subjective_question.add_subjective_question(BLANK, BLANK, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_009(self):
        self.subjective_question.add_subjective_question(BLANK, PASSAGE_VALUE, BLANK, generate_random_string_subject(), generate_random_string_subject(), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_010(self):
        self.subjective_question.add_subjective_question(BLANK, PASSAGE_VALUE, generate_random_string_subject(), BLANK, generate_random_string_subject(), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_011(self):
        self.subjective_question.add_subjective_question(BLANK, PASSAGE_VALUE, generate_random_string_subject(), generate_random_string_subject(), BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_012(self):
        self.subjective_question.add_subjective_question(HINDI, BLANK, BLANK, generate_random_string_subject(), generate_random_string_subject(), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_013(self):
        self.subjective_question.add_subjective_question(HINDI, BLANK, generate_random_string_subject(), BLANK, generate_random_string_subject(), ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_014(self):
        self.subjective_question.add_subjective_question(HINDI, BLANK, generate_random_string_subject(), generate_random_string_subject(), BLANK, ADD, BLANK)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_015(self):
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, BLANK, BLANK, generate_random_string_subject(), ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_016(self):
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, BLANK, generate_random_string_subject(), BLANK, ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_017(self):
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_018(self):
        self.subjective_question.add_subjective_question(BLANK, BLANK, BLANK, generate_random_string_subject(), generate_random_string_subject(), ADD, VALIDATION)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_019(self):
        self.subjective_question.add_subjective_question(BLANK, BLANK, generate_random_string_subject(), BLANK, generate_random_string_subject(), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_020(self):
        self.subjective_question.add_subjective_question(BLANK, BLANK, generate_random_string_subject(), generate_random_string_subject(), BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_021(self):
        self.subjective_question.add_subjective_question(BLANK, PASSAGE_VALUE, BLANK, BLANK, generate_random_string_subject(), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_022(self):
        self.subjective_question.add_subjective_question(BLANK, PASSAGE_VALUE, generate_random_string_subject(), BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_023(self):
        self.subjective_question.add_subjective_question(HINDI, BLANK, BLANK, BLANK, generate_random_string_subject(), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_024(self):
        self.subjective_question.add_subjective_question(HINDI, BLANK, generate_random_string_subject(), BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_024(self):
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_025(self):
        self.subjective_question.add_subjective_question(BLANK, BLANK, BLANK, BLANK, generate_random_string_subject(), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_026(self):
        self.subjective_question.add_subjective_question(BLANK, BLANK, BLANK, generate_random_string_subject(), BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_026(self):
        self.subjective_question.add_subjective_question(BLANK, BLANK, generate_random_string_subject(), BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_027(self):
        self.subjective_question.add_subjective_question(BLANK, PASSAGE_VALUE, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_028(self):
        self.subjective_question.add_subjective_question(HINDI, BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_029(self):
        self.subjective_question.add_subjective_question(BLANK, BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_030(self):
        self.subjective_question.add_subjective_question(TYPING_TEST, PASSAGE_VALUE, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), ADD, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_031(self):
        self.subjective_question.add_subjective_question(EXCEL, PASSAGE_VALUE, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), ADD, BLANK)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_032(self):
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, generate_random_dynamic_string(INVALID_LENGTH_STRING), generate_random_string_subject(), generate_random_string_subject(), ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_033(self):
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), generate_random_dynamic_string(INVALID_LENGTH_STRING), generate_random_string_subject(), ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_034(self):
        self.subjective_question.add_subjective_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), generate_random_string_subject(), generate_random_dynamic_string(INVALID_LENGTH_STRING), ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_035(self):
        self.subjective_question.search_functionality(QUESTION_MICQ, BLANK, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_036(self):
        self.subjective_question.search_functionality(BLANK, HINDI, BLANK)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_037(self):
        self.subjective_question.search_functionality(QUESTION_MICQ, HINDI, BLANK)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_038(self):
        self.subjective_question.search_functionality(BLANK, BLANK, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_039(self):
        self.subjective_question.search_functionality(WRONG_SEARCH, BLANK, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_040(self):
        self.subjective_question.search_functionality(BLANK, MATHS, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_041(self):
        self.subjective_question.search_functionality(WRONG_SEARCH, MATHS, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_042(self):
        self.subjective_question.delete_row_in_table(ACCEPT)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_043(self):
        self.subjective_question.delete_row_in_table(BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_044(self):
        self.subjective_question.edit_row_of_existing_table()
