import pytest
from Utilities.constants import *
from Utilities.return_message import *

@pytest.mark.usefixtures("setup_and_teardown")
class TestMultipleImageChoiceQuestion:

    def test_001(self):
        self.log.getthelogs().info('TEST CASE, test_001')
        self.multiple_image_choice_question.add_new_question_multiple_image_choice_question()

    def test_002(self):
        self.log.getthelogs().info('TEST CASE, test_002')
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ,IMAGE, IMAGE,IMAGE, IMAGE, ADD)
        self.multiple_image_choice_question.display_success_message_for_multiple_image_choice_question(QUESTION_ADDED,'Screenshots/test_002.png')

    def test_003(self):
        self.log.getthelogs().info('TEST CASE, test_003')
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ,BLANK, BLANK,BLANK, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_003.png')

    def test_004(self):
        self.log.getthelogs().info('TEST CASE, test_004')
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ,IMAGE, BLANK,BLANK, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_004.png')

    def test_005(self):
        self.log.getthelogs().info('TEST CASE, test_005')
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ,IMAGE, IMAGE,BLANK, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_005.png')

    def test_006(self):
        self.log.getthelogs().info('TEST CASE, test_006')
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ,IMAGE, IMAGE,IMAGE, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_006.png')

    def test_007(self):
        self.log.getthelogs().info('TEST CASE, test_007')
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK,IMAGE, BLANK,BLANK, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_007.png')

    def test_008(self):
        self.log.getthelogs().info('TEST CASE, test_008')
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK,BLANK, IMAGE,BLANK, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_008.png')

    def test_009(self):
        self.log.getthelogs().info('TEST CASE, test_009')
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK,BLANK, BLANK, IMAGE, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_009.png')

    def test_010(self):
        self.log.getthelogs().info('TEST CASE, test_010')
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK,BLANK, BLANK, BLANK, IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_010.png')

    def test_011(self):
        self.log.getthelogs().info('TEST CASE, test_011')
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ,BLANK, IMAGE, BLANK, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_011.png')

    def test_012(self):
        self.log.getthelogs().info('TEST CASE, test_012')
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ,BLANK, BLANK, IMAGE, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_012.png')

    def test_013(self):
        self.log.getthelogs().info('TEST CASE, test_013')
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ,BLANK, BLANK, BLANK, IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_013.png')

    def test_014(self):
        self.log.getthelogs().info('TEST CASE, test_014')     
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK,IMAGE, IMAGE, BLANK, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_014.png')

    def test_015(self):
        self.log.getthelogs().info('TEST CASE, test_015')      
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK,IMAGE, BLANK, IMAGE, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_015.png')

    def test_016(self):
        self.log.getthelogs().info('TEST CASE, test_016')       
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK,IMAGE, BLANK, BLANK, IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_016.png')

    def test_017(self):
        self.log.getthelogs().info('TEST CASE, test_017')     
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK,BLANK, IMAGE, BLANK, IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_017.png')

    def test_018(self):
        self.log.getthelogs().info('TEST CASE, test_018')      
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK,BLANK, BLANK, IMAGE, IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_018.png')

    def test_019(self):
        self.log.getthelogs().info('TEST CASE, test_019')       
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ, IMAGE, BLANK,IMAGE,BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_019.png')

    def test_020(self):
        self.log.getthelogs().info('TEST CASE, test_020')    
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ, IMAGE, BLANK,BLANK,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_020.png')

    def test_021(self):
        self.log.getthelogs().info('TEST CASE, test_021')        
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ, BLANK, IMAGE,BLANK,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_021.png')

    def test_022(self):
        self.log.getthelogs().info('TEST CASE, test_022')        
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ, BLANK, BLANK,IMAGE,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_022.png')

    def test_023(self):
        self.log.getthelogs().info('TEST CASE, test_023')        
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK, IMAGE, BLANK,IMAGE,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_023.png')

    def test_024(self):
        self.log.getthelogs().info('TEST CASE, test_024')        
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK, BLANK, IMAGE,IMAGE,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_024.png')

    def test_025(self):
        self.log.getthelogs().info('TEST CASE, test_025')        
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ, BLANK, IMAGE,IMAGE,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_025.png')

    def test_026(self):
        self.log.getthelogs().info('TEST CASE, test_026')
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK, IMAGE, IMAGE,IMAGE,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_026.png')

    def test_027(self):
        self.log.getthelogs().info('TEST CASE, test_027')
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ, BLANK, IMAGE,IMAGE,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_027.png')
    
    def test_028(self):
        self.log.getthelogs().info('TEST CASE, test_028')
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ, IMAGE, BLANK,IMAGE,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_028.png')
    
    def test_029(self):
        self.log.getthelogs().info('TEST CASE, test_029')
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ, IMAGE, IMAGE,BLANK,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required('Screenshots/test_029.png')
        
    def test_030(self):
        self.log.getthelogs().info('TEST CASE, test_030')
        self.multiple_image_choice_question.search_functionality_for_multiple_image_choice_question(SEARCH_QUESTION_MICQ, BLANK)
        self.multiple_image_choice_question.search_after_row_count('Screenshots/test_030.png')
        
    def test_031(self):
        self.log.getthelogs().info('TEST CASE, test_031')
        self.multiple_image_choice_question.search_functionality_for_multiple_image_choice_question(BLANK, HINDI)
        self.multiple_image_choice_question.search_after_row_count('Screenshots/test_031.png')
    
    def test_032(self):
        self.log.getthelogs().info('TEST CASE, test_032')
        self.multiple_image_choice_question.search_functionality_for_multiple_image_choice_question(SEARCH_QUESTION_MICQ, HINDI)
        self.multiple_image_choice_question.search_after_row_count('Screenshots/test_032.png')
    
    def test_033(self):
        self.log.getthelogs().info('TEST CASE, test_033')
        self.multiple_image_choice_question.search_functionality_for_multiple_image_choice_question(BLANK, BLANK)
        self.multiple_image_choice_question.search_after_row_count('Screenshots/test_033.png')
    
    def test_034(self):
        self.log.getthelogs().info('TEST CASE, test_034')
        self.multiple_image_choice_question.search_functionality_for_multiple_image_choice_question(WRONG_SEARCH, BLANK)
        self.multiple_image_choice_question.display_success_message_for_multiple_image_choice_question(NO_DATA,'Screenshots/test_034.png')
    
    def test_035(self):
        self.log.getthelogs().info('TEST CASE, test_035')
        self.multiple_image_choice_question.search_functionality_for_multiple_image_choice_question(BLANK, MATHS)
        self.multiple_image_choice_question.display_success_message_for_multiple_image_choice_question(NO_DATA,'Screenshots/test_035.png')

    def test_036(self):
        self.log.getthelogs().info('TEST CASE, test_036')
        self.multiple_image_choice_question.search_functionality_for_multiple_image_choice_question(SEARCH_QUESTION_MICQ, MATHS)
        self.multiple_image_choice_question.display_success_message_for_multiple_image_choice_question(NO_DATA,'Screenshots/test_036.png')
        
    def test_037(self):
        self.log.getthelogs().info('TEST CASE, test_037')
        self.multiple_image_choice_question.search_functionality_for_multiple_image_choice_question(THAR, HINDI)
        self.multiple_image_choice_question.display_success_message_for_multiple_image_choice_question(NO_DATA,'Screenshots/test_037.png')
        
    def test_038(self):
        self.log.getthelogs().info('TEST CASE, test_038')
        self.multiple_image_choice_question.search_functionality_for_multiple_image_choice_question(CASCSA, MATHS)
        self.multiple_image_choice_question.display_success_message_for_multiple_image_choice_question(NO_DATA,'Screenshots/test_038.png')
        
    def test_039(self):
        self.log.getthelogs().info('TEST CASE, test_039')
        self.multiple_image_choice_question.delete_row_in_existing_table(BLANK,'Screenshots/test_039.png' )
        
    def test_040(self):
        self.log.getthelogs().info('TEST CASE, test_040')
        self.multiple_image_choice_question.delete_row_in_existing_table(ACCEPT,'Screenshots/test_040.png' )
        
    def test_041(self):
        self.log.getthelogs().info('TEST CASE, test_041')
        self.multiple_image_choice_question.edit_row_in_existing_table(CLOSE_BUTTON,BLANK,'Screenshots/test_041.png')
        
    def test_042(self):
        self.log.getthelogs().info('TEST CASE, test_042')
        self.multiple_image_choice_question.edit_row_in_existing_table(BLANK,BLANK,'Screenshots/test_042.png')
        
    def test_043(self):
        self.log.getthelogs().info('TEST CASE, test_043')
        self.multiple_image_choice_question.edit_row_in_existing_table(BLANK,CLEAR_QUESTION,'Screenshots/test_043.png')
