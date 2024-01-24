import allure
import pytest

from Utilities.constants import *
from Utilities.return_message import *
from Utilities.generate_email import *

@pytest.mark.usefixtures("setup_and_teardown")
class TestMultipleChoiceQuestion:
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression 
    def test_001(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, OPTION_D, ADD, BLANK)
        
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression  
    def test_002(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, OPTION_D, BLANK, BLANK)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke    
    def test_003(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke     
    def test_004(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, BLANK, BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke 
    def test_005(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, generate_random_string_subject(), BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke     
    def test_006(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, OPTION_A, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke 
    def test_007(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, OPTION_B, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke     
    def test_008(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, BLANK, OPTION_C, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke 
    def test_009(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, BLANK, BLANK, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke 
    def test_010(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, BLANK, BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke 
    def test_011(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, generate_random_string_subject(), BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke 
    def test_012(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, OPTION_A, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke     
    def test_013(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, BLANK, OPTION_B, BLANK, BLANK, ADD, VALIDATION)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke 
    def test_014(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, BLANK, BLANK, OPTION_C, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke 
    def test_015(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, BLANK, BLANK, BLANK, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke 
    def test_016(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, generate_random_string_subject(), BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke 
    def test_017(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, BLANK, OPTION_A, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity    
    def test_018(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, BLANK, BLANK, OPTION_B, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke    
    def test_019(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, BLANK, BLANK, BLANK, OPTION_C, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_020(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, BLANK, BLANK, BLANK, BLANK, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke    
    def test_021(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, generate_random_string_subject(), OPTION_A, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke 
    def test_022(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, generate_random_string_subject(), BLANK, OPTION_B, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR) 
    @pytest.mark.smoke
    def test_023(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, generate_random_string_subject(), BLANK, BLANK, OPTION_C, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke 
    def test_024(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, generate_random_string_subject(), BLANK, BLANK, BLANK, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke 
    def test_025(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, OPTION_A, OPTION_B, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR) 
    @pytest.mark.smoke
    def test_026(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, OPTION_A, BLANK, OPTION_C, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke 
    def test_027(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, OPTION_A, BLANK, BLANK, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL) 
    @pytest.mark.smoke
    def test_028(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, OPTION_B, OPTION_C, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke 
    def test_029(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, OPTION_B, BLANK, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_030(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, BLANK, OPTION_C, OPTION_D, ADD, VALIDATION)
       
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_031(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_032(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, BLANK, OPTION_A, BLANK, BLANK, BLANK, ADD, VALIDATION)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_033(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, BLANK, BLANK, OPTION_B, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_034(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, BLANK, BLANK, BLANK, OPTION_C, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_035(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, BLANK, BLANK, BLANK, BLANK, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_036(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, generate_random_string_subject(), OPTION_A, BLANK, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_037(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, generate_random_string_subject(), BLANK, OPTION_B, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_038(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, generate_random_string_subject(), BLANK, BLANK, OPTION_C, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_039(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, generate_random_string_subject(), BLANK, BLANK, BLANK, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_040(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, OPTION_A, OPTION_B, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    @pytest.mark.smoke
    def test_041(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, OPTION_A, BLANK, OPTION_C, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_042(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, OPTION_A, BLANK, BLANK, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_043(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, BLANK, OPTION_B, OPTION_C, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_044(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, BLANK, OPTION_B, BLANK, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_045(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, BLANK, BLANK, OPTION_C, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_046(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, BLANK, BLANK, BLANK, ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_047(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, generate_random_string_subject(), BLANK, OPTION_B, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_048(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, generate_random_string_subject(), BLANK, BLANK, OPTION_C, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_049(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, generate_random_string_subject(), BLANK, BLANK, BLANK, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_050(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, BLANK, OPTION_A, OPTION_B, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_051(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, BLANK, BLANK, OPTION_B, OPTION_C, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_052(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, BLANK, BLANK, BLANK, OPTION_C, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_053(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, generate_random_string_subject(), OPTION_A, OPTION_B, BLANK, BLANK, ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_054(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, generate_random_string_subject(), BLANK, OPTION_B, OPTION_C, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_055(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, generate_random_string_subject(), BLANK, BLANK, OPTION_C, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_056(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, OPTION_A, OPTION_B, OPTION_C, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_057(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, OPTION_A, BLANK, OPTION_C, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_058(self):
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, OPTION_B, OPTION_C, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_059(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, BLANK, BLANK, BLANK, ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_060(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), BLANK, OPTION_B, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_061(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), BLANK, BLANK, OPTION_C, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_062(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), BLANK, BLANK, BLANK, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_063(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, BLANK, OPTION_A, OPTION_B, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_064(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, BLANK, BLANK, OPTION_B, OPTION_C, BLANK, ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_065(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, BLANK, BLANK, OPTION_B, OPTION_C, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_066(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, BLANK, BLANK, BLANK, OPTION_C, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_067(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, OPTION_B, BLANK, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_068(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, BLANK, OPTION_C, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_069(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, BLANK, BLANK, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_070(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), BLANK, OPTION_B, OPTION_C, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_071(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), BLANK, BLANK, OPTION_C, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_072(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, BLANK, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_073(self):
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, OPTION_B, BLANK, OPTION_D, ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_074(self):
        self.multiple_choice_question.add_question_multiple_choice_question_with_maxlength_validation(HINDI, PASSAGE_VALUE, generate_random_dynamic_string(INVALID_LENGTH_STRING), OPTION_A, OPTION_B, OPTION_C, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_075(self):
        self.multiple_choice_question.add_question_multiple_choice_question_with_maxlength_validation(HINDI, PASSAGE_VALUE, generate_random_string_subject(), generate_random_dynamic_string(INVALID_LENGTH_STRING), OPTION_B, OPTION_C, OPTION_D, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_076(self):
        self.multiple_choice_question.add_question_multiple_choice_question_with_maxlength_validation(HINDI, PASSAGE_VALUE, HINDI, OPTION_A, generate_random_dynamic_string(INVALID_LENGTH_STRING), OPTION_C, OPTION_D, ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_077(self):
        self.multiple_choice_question.add_question_multiple_choice_question_with_maxlength_validation(HINDI, PASSAGE_VALUE, HINDI, OPTION_A, OPTION_B, generate_random_dynamic_string(INVALID_LENGTH_STRING), OPTION_D, ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_078(self):
        self.multiple_choice_question.add_question_multiple_choice_question_with_maxlength_validation(HINDI, PASSAGE_VALUE, HINDI, OPTION_A, OPTION_B, OPTION_C, generate_random_dynamic_string(INVALID_LENGTH_STRING), ADD, VALIDATION)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_079(self):
        self.multiple_choice_question.delete_row_in_existing_table(ACCEPT)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_080(self):
        self.multiple_choice_question.delete_row_in_existing_table(BLANK)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_081(self):
        self.multiple_choice_question.search_functionality(QUESTION_MCQ, BLANK)
        self.multiple_choice_question.row_count_table()
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_082(self):
        self.multiple_choice_question.search_functionality(BLANK, HINDI)
        self.multiple_choice_question.row_count_table()
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_083(self):
        self.multiple_choice_question.search_functionality(QUESTION_MCQ, HINDI)
        self.multiple_choice_question.row_count_table()
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_084(self):
        self.multiple_choice_question.search_functionality(QUESTION_MCQD, HINDI)
        self.multiple_choice_question.no_data_found_validation()

    @allure.severity(allure.severity_level.MINOR)
    def test_085(self):
        self.multiple_choice_question.search_functionality(QUESTION_MCQ, MATHS)
        self.multiple_choice_question.no_data_found_validation()
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_086(self):
        self.multiple_choice_question.search_functionality(QUESTION_MCQD, MATHS)
        self.multiple_choice_question.no_data_found_validation()
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_087(self):
        self.multiple_choice_question.edit_row_of_existing_table()
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_088(self):
        self.multiple_choice_question.same_question_gives_on_presence_on_table(HINDI, PASSAGE_VALUE, OHMOBGT, OPTION_A, OPTION_B, OPTION_C, OPTION_D)
