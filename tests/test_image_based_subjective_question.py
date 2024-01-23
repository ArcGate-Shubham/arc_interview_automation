import allure
import pytest

from Utilities.constants import *
from Utilities.return_message import *
from Utilities.generate_email import *

@pytest.mark.usefixtures("setup_and_teardown")
class TestImageBasedSubjectiveQuestion:
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_001(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, generate_random_string_subject(), HINDI, IMAGE, ADD, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_002(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, generate_random_string_subject(), HINDI, IMAGE, BLANK, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_003(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_004(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, BLANK, BLANK, BLANK, ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_005(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(BLANK, HINDI, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_006(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(BLANK, BLANK, HINDI, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_007(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(BLANK, BLANK, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_008(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, generate_random_string_subject(), BLANK, BLANK, ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_009(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, BLANK, generate_random_string_subject(), BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_010(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, BLANK, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_011(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(BLANK, generate_random_string_subject(), generate_random_string_subject(), BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_012(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(BLANK, generate_random_string_subject(), BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_013(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(BLANK, BLANK, generate_random_string_subject(), IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_014(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, generate_random_string_subject(), generate_random_string_subject(), BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_015(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, generate_random_string_subject(), BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_016(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, BLANK, generate_random_string_subject(), IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_017(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(BLANK, generate_random_string_subject(), generate_random_string_subject(), IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_018(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, generate_random_string_subject(), generate_random_string_subject(), OTHER_IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_019(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(TYPING_TEST, generate_random_string_subject(), generate_random_string_subject(), IMAGE, ADD, BLANK)
        
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_020(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(EXCEL, generate_random_string_subject(), generate_random_string_subject(), IMAGE, ADD, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_021(self):
        self.image_based_subjective_question.add_new_image_based_subjective_question(HINDI, generate_random_string_subject(), generate_random_string_subject(), ANOTHER_IMAGE, ADD, VALIDATION)
