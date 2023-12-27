import allure
import pytest
from Utilities.constants import *
from Utilities.return_message import *
from Utilities.generate_email import *

@pytest.mark.usefixtures("setup_and_teardown")
class TestMultipleChoiceQuestion:
    
    @allure.severity(allure.severity_level.CRITICAL)
    def test_001(self):
        self.log.getthelogs().info('TEST CASE, test_001')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, OPTION_D, ADD, BLANK, 'Screenshots/test_001.png')
        
    @allure.severity(allure.severity_level.CRITICAL)  
    def test_002(self):
        self.log.getthelogs().info('TEST CASE, test_002')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, OPTION_D, BLANK, BLANK, 'Screenshots/test_002.png')
    
    @allure.severity(allure.severity_level.NORMAL)    
    def test_003(self):
        self.log.getthelogs().info('TEST CASE, test_003')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_003.png')
    
    @allure.severity(allure.severity_level.NORMAL)     
    def test_004(self):
        self.log.getthelogs().info('TEST CASE, test_004')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, BLANK, BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_004.png')
    
    @allure.severity(allure.severity_level.NORMAL) 
    def test_005(self):
        self.log.getthelogs().info('TEST CASE, test_005')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, generate_random_string_subject(), BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_005.png')
    
    @allure.severity(allure.severity_level.NORMAL)     
    def test_006(self):
        self.log.getthelogs().info('TEST CASE, test_006')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, OPTION_A, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_006.png')
    
    @allure.severity(allure.severity_level.NORMAL) 
    def test_007(self):
        self.log.getthelogs().info('TEST CASE, test_007')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, OPTION_B, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_007.png')
    
    @allure.severity(allure.severity_level.NORMAL)     
    def test_008(self):
        self.log.getthelogs().info('TEST CASE, test_008')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, BLANK, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_008.png')
    
    @allure.severity(allure.severity_level.NORMAL) 
    def test_009(self):
        self.log.getthelogs().info('TEST CASE, test_009')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, BLANK, BLANK, OPTION_D, ADD, VALIDATION, 'Screenshots/test_009.png')
    
    @allure.severity(allure.severity_level.NORMAL) 
    def test_010(self):
        self.log.getthelogs().info('TEST CASE, test_010')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, BLANK, BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_010.png')
    
    @allure.severity(allure.severity_level.NORMAL) 
    def test_011(self):
        self.log.getthelogs().info('TEST CASE, test_011')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, generate_random_string_subject(), BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_011.png')
    
    @allure.severity(allure.severity_level.MINOR) 
    def test_012(self):
        self.log.getthelogs().info('TEST CASE, test_012')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, OPTION_A, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_012.png')
    
    @allure.severity(allure.severity_level.MINOR)     
    def test_013(self):
        self.log.getthelogs().info('TEST CASE, test_013')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, BLANK, OPTION_B, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_013.png')

    @allure.severity(allure.severity_level.MINOR) 
    def test_014(self):
        self.log.getthelogs().info('TEST CASE, test_014')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, BLANK, BLANK, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_014.png')
    
    @allure.severity(allure.severity_level.MINOR) 
    def test_015(self):
        self.log.getthelogs().info('TEST CASE, test_015')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, BLANK, BLANK, BLANK, OPTION_D, ADD, VALIDATION, 'Screenshots/test_015.png')
    
    @allure.severity(allure.severity_level.MINOR) 
    def test_016(self):
        self.log.getthelogs().info('TEST CASE, test_016')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, generate_random_string_subject(), BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_016.png')

    @allure.severity(allure.severity_level.NORMAL) 
    def test_017(self):
        self.log.getthelogs().info('TEST CASE, test_017')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, BLANK, OPTION_A, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_017.png')
    
    @allure.severity(allure.severity_level.NORMAL)    
    def test_018(self):
        self.log.getthelogs().info('TEST CASE, test_018')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, BLANK, BLANK, OPTION_B, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_018.png')
    
    @allure.severity(allure.severity_level.NORMAL)    
    def test_019(self):
        self.log.getthelogs().info('TEST CASE, test_019')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, BLANK, BLANK, BLANK, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_019.png')
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_020(self):
        self.log.getthelogs().info('TEST CASE, test_020')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, BLANK, BLANK, BLANK, BLANK, OPTION_D, ADD, VALIDATION, 'Screenshots/test_020.png')
    
    @allure.severity(allure.severity_level.MINOR)    
    def test_021(self):
        self.log.getthelogs().info('TEST CASE, test_021')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, generate_random_string_subject(), OPTION_A, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_021.png')
    
    @allure.severity(allure.severity_level.MINOR) 
    def test_022(self):
        self.log.getthelogs().info('TEST CASE, test_022')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, generate_random_string_subject(), BLANK, OPTION_B, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_022.png')
    
    @allure.severity(allure.severity_level.MINOR) 
    def test_023(self):
        self.log.getthelogs().info('TEST CASE, test_023')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, generate_random_string_subject(), BLANK, BLANK, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_023.png')
    
    @allure.severity(allure.severity_level.MINOR) 
    def test_024(self):
        self.log.getthelogs().info('TEST CASE, test_024')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, generate_random_string_subject(), BLANK, BLANK, BLANK, OPTION_D, ADD, VALIDATION, 'Screenshots/test_024.png')
    
    @allure.severity(allure.severity_level.MINOR) 
    def test_025(self):
        self.log.getthelogs().info('TEST CASE, test_025')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, OPTION_A, OPTION_B, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_025.png')
    
    @allure.severity(allure.severity_level.MINOR) 
    def test_026(self):
        self.log.getthelogs().info('TEST CASE, test_026')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, OPTION_A, BLANK, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_026.png')
    
    @allure.severity(allure.severity_level.MINOR) 
    def test_027(self):
        self.log.getthelogs().info('TEST CASE, test_027')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, OPTION_A, BLANK, BLANK, OPTION_D, ADD, VALIDATION, 'Screenshots/test_027.png')
    
    @allure.severity(allure.severity_level.NORMAL) 
    def test_028(self):
        self.log.getthelogs().info('TEST CASE, test_028')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, OPTION_B, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_028.png')
    
    @allure.severity(allure.severity_level.MINOR) 
    def test_029(self):
        self.log.getthelogs().info('TEST CASE, test_029')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, OPTION_B, BLANK, OPTION_D, ADD, VALIDATION, 'Screenshots/test_029.png')
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_030(self):
        self.log.getthelogs().info('TEST CASE, test_030')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, BLANK, OPTION_C, OPTION_D, ADD, VALIDATION, 'Screenshots/test_030.png')
