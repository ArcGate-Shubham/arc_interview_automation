import pytest
from Utilities.constants import *
from Utilities.return_message import *
from Utilities.generate_email import *

@pytest.mark.usefixtures("setup_and_teardown")
class TestMultipleChoiceQuestion:
    
    def test_001(self):
        self.log.getthelogs().info('TEST CASE, test_001')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, OPTION_D, ADD, BLANK, 'Screenshots/test_001.png')
        
    def test_002(self):
        self.log.getthelogs().info('TEST CASE, test_002')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, OPTION_D, BLANK, BLANK, 'Screenshots/test_002.png')
        
    def test_003(self):
        self.log.getthelogs().info('TEST CASE, test_003')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_003.png')
        
    def test_004(self):
        self.log.getthelogs().info('TEST CASE, test_004')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, BLANK, BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_004.png')
    
    def test_005(self):
        self.log.getthelogs().info('TEST CASE, test_005')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, generate_random_string_subject(), BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_005.png')
        
    def test_006(self):
        self.log.getthelogs().info('TEST CASE, test_006')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, OPTION_A, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_006.png')
    
    def test_007(self):
        self.log.getthelogs().info('TEST CASE, test_007')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, OPTION_B, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_007.png')
        
    def test_008(self):
        self.log.getthelogs().info('TEST CASE, test_008')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, BLANK, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_008.png')
    
    def test_009(self):
        self.log.getthelogs().info('TEST CASE, test_009')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, BLANK, BLANK, OPTION_D, ADD, VALIDATION, 'Screenshots/test_009.png')
    
    def test_010(self):
        self.log.getthelogs().info('TEST CASE, test_010')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, BLANK, BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_010.png')
    
    def test_011(self):
        self.log.getthelogs().info('TEST CASE, test_011')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, generate_random_string_subject(), BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_011.png')
    
    def test_012(self):
        self.log.getthelogs().info('TEST CASE, test_012')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, OPTION_A, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_012.png')
        
    def test_013(self):
        self.log.getthelogs().info('TEST CASE, test_013')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, BLANK, OPTION_B, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_013.png')

    def test_014(self):
        self.log.getthelogs().info('TEST CASE, test_014')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, BLANK, BLANK, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_014.png')
    
    def test_015(self):
        self.log.getthelogs().info('TEST CASE, test_015')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, BLANK, BLANK, BLANK, OPTION_D, ADD, VALIDATION, 'Screenshots/test_015.png')
    
    def test_016(self):
        self.log.getthelogs().info('TEST CASE, test_015')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, generate_random_string_subject(), BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_016.png')
