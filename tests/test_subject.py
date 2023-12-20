import pytest

from Utilities.generate_email import generate_random_string_subject

@pytest.mark.usefixtures("setup_and_teardown")
class TestSubject:
    def test_add_new_subject_with_valid_data(self):
        self.log.getthelogs().info('TEST CASE, test_add_new_subject_with_valid_data')
        self.subject.fill_the_form_add_new_subject(generate_random_string_subject())
        self.subject.success_message_for_subject('Subject added successfully', 'Screenshots/test_add_new_subject_with_valid_data.png')
    
    def test_add_new_subject_without_data(self):
        self.log.getthelogs().info('TEST CASE, test_add_new_subject_without_data')
        self.subject.fill_the_form_add_new_subject('')
        self.subject.validation_message_for_required_subject('Screenshots/test_add_new_subject_without_data.png')
            
    def test_add_new_subject_with_numeric_data(self):
        self.log.getthelogs().info('TEST CASE, test_add_new_subject_with_numeric_data')
        self.subject.fill_the_form_add_new_subject('1234')
        self.subject.validation_message_for_subject('Screenshots/test_add_new_subject_with_numeric_data.png')

    def test_add_new_subject_with_special_character_data(self):
        self.log.getthelogs().info('TEST CASE, test_add_new_subject_with_special_character_data')
        self.subject.fill_the_form_add_new_subject('####')
        self.subject.validation_message_for_subject('Screenshots/test_add_new_subject_with_special_character_data.png')
    
    def test_add_new_subject_with_numeric_data_along_with_string(self):
        self.log.getthelogs().info('TEST CASE, test_add_new_subject_with_numeric_data_along_with_string')
        self.subject.fill_the_form_add_new_subject('shubha111')
        self.subject.validation_message_for_subject('Screenshots/test_add_new_subject_with_numeric_data_along_with_string.png')
    
    def test_add_new_subject_with_alterat_along_with_string(self):
        self.log.getthelogs().info('TEST CASE, test_add_new_subject_with_alterat_along_with_string')
        self.subject.fill_the_form_add_new_subject('shubha@@@@')
        self.subject.validation_message_for_subject('Screenshots/test_add_new_subject_with_alterat_along_with_string.png')
            
    def test_add_new_subject_with_special_character_along_with_string(self):
        self.log.getthelogs().info('TEST CASE, test_add_new_subject_with_special_character_along_with_string')
        self.subject.fill_the_form_add_new_subject('shubha!!!!')
        self.subject.success_message_for_subject('Subject added successfully', 'Screenshots/test_add_new_subject_with_special_character_along_with_string.png')
            
    def test_add_new_subject_with_add_new_subject_and_click_on_cancel_button(self):
        self.log.getthelogs().info('TEST CASE, test_add_new_subject_with_add_new_subject_and_click_on_cancel_button')
        self.subject.not_save_new_subject_click_on_cancel_button()
        
    def test_successfully_deleted_row_in_the_subject_table(self):
        self.log.getthelogs().info('TEST CASE, test_successfully_deleted_row_in_the_subject_table')
        self.subject.delete_row_in_the_subject_table()
        
    def test_not_deleted_row_from_subject_table(self):
        self.log.getthelogs().info('TEST CASE, test_not_deleted_row_from_subject_table')
        self.subject.not_delete_row_in_subject_table('Screenshots/test_not_deleted_row_from_subject_table.png')

    def test_existing_data_update_using_edit_button(self):
        self.log.getthelogs().info('TEST CASE, test_existing_data_update_using_edit_button')
        self.subject.update_existing_data_in_the_subject_table_without_change('Screenshots/test_existing_data_update_using_edit_button.png')
        
    def test_click_edit_button_and_then_subject_clear_and_click_save_button(self):
        self.log.getthelogs().info('TEST CASE, test_click_edit_button_and_then_subject_clear_and_click_save_button')
        self.subject.update_existing_subject_click_on_edit_button('')
        self.subject.validation_message_for_required_subject('Screenshots/test_click_edit_button_and_then_subject_clear_and_click_save_button.png')
    
    def test_click_edit_button_and_then_subject_clear_and_change_subject_then_click_save_button(self):
        self.log.getthelogs().info('TEST CASE, test_click_edit_button_and_then_subject_clear_and_change_subject_then_click_save_button')
        self.subject.update_existing_subject_click_on_edit_button(generate_random_string_subject())
        self.subject.success_message_for_subject('Subject updated successfully', 'Screenshots/test_click_edit_button_and_then_subject_clear_and_change_subject_then_click_save_button.png')
            
    def test_click_edit_button_and_then_subject_clear_and_change_subject_data_with_number_then_click_save_button(self):
        self.log.getthelogs().info('TEST CASE, test_click_edit_button_and_then_subject_clear_and_change_subject_data_with_number_then_click_save_button')
        self.subject.update_existing_subject_click_on_edit_button('asdfghj1')
        self.subject.validation_message_for_subject('Screenshots/test_click_edit_button_and_then_subject_clear_and_change_subject_data_with_number_then_click_save_button.png')

    def test_click_edit_button_and_then_subject_clear_and_change_subject_data_with_special_character_then_click_save_button(self):
        self.log.getthelogs().info('TEST CASE, test_click_edit_button_and_then_subject_clear_and_change_subject_data_with_special_character_then_click_save_button')
        self.subject.update_existing_subject_click_on_edit_button('asdfghj@')
        self.subject.validation_message_for_subject('Screenshots/test_click_edit_button_and_then_subject_clear_and_change_subject_data_with_special_character_then_click_save_button.png')
