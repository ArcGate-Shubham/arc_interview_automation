import time
import pytest
import allure

from Utilities.generate_email import *
from Utilities.return_message import *
from Utilities.constants import *

@pytest.mark.usefixtures("setup_and_teardown")
class TestAllowAuthenticatedUser:
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_001(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(generate_username_time_stamp(),generate_email_time_stamp(), ADMIN, STATUS)
        assert USER_ADDED in self.authenticated_user.display_message_on_top()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_002(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(NAME, EMAIL, ADMIN, STATUS)
        assert EMAIL_ALREADY in self.authenticated_user.display_message_on_top()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_003(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(NAME, ANOTHER_EMAIL, ADMIN, STATUS)
        assert USERNAME_ALREADY in self.authenticated_user.display_message_on_top()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_004(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(BLANK, ANOTHER_EMAIL, ADMIN , STATUS)
        self.authenticated_user.display_validation_message_yes_or_no()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_005(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(NAME, BLANK , ADMIN , STATUS)
        self.authenticated_user.display_validation_message_yes_or_no()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_006(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(NAME, ANOTHER_EMAIL, DASH_DATA, STATUS)
        self.authenticated_user.display_validation_message_yes_or_no()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_007(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(NAME, ANOTHER_EMAIL, ADMIN, DASH_DATA)
        self.authenticated_user.display_validation_message_yes_or_no()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_008(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(BLANK, BLANK, ADMIN, STATUS)
        self.authenticated_user.display_validation_message_yes_or_no()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_009(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(BLANK, ANOTHER_EMAIL, DASH_DATA, STATUS)
        self.authenticated_user.display_validation_message_yes_or_no()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_010(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(BLANK, ANOTHER_EMAIL, ADMIN, DASH_DATA)
        self.authenticated_user.display_validation_message_yes_or_no()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_011(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(NAME, BLANK, DASH_DATA, STATUS)
        self.authenticated_user.display_validation_message_yes_or_no()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_012(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(NAME, BLANK, ADMIN, DASH_DATA)
        self.authenticated_user.display_validation_message_yes_or_no()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_013(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(NAME, ANOTHER_EMAIL, DASH_DATA, DASH_DATA)
        self.authenticated_user.display_validation_message_yes_or_no()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_014(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(NAME, BLANK, DASH_DATA, DASH_DATA)
        self.authenticated_user.display_validation_message_yes_or_no()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_015(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(BLANK, ANOTHER_EMAIL, DASH_DATA, DASH_DATA)
        self.authenticated_user.display_validation_message_yes_or_no()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_016(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(BLANK, BLANK, ADMIN, DASH_DATA)
        self.authenticated_user.display_validation_message_yes_or_no()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_017(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(BLANK, BLANK, DASH_DATA, STATUS)
        self.authenticated_user.display_validation_message_yes_or_no()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_018(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(BLANK, BLANK, DASH_DATA, DASH_DATA)
        self.authenticated_user.display_validation_message_yes_or_no()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_019(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(NAME, ANOTHER_EMAIL, ADMIN, STATUS)
        self.authenticated_user.display_arcgate_email_validation_message(NOT_MODAL)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_020(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(NAME, ANOTHER_EMAIL, ADMIN, STATUS)
        self.authenticated_user.display_arcgate_email_validation_message(NOT_MODAL)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_021(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(NAME, YAHOO_EMAIL, ADMIN, STATUS)
        self.authenticated_user.display_arcgate_email_validation_message(BLANK)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_022(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(NAME, ANOTHER_EMAIL, ADMIN, STATUS)
        self.authenticated_user.display_arcgate_email_validation_message(NOT_MODAL)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_023(self):  
        self.authenticated_user.fill_the_form_allow_authenticated_user(NAME, DOT_IN_EMAIL, ADMIN, STATUS)
        self.authenticated_user.display_arcgate_email_validation_message(BLANK)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_024(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(BLANK, GMAIL_EMAIL, ADMIN, STATUS)
        self.authenticated_user.display_arcgate_email_validation_message(BLANK)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_025(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(NAME,GMAIL_EMAIL, DASH_DATA, STATUS)
        self.authenticated_user.display_arcgate_email_validation_message(BLANK)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_026(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(NAME, GMAIL_EMAIL, ADMIN, DASH_DATA)
        self.authenticated_user.display_arcgate_email_validation_message(BLANK)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_027(self): 
        self.authenticated_user.fill_the_form_allow_authenticated_user(BLANK, GMAIL_EMAIL, DASH_DATA, STATUS)
        self.authenticated_user.display_arcgate_email_validation_message(BLANK)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_028(self): 
        self.authenticated_user.fill_the_form_allow_authenticated_user(BLANK, GMAIL_EMAIL, ADMIN, DASH_DATA)
        self.authenticated_user.display_arcgate_email_validation_message(BLANK)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_029(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(NAME, GMAIL_EMAIL , DASH_DATA, DASH_DATA)
        self.authenticated_user.display_arcgate_email_validation_message(BLANK)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_030(self):
        self.authenticated_user.fill_the_form_allow_authenticated_user(BLANK, GMAIL_EMAIL, DASH_DATA, DASH_DATA)
        self.authenticated_user.display_arcgate_email_validation_message(BLANK)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_031(self):
        self.authenticated_user.search_functionality(NAME, BLANK, BLANK)
        assert NAME in self.authenticated_user.display_username_in_table_in_td_tag()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_032(self):
        self.authenticated_user.search_functionality(ANOTHER_NAME, BLANK, BLANK)
        assert NO_DATA in self.authenticated_user.display_no_data_found_validation_in_message()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_033(self):
        self.authenticated_user.search_functionality(BLANK, EMAIL, BLANK)
        assert EMAIL in self.authenticated_user.display_email_in_table()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_034(self):
        self.authenticated_user.search_functionality(BLANK, NEW_EMAIL, BLANK)
        assert NO_DATA in self.authenticated_user.display_no_data_found_validation_in_message()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke    
    def test_035(self):
        self.authenticated_user.search_functionality(BLANK, BLANK, ADMIN)
        assert ADMIN in self.authenticated_user.display_role_for_admin_role_in_table()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_036(self):
        self.authenticated_user.search_functionality(BLANK, BLANK, ROLE)
        assert NO_DATA in self.authenticated_user.display_no_data_found_validation_in_message()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_037(self):
        self.authenticated_user.search_functionality(NAME, EMAIL, BLANK)
        assert NAME in self.authenticated_user.display_username_in_table_in_td_tag() and EMAIL in self.authenticated_user.display_email_in_table()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_038(self):
        self.authenticated_user.search_functionality(NAME, EMAIL, BLANK)
        assert NAME in self.authenticated_user.display_username_in_table_in_td_tag() and EMAIL in self.authenticated_user.display_email_in_table()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_039(self):
        self.authenticated_user.search_functionality(NAME, BLANK, ADMIN)
        assert NAME in self.authenticated_user.display_username_in_table_in_td_tag() and ADMIN in self.authenticated_user.display_role_for_admin_role_in_table()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_040(self):
        self.authenticated_user.search_functionality_from_diffrent_types(NAME, NEW_EMAIL, BLANK)
        assert NO_DATA in self.authenticated_user.display_no_data_found_validation_in_message()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_041(self):
        self.authenticated_user.search_functionality_from_diffrent_types(NAME, BLANK, ANOTHER_ROLE)
        assert NO_DATA in self.authenticated_user.display_no_data_found_validation_in_message()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_042(self):
        self.authenticated_user.search_functionality_from_diffrent_types(BLANK, EMAIL, ANOTHER_ROLE)
        assert NO_DATA in self.authenticated_user.display_no_data_found_validation_in_message()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_043(self):
        self.authenticated_user.search_functionality_from_diffrent_types(ANOTHER_NAME, BLANK, ANOTHER_ROLE)
        assert NO_DATA in self.authenticated_user.display_no_data_found_validation_in_message()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_044(self):
        self.authenticated_user.search_functionality_from_diffrent_types(NAME, EMAIL, ADMIN)
        assert NAME in self.authenticated_user.display_username_in_table_in_td_tag() and ADMIN in self.authenticated_user.display_role_for_admin_role_in_table() and EMAIL in self.authenticated_user.display_email_in_table()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_045(self):
        self.authenticated_user.search_functionality_from_diffrent_types(ANOTHER_NAME, NEW_EMAIL, ANOTHER_ROLE)
        assert NO_DATA in self.authenticated_user.display_no_data_found_validation_in_message()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_046(self):
        self.authenticated_user.delete_any_row_of_authenticated_user_in_table_data()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_047(self):
        self.authenticated_user.not_delete_any_row_of_authenticated_user_in_table_data_using_cancel_button()
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke    
    def test_048(self):
        self.authenticated_user.click_on_edit_button_and_without_changes_click_on_cancel_button()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke    
    def test_049(self):
        self.authenticated_user.click_on_edit_button_and_update_all_input_type()
        self.authenticated_user.username().clear()
        self.authenticated_user.click_on_authenticated_user_save_button()
        self.authenticated_user.display_validation_message_yes_or_no()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke    
    def test_050(self):
        self.authenticated_user.click_on_edit_button_and_update_all_input_type()
        self.authenticated_user.email().clear()
        self.authenticated_user.click_on_authenticated_user_save_button()
        self.authenticated_user.display_validation_message_yes_or_no()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_051(self):
        self.authenticated_user.click_on_edit_button_and_update_all_input_type()
        self.authenticated_user.role()
        self.authenticated_user.click_on_authenticated_user_save_button()
        self.authenticated_user.display_validation_message_yes_or_no()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_052(self):
        self.authenticated_user.click_on_edit_button_and_update_all_input_type()
        self.authenticated_user.status()
        self.authenticated_user.click_on_authenticated_user_save_button()
        self.authenticated_user.display_validation_message_yes_or_no()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke    
    def test_053(self):
        self.authenticated_user.click_on_edit_button_and_update_all_input_type()
        self.authenticated_user.username().clear()
        self.authenticated_user.email().clear()
        time.sleep(3)
        self.authenticated_user.click_on_authenticated_user_save_button()
        self.authenticated_user.display_validation_message_yes_or_no()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_054(self):
        self.authenticated_user.click_on_edit_button_and_update_all_input_type()
        self.authenticated_user.username().clear()
        self.authenticated_user.role()
        self.authenticated_user.click_on_authenticated_user_save_button()
        self.authenticated_user.display_validation_message_yes_or_no()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_055(self):
        self.authenticated_user.click_on_edit_button_and_update_all_input_type()
        self.authenticated_user.username().clear()
        self.authenticated_user.status()
        self.authenticated_user.click_on_authenticated_user_save_button()
        self.authenticated_user.display_validation_message_yes_or_no()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_056(self):
        self.authenticated_user.click_on_edit_button_and_update_all_input_type()
        self.authenticated_user.email().clear()
        self.authenticated_user.role()
        self.authenticated_user.click_on_authenticated_user_save_button()
        self.authenticated_user.display_validation_message_yes_or_no()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_057(self):
        self.authenticated_user.click_on_edit_button_and_update_all_input_type()
        self.authenticated_user.email().clear()
        self.authenticated_user.status()
        self.authenticated_user.click_on_authenticated_user_save_button()
        self.authenticated_user.display_validation_message_yes_or_no()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_058(self):
        self.authenticated_user.click_on_edit_button_and_update_all_input_type()
        self.authenticated_user.role()
        self.authenticated_user.status()
        self.authenticated_user.click_on_authenticated_user_save_button()
        self.authenticated_user.display_validation_message_yes_or_no()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_059(self):
        self.authenticated_user.click_on_edit_button_and_update_all_input_type()
        self.authenticated_user.username().clear()
        self.authenticated_user.email().clear()
        self.authenticated_user.role()
        self.authenticated_user.click_on_authenticated_user_save_button()
        self.authenticated_user.display_validation_message_yes_or_no()
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_060(self):
        self.authenticated_user.click_on_edit_button_and_update_all_input_type()
        self.authenticated_user.username().clear()
        self.authenticated_user.email().clear()
        self.authenticated_user.status()
        self.authenticated_user.click_on_authenticated_user_save_button()
        self.authenticated_user.display_validation_message_yes_or_no()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_061(self):
        self.authenticated_user.click_on_edit_button_and_update_all_input_type()
        self.authenticated_user.username().clear()
        self.authenticated_user.role()
        self.authenticated_user.status()
        self.authenticated_user.click_on_authenticated_user_save_button()
        self.authenticated_user.display_validation_message_yes_or_no()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_062(self):
        self.authenticated_user.click_on_edit_button_and_update_all_input_type()
        self.authenticated_user.email().clear()
        self.authenticated_user.role()
        self.authenticated_user.status()
        self.authenticated_user.click_on_authenticated_user_save_button()
        self.authenticated_user.display_validation_message_yes_or_no()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_063(self):
        self.authenticated_user.click_on_edit_button_and_update_all_input_type()
        self.authenticated_user.username().clear()
        self.authenticated_user.email().clear()
        self.authenticated_user.role()
        self.authenticated_user.status()
        self.authenticated_user.click_on_authenticated_user_save_button()
        self.authenticated_user.display_validation_message_yes_or_no()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke    
    def test_064(self):
        self.authenticated_user.click_on_edit_button_then_click_on_save_button()
