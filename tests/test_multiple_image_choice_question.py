import pytest
import configparser

from Utilities.logger import logclass
from PageObjects.MultipleImageChoiceQuestionPage import MultipleImageChoiceQuestion
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

@pytest.mark.usefixtures("setup_and_teardown")
class TestMultipleImageChoiceQuestion:
    
    def setup_method(self):
        self.log = logclass().getthelogs()
        
    def test_001(self):
        self.log.info('TEST CASE, test_001')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_multiple_image_choice_question()
        
    def test_002(self):
        self.log.info('TEST CASE, test_002')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('what is your name','/home/arcgate/Pictures/Screenshot1.png', '/home/arcgate/Pictures/Screenshot1.png','/home/arcgate/Pictures/Screenshot1.png', '/home/arcgate/Pictures/Screenshot1.png', 'add')
        multiple_image_choice_question.display_success_message_for_multiple_image_choice_question('Question added successfully','Screenshots/test_002.png')
            
    def test_003(self):
        self.log.info('TEST CASE, test_003')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('what is your name','', '','', '', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_003.png')
            
    def test_004(self):
        self.log.info('TEST CASE, test_004')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('what is your name','/home/arcgate/Pictures/Screenshot1.png', '','', '', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_004.png')
            
    def test_005(self):
        self.log.info('TEST CASE, test_005')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('what is your name','/home/arcgate/Pictures/Screenshot1.png', '/home/arcgate/Pictures/Screenshot1.png','', '', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_005.png')
        
    def test_006(self):
        self.log.info('TEST CASE, test_006')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('what is your name','/home/arcgate/Pictures/Screenshot1.png', '/home/arcgate/Pictures/Screenshot1.png','/home/arcgate/Pictures/Screenshot1.png', '', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_006.png')

    def test_007(self):
        self.log.info('TEST CASE, test_007')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('','/home/arcgate/Pictures/Screenshot1.png', '','', '', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_007.png')
    
    def test_008(self):
        self.log.info('TEST CASE, test_008')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('','', '/home/arcgate/Pictures/Screenshot1.png','', '', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_008.png')
        
    def test_009(self):
        self.log.info('TEST CASE, test_009')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('','', '', '/home/arcgate/Pictures/Screenshot1.png', '', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_009.png')
        
    def test_010(self):
        self.log.info('TEST CASE, test_010')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('','', '', '', '/home/arcgate/Pictures/Screenshot1.png', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_010.png')

    def test_011(self):
        self.log.info('TEST CASE, test_011')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('what is your name','', '/home/arcgate/Pictures/Screenshot1.png', '', '', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_011.png')
        
    def test_012(self):
        self.log.info('TEST CASE, test_012')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('what is your name','', '', '/home/arcgate/Pictures/Screenshot1.png', '', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_012.png')
    
    def test_013(self):
        self.log.info('TEST CASE, test_013')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('what is your name','', '', '', '/home/arcgate/Pictures/Screenshot1.png', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_013.png')
    
    def test_014(self):
        self.log.info('TEST CASE, test_014')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('','/home/arcgate/Pictures/Screenshot1.png', '/home/arcgate/Pictures/Screenshot1.png', '', '', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_014.png')
    
    def test_015(self):
        self.log.info('TEST CASE, test_015')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('','/home/arcgate/Pictures/Screenshot1.png', '', '/home/arcgate/Pictures/Screenshot1.png', '', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_015.png')
    
    def test_016(self):
        self.log.info('TEST CASE, test_016')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('','/home/arcgate/Pictures/Screenshot1.png', '', '', '/home/arcgate/Pictures/Screenshot1.png', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_016.png')
        
    def test_017(self):
        self.log.info('TEST CASE, test_017')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('','', '/home/arcgate/Pictures/Screenshot1.png', '', '/home/arcgate/Pictures/Screenshot1.png', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_017.png')
    
    def test_018(self):
        self.log.info('TEST CASE, test_018')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('','', '', '/home/arcgate/Pictures/Screenshot1.png', '/home/arcgate/Pictures/Screenshot1.png', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_018.png')
        
    def test_019(self):
        self.log.info('TEST CASE, test_019')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('what is your name', '/home/arcgate/Pictures/Screenshot1.png', '','/home/arcgate/Pictures/Screenshot1.png','', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_019.png')
    
    def test_020(self):
        self.log.info('TEST CASE, test_020')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('what is your name', '/home/arcgate/Pictures/Screenshot1.png', '','','/home/arcgate/Pictures/Screenshot1.png', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_020.png')
    
    def test_021(self):
        self.log.info('TEST CASE, test_021')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('what is your name', '', '/home/arcgate/Pictures/Screenshot1.png','','/home/arcgate/Pictures/Screenshot1.png', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_021.png')
    
    def test_022(self):
        self.log.info('TEST CASE, test_022')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('what is your name', '', '','/home/arcgate/Pictures/Screenshot1.png','/home/arcgate/Pictures/Screenshot1.png', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_022.png')
        
    def test_023(self):
        self.log.info('TEST CASE, test_023')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('', '/home/arcgate/Pictures/Screenshot1.png', '','/home/arcgate/Pictures/Screenshot1.png','/home/arcgate/Pictures/Screenshot1.png', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_023.png')
    
    def test_024(self):
        self.log.info('TEST CASE, test_024')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('', '', '/home/arcgate/Pictures/Screenshot1.png','/home/arcgate/Pictures/Screenshot1.png','/home/arcgate/Pictures/Screenshot1.png', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_024.png')
    
    def test_025(self):
        self.log.info('TEST CASE, test_025')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('what is your name', '', '/home/arcgate/Pictures/Screenshot1.png','/home/arcgate/Pictures/Screenshot1.png','/home/arcgate/Pictures/Screenshot1.png', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_025.png')
    
    def test_026(self):
        self.log.info('TEST CASE, test_026')
        multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        multiple_image_choice_question.add_new_question_with_all_valid_input('', '/home/arcgate/Pictures/Screenshot1.png', '/home/arcgate/Pictures/Screenshot1.png','/home/arcgate/Pictures/Screenshot1.png','/home/arcgate/Pictures/Screenshot1.png', 'add')
        multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_026.png')
