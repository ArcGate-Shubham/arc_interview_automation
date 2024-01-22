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
       
    @allure.severity(allure.severity_level.NORMAL)
    def test_031(self):
        self.log.getthelogs().info('TEST CASE, test_031')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), BLANK, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_031.png')
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_032(self):
        self.log.getthelogs().info('TEST CASE, test_032')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, BLANK, OPTION_A, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_032.png')

    @allure.severity(allure.severity_level.NORMAL)
    def test_033(self):
        self.log.getthelogs().info('TEST CASE, test_033')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, BLANK, BLANK, OPTION_B, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_033.png')
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_034(self):
        self.log.getthelogs().info('TEST CASE, test_034')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, BLANK, BLANK, BLANK, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_034.png')
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_035(self):
        self.log.getthelogs().info('TEST CASE, test_035')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, BLANK, BLANK, BLANK, BLANK, OPTION_D, ADD, VALIDATION, 'Screenshots/test_035.png')
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_036(self):
        self.log.getthelogs().info('TEST CASE, test_036')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, generate_random_string_subject(), OPTION_A, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_036.png')
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_037(self):
        self.log.getthelogs().info('TEST CASE, test_037')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, generate_random_string_subject(), BLANK, OPTION_B, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_037.png')
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_038(self):
        self.log.getthelogs().info('TEST CASE, test_038')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, generate_random_string_subject(), BLANK, BLANK, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_038.png')
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_039(self):
        self.log.getthelogs().info('TEST CASE, test_039')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, generate_random_string_subject(), BLANK, BLANK, BLANK, OPTION_D, ADD, VALIDATION, 'Screenshots/test_039.png')
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_040(self):
        self.log.getthelogs().info('TEST CASE, test_040')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, OPTION_A, OPTION_B, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_040.png')
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_041(self):
        self.log.getthelogs().info('TEST CASE, test_041')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, OPTION_A, BLANK, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_041.png')
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_042(self):
        self.log.getthelogs().info('TEST CASE, test_042')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, OPTION_A, BLANK, BLANK, OPTION_D, ADD, VALIDATION, 'Screenshots/test_042.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_043(self):
        self.log.getthelogs().info('TEST CASE, test_043')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, BLANK, OPTION_B, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_043.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_044(self):
        self.log.getthelogs().info('TEST CASE, test_044')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, BLANK, OPTION_B, BLANK, OPTION_D, ADD, VALIDATION, 'Screenshots/test_044.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_045(self):
        self.log.getthelogs().info('TEST CASE, test_045')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, BLANK, BLANK, BLANK, BLANK, OPTION_C, OPTION_D, ADD, VALIDATION, 'Screenshots/test_045.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_046(self):
        self.log.getthelogs().info('TEST CASE, test_046')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_046.png')
        
    @allure.severity(allure.severity_level.MINOR)
    def test_047(self):
        self.log.getthelogs().info('TEST CASE, test_047')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, generate_random_string_subject(), BLANK, OPTION_B, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_047.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_048(self):
        self.log.getthelogs().info('TEST CASE, test_048')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, generate_random_string_subject(), BLANK, BLANK, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_048.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_049(self):
        self.log.getthelogs().info('TEST CASE, test_049')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, generate_random_string_subject(), BLANK, BLANK, BLANK, OPTION_D, ADD, VALIDATION, 'Screenshots/test_049.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_050(self):
        self.log.getthelogs().info('TEST CASE, test_050')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, BLANK, OPTION_A, OPTION_B, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_050.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_051(self):
        self.log.getthelogs().info('TEST CASE, test_051')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, BLANK, BLANK, OPTION_B, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_051.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_052(self):
        self.log.getthelogs().info('TEST CASE, test_052')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, PASSAGE_VALUE, BLANK, BLANK, BLANK, OPTION_C, OPTION_D, ADD, VALIDATION, 'Screenshots/test_052.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_053(self):
        self.log.getthelogs().info('TEST CASE, test_053')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, generate_random_string_subject(), OPTION_A, OPTION_B, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_053.png')
        
    @allure.severity(allure.severity_level.MINOR)
    def test_054(self):
        self.log.getthelogs().info('TEST CASE, test_054')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, generate_random_string_subject(), BLANK, OPTION_B, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_054.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_055(self):
        self.log.getthelogs().info('TEST CASE, test_055')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, generate_random_string_subject(), BLANK, BLANK, OPTION_C, OPTION_D, ADD, VALIDATION, 'Screenshots/test_055.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_056(self):
        self.log.getthelogs().info('TEST CASE, test_056')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, OPTION_A, OPTION_B, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_056.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_057(self):
        self.log.getthelogs().info('TEST CASE, test_057')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, OPTION_A, BLANK, OPTION_C, OPTION_D, ADD, VALIDATION, 'Screenshots/test_057.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_058(self):
        self.log.getthelogs().info('TEST CASE, test_058')
        self.multiple_choice_question.add_question_multiple_choice_question(DASH_DATA, BLANK, BLANK, BLANK, OPTION_B, OPTION_C, OPTION_D, ADD, VALIDATION, 'Screenshots/test_058.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_059(self):
        self.log.getthelogs().info('TEST CASE, test_059')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, BLANK, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_059.png')
        
    @allure.severity(allure.severity_level.MINOR)
    def test_060(self):
        self.log.getthelogs().info('TEST CASE, test_060')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), BLANK, OPTION_B, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_060.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_061(self):
        self.log.getthelogs().info('TEST CASE, test_061')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), BLANK, BLANK, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_061.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_062(self):
        self.log.getthelogs().info('TEST CASE, test_062')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), BLANK, BLANK, BLANK, OPTION_D, ADD, VALIDATION, 'Screenshots/test_062.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_063(self):
        self.log.getthelogs().info('TEST CASE, test_063')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, BLANK, OPTION_A, OPTION_B, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_063.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_064(self):
        self.log.getthelogs().info('TEST CASE, test_064')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, BLANK, BLANK, OPTION_B, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_064.png')
        
    @allure.severity(allure.severity_level.MINOR)
    def test_065(self):
        self.log.getthelogs().info('TEST CASE, test_065')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, BLANK, BLANK, OPTION_B, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_065.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_066(self):
        self.log.getthelogs().info('TEST CASE, test_066')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, BLANK, BLANK, BLANK, OPTION_C, OPTION_D, ADD, VALIDATION, 'Screenshots/test_066.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_067(self):
        self.log.getthelogs().info('TEST CASE, test_067')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, OPTION_B, BLANK, BLANK, ADD, VALIDATION, 'Screenshots/test_067.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_068(self):
        self.log.getthelogs().info('TEST CASE, test_068')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, BLANK, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_068.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_069(self):
        self.log.getthelogs().info('TEST CASE, test_069')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, BLANK, BLANK, OPTION_D, ADD, VALIDATION, 'Screenshots/test_069.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_070(self):
        self.log.getthelogs().info('TEST CASE, test_070')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), BLANK, OPTION_B, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_070.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_071(self):
        self.log.getthelogs().info('TEST CASE, test_071')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), BLANK, BLANK, OPTION_C, OPTION_D, ADD, VALIDATION, 'Screenshots/test_071.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_072(self):
        self.log.getthelogs().info('TEST CASE, test_072')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, OPTION_B, OPTION_C, BLANK, ADD, VALIDATION, 'Screenshots/test_072.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_073(self):
        self.log.getthelogs().info('TEST CASE, test_073')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE, generate_random_string_subject(), OPTION_A, OPTION_B, BLANK, OPTION_D, ADD, VALIDATION, 'Screenshots/test_073.png')
        
    @allure.severity(allure.severity_level.MINOR)
    def test_074(self):
        self.log.getthelogs().info('TEST CASE, test_074')
        self.multiple_choice_question.add_question_multiple_choice_question_with_maxlength_validation(HINDI, PASSAGE_VALUE, generate_random_dynamic_string(INVALID_LENGTH_STRING), OPTION_A, OPTION_B, OPTION_C, OPTION_D, ADD, VALIDATION, 'Screenshots/test_074.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_075(self):
        self.log.getthelogs().info('TEST CASE, test_075')
        self.multiple_choice_question.add_question_multiple_choice_question_with_maxlength_validation(HINDI, PASSAGE_VALUE, generate_random_string_subject(), generate_random_dynamic_string(INVALID_LENGTH_STRING), OPTION_B, OPTION_C, OPTION_D, ADD, VALIDATION, 'Screenshots/test_075.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_076(self):
        self.log.getthelogs().info('TEST CASE, test_076')
        self.multiple_choice_question.add_question_multiple_choice_question_with_maxlength_validation(HINDI, PASSAGE_VALUE, HINDI, OPTION_A, generate_random_dynamic_string(INVALID_LENGTH_STRING), OPTION_C, OPTION_D, ADD, VALIDATION, 'Screenshots/test_076.png')
        
    @allure.severity(allure.severity_level.MINOR)
    def test_077(self):
        self.log.getthelogs().info('TEST CASE, test_077')
        self.multiple_choice_question.add_question_multiple_choice_question_with_maxlength_validation(HINDI, PASSAGE_VALUE, HINDI, OPTION_A, OPTION_B, generate_random_dynamic_string(INVALID_LENGTH_STRING), OPTION_D, ADD, VALIDATION, 'Screenshots/test_077.png')
        
    @allure.severity(allure.severity_level.MINOR)
    def test_078(self):
        self.log.getthelogs().info('TEST CASE, test_078')
        self.multiple_choice_question.add_question_multiple_choice_question_with_maxlength_validation(HINDI, PASSAGE_VALUE, HINDI, OPTION_A, OPTION_B, OPTION_C, generate_random_dynamic_string(INVALID_LENGTH_STRING), ADD, VALIDATION, 'Screenshots/test_078.png')

    @allure.severity(allure.severity_level.MINOR)
    def test_079(self):
        self.log.getthelogs().info('TEST CASE, test_079')
        self.multiple_choice_question.delete_row_in_existing_table(ACCEPT, 'Screenshots/test_079.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_080(self):
        self.log.getthelogs().info('TEST CASE, test_080')
        self.multiple_choice_question.delete_row_in_existing_table(BLANK, 'Screenshots/test_080.png')
    
    @allure.severity(allure.severity_level.MINOR)
    def test_081(self):
        self.log.getthelogs().info('TEST CASE, test_081')
        self.multiple_choice_question.search_functionality(QUESTION_MCQ, BLANK)
        self.multiple_choice_question.row_count_table('Screenshots/test_081.png')
        
    @allure.severity(allure.severity_level.MINOR)
    def test_082(self):
        self.log.getthelogs().info('TEST CASE, test_082')
        self.multiple_choice_question.search_functionality(BLANK, HINDI)
        self.multiple_choice_question.row_count_table('Screenshots/test_082.png')
        
    @allure.severity(allure.severity_level.MINOR)
    def test_083(self):
        self.log.getthelogs().info('TEST CASE, test_083')
        self.multiple_choice_question.search_functionality(QUESTION_MCQ, HINDI)
        self.multiple_choice_question.row_count_table('Screenshots/test_083.png')
        
    @allure.severity(allure.severity_level.MINOR)
    def test_084(self):
        self.log.getthelogs().info('TEST CASE, test_084')
        self.multiple_choice_question.search_functionality(QUESTION_MCQD, HINDI)
        self.multiple_choice_question.no_data_found_validation('Screenshots/test_084.png')

    @allure.severity(allure.severity_level.MINOR)
    def test_085(self):
        self.log.getthelogs().info('TEST CASE, test_085')
        self.multiple_choice_question.search_functionality(QUESTION_MCQ, MATHS)
        self.multiple_choice_question.no_data_found_validation('Screenshots/test_085.png')
        
    @allure.severity(allure.severity_level.MINOR)
    def test_086(self):
        self.log.getthelogs().info('TEST CASE, test_086')
        self.multiple_choice_question.search_functionality(QUESTION_MCQD, MATHS)
        self.multiple_choice_question.no_data_found_validation('Screenshots/test_086.png')
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_087(self):
        self.log.getthelogs().info('TEST CASE, test_087')
        self.multiple_choice_question.edit_row_of_existing_table('Screenshots/test_087.png')
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_088(self):
        self.log.getthelogs().info('TEST CASE, test_088')
        self.multiple_choice_question.same_question_gives_on_presence_on_table(HINDI, PASSAGE_VALUE, OHMOBGT, OPTION_A, OPTION_B, OPTION_C, OPTION_D, 'Screenshots/test_088.png')
