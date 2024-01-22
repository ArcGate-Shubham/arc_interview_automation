import allure
import pytest
from Utilities.constants import *
from Utilities.return_message import *
from Utilities.generate_email import *

@pytest.mark.usefixtures("setup_and_teardown")
class TestImageBasedMultipleChoiceQuestion:
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_001(self):
        self.log.getthelogs().info('TEST CASE, test_001')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, OPTION_D, IMAGE, ADD, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_002(self):
        self.log.getthelogs().info('TEST CASE, test_002')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, OPTION_D, IMAGE, BLANK, BLANK)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_003(self):
        self.log.getthelogs().info('TEST CASE, test_003')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_004(self):
        self.log.getthelogs().info('TEST CASE, test_004')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, BLANK, OPTION_A, OPTION_B, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_005(self):
        self.log.getthelogs().info('TEST CASE, test_005')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), BLANK, OPTION_B, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    @pytest.mark.smoke
    def test_006(self):
        self.log.getthelogs().info('TEST CASE, test_006')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), OPTION_A, BLANK, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_007(self):
        self.log.getthelogs().info('TEST CASE, test_007')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), OPTION_A, OPTION_B, BLANK, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_008(self):
        self.log.getthelogs().info('TEST CASE, test_008')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_009(self):
        self.log.getthelogs().info('TEST CASE, test_009')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, BLANK, OPTION_A, OPTION_B, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_010(self):
        self.log.getthelogs().info('TEST CASE, test_010')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, generate_random_string_subject(), BLANK, OPTION_B, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_011(self):
        self.log.getthelogs().info('TEST CASE, test_011')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, generate_random_string_subject(), OPTION_A, BLANK, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_012(self):
        self.log.getthelogs().info('TEST CASE, test_012')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, generate_random_string_subject(), OPTION_A, OPTION_B, BLANK, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_013(self):
        self.log.getthelogs().info('TEST CASE, test_013')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_014(self):
        self.log.getthelogs().info('TEST CASE, test_014')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, BLANK, BLANK, OPTION_B, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_015(self):
        self.log.getthelogs().info('TEST CASE, test_015')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, BLANK, OPTION_A, BLANK, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_016(self):
        self.log.getthelogs().info('TEST CASE, test_016')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, BLANK, OPTION_A, OPTION_B, BLANK, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_017(self):
        self.log.getthelogs().info('TEST CASE, test_017')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, BLANK, OPTION_A, OPTION_B, OPTION_C, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_018(self):
        self.log.getthelogs().info('TEST CASE, test_018')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), BLANK, BLANK, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_019(self):
        self.log.getthelogs().info('TEST CASE, test_019')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), BLANK, OPTION_B, BLANK, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_020(self):
        self.log.getthelogs().info('TEST CASE, test_020')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), BLANK, OPTION_B, OPTION_C, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_021(self):
        self.log.getthelogs().info('TEST CASE, test_021')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), OPTION_A, BLANK, BLANK, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_022(self):
        self.log.getthelogs().info('TEST CASE, test_022')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), OPTION_A, BLANK, OPTION_C, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_023(self):
        self.log.getthelogs().info('TEST CASE, test_023')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), OPTION_A, OPTION_B, BLANK, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_024(self):
        self.log.getthelogs().info('TEST CASE, test_024')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, BLANK, BLANK, OPTION_B, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_025(self):
        self.log.getthelogs().info('TEST CASE, test_025')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, BLANK, OPTION_A, BLANK, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_026(self):
        self.log.getthelogs().info('TEST CASE, test_026')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, BLANK, OPTION_A, OPTION_B, BLANK, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_027(self):
        self.log.getthelogs().info('TEST CASE, test_027')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, BLANK, OPTION_A, OPTION_B, OPTION_C, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_028(self):
        self.log.getthelogs().info('TEST CASE, test_028')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, generate_random_string_subject(), BLANK, BLANK, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_029(self):
        self.log.getthelogs().info('TEST CASE, test_029')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, generate_random_string_subject(), OPTION_A, BLANK, BLANK, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_030(self):
        self.log.getthelogs().info('TEST CASE, test_030')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, generate_random_string_subject(), OPTION_A, OPTION_B, BLANK, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_031(self):
        self.log.getthelogs().info('TEST CASE, test_031')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_032(self):
        self.log.getthelogs().info('TEST CASE, test_032')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, BLANK, BLANK, OPTION_B, BLANK, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_033(self):
        self.log.getthelogs().info('TEST CASE, test_033')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, BLANK, BLANK, OPTION_B, OPTION_C, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_034(self):
        self.log.getthelogs().info('TEST CASE, test_034')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, BLANK, OPTION_A, OPTION_B, BLANK, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_035(self):
        self.log.getthelogs().info('TEST CASE, test_035')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, generate_random_string_subject(), OPTION_A, BLANK, BLANK, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_036(self):
        self.log.getthelogs().info('TEST CASE, test_036')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), BLANK, BLANK, BLANK, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_037(self):
        self.log.getthelogs().info('TEST CASE, test_037')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, BLANK, BLANK, BLANK, BLANK, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_038(self):
        self.log.getthelogs().info('TEST CASE, test_038')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, generate_random_string_subject(), BLANK, BLANK, BLANK, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_039(self):
        self.log.getthelogs().info('TEST CASE, test_039')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, BLANK, OPTION_A, BLANK, BLANK, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_040(self):
        self.log.getthelogs().info('TEST CASE, test_040')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, BLANK, BLANK, OPTION_B, BLANK, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_041(self):
        self.log.getthelogs().info('TEST CASE, test_041')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, OPTION_C, BLANK, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_042(self):
        self.log.getthelogs().info('TEST CASE, test_042')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, BLANK, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_043(self):
        self.log.getthelogs().info('TEST CASE, test_043')
        self.image_based_multiple_choice_question.search_functionality(QUESTION_MICQ, HINDI, BLANK)
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_044(self):
        self.log.getthelogs().info('TEST CASE, test_044')
        self.image_based_multiple_choice_question.search_functionality(QUESTION_MICQ, BLANK, BLANK)
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_045(self):
        self.log.getthelogs().info('TEST CASE, test_045')
        self.image_based_multiple_choice_question.search_functionality(BLANK, HINDI, BLANK)
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_046(self):
        self.log.getthelogs().info('TEST CASE, test_046')
        self.image_based_multiple_choice_question.search_functionality(BLANK, BLANK, BLANK)
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_047(self):
        self.log.getthelogs().info('TEST CASE, test_046')
        self.image_based_multiple_choice_question.search_functionality(WRONG_SEARCH, BLANK, VALIDATION)
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_048(self):
        self.log.getthelogs().info('TEST CASE, test_048')
        self.image_based_multiple_choice_question.search_functionality(BLANK, MATHS, VALIDATION)
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_049(self):
        self.log.getthelogs().info('TEST CASE, test_048')
        self.image_based_multiple_choice_question.search_functionality(WRONG_SEARCH, MATHS, VALIDATION)
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_050(self):
        self.log.getthelogs().info('TEST CASE, test_050')
        self.image_based_multiple_choice_question.delete_row_in_table(ACCEPT)
        
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_051(self):
        self.log.getthelogs().info('TEST CASE, test_051')
        self.image_based_multiple_choice_question.delete_row_in_table(BLANK)
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_052(self):
        self.log.getthelogs().info('TEST CASE, test_052')
        self.image_based_multiple_choice_question.edit_row_of_existing_table()
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_053(self):
        self.log.getthelogs().info('TEST CASE, test_053')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(EXCEL, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, OPTION_D, IMAGE, ADD, BLANK)
        
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_054(self):
        self.log.getthelogs().info('TEST CASE, test_054')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(TYPING_TEST, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, OPTION_D, IMAGE, ADD, BLANK)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_055(self):
        self.log.getthelogs().info('TEST CASE, test_055')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_dynamic_string(INVALID_LENGTH_STRING), OPTION_A, OPTION_B, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_056(self):
        self.log.getthelogs().info('TEST CASE, test_056')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), generate_random_dynamic_string(INVALID_LENGTH_STRING), OPTION_B, OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_057(self):
        self.log.getthelogs().info('TEST CASE, test_057')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), OPTION_A, generate_random_dynamic_string(INVALID_LENGTH_STRING), OPTION_C, OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_058(self):
        self.log.getthelogs().info('TEST CASE, test_058')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), OPTION_A, OPTION_B, generate_random_dynamic_string(INVALID_LENGTH_STRING), OPTION_D, IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_059(self):
        self.log.getthelogs().info('TEST CASE, test_059')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, generate_random_dynamic_string(INVALID_LENGTH_STRING), IMAGE, ADD, VALIDATION)
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_060(self):
        self.log.getthelogs().info('TEST CASE, test_060')
        self.image_based_multiple_choice_question.add_image_based_multiple_choice_question(HINDI, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, OPTION_D, OTHER_IMAGE, ADD, VALIDATION)
