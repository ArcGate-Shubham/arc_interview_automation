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
