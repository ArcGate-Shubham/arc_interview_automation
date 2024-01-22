import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from PageObjects.LoginPage import Login
from Utilities.logger import logclass
from Utilities.return_message import *
from Utilities.Readconfigurations import *

class MultipleImageChoiceQuestion(logclass):
    def __init__(self, driver):
        self.driver = driver
        self.add_new_question_button_xpath = 'addButton'
        self.row_count_of_table_xpath = 'tbody#demo tr'
        self.close_button_xpath = 'close-dialoge'
        self.question_title_xpath = 'MICQ_title'
        self.subject_choosen_xpath = '//select[@id="MICQ_subject"]/option[5]'
        self.image_optionA_image_xpath = 'MICQ_optionA'
        self.image_optionB_image_xpath = 'MICQ_optionB'
        self.image_optionC_image_xpath = 'MICQ_optionC'
        self.image_optionD_image_xpath = 'MICQ_optionD'
        self.add_question_button_xpath = 'add_question_btn'
        self.right_question_answer_xpath = 'chkboxOption1'
        self.display_sucess_message_xpath = 'notice'
        self.parsley_required_validation_xpath = 'parsley-required'
        self.display_modal_xpath = 'modal-content'
        self.search_by_question_title_xpath = 'id_question_title'
        self.search_by_subject_xpath = 'id_subject'
        self.click_on_search_button_xpath = '//input[@value="Search"]'
        self.click_on_delete_button_xpath = 'Delete'
        self.click_on_edit_button_xpath = 'a.Edit'
        self.get_text_of_question_name_xpath = '//*[@id="demo"]/tr[1]/td[1]'
        self.click_on_edit_button_and_also_select_subject_dropdown_xpath = '//select[@id="MICQ_subject"]/option[1]'
        self.updated_subject_input_xpath = '//select[@id="MICQ_subject"]/option[6]'
        
    def click_on_add_new_question_button(self):
        time.sleep(1)
        self.driver.find_element(By.ID, self.add_new_question_button_xpath).click()
        
    def row_count_of_existing_table(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.row_count_of_table_xpath)
    
    def click_on_close_button(self):
        time.sleep(1)
        self.driver.find_element(By.ID, self.close_button_xpath).click()
        
    def input_question_title(self, question_title):
        time.sleep(1)
        return self.driver.find_element(By.ID, self.question_title_xpath).send_keys(question_title)
    
    def input_optionA(self,optionA):
        time.sleep(1)
        return self.driver.find_element(By.ID, self.image_optionA_image_xpath).send_keys(optionA)
    
    def input_optionB(self,optionB):
        time.sleep(2)
        return self.driver.find_element(By.ID, self.image_optionB_image_xpath).send_keys(optionB)
    
    def input_optionC(self, optionC):
        time.sleep(2)
        return self.driver.find_element(By.ID, self.image_optionC_image_xpath).send_keys(optionC)
    
    def input_optionD(self, optionD):
        time.sleep(2)
        return self.driver.find_element(By.ID, self.image_optionD_image_xpath).send_keys(optionD)
    
    def add_question_button(self):
        time.sleep(2)
        self.driver.find_element(By.ID, self.add_question_button_xpath).click()
        
    def checked_right_answer_options(self):
        time.sleep(1)
        self.driver.find_element(By.ID, self.right_question_answer_xpath).click()
        
    def display_success_message(self):
        time.sleep(1)
        return self.driver.find_element(By.ID, self.display_sucess_message_xpath).text
    
    def display_validation_message(self):
        time.sleep(1)
        return self.driver.find_element(By.CLASS_NAME, self.parsley_required_validation_xpath).text
    
    def search_by_question_title(self):
        return self.driver.find_element(By.ID, self.search_by_question_title_xpath)
    
    def search_by_subject(self):
        return self.driver.find_element(By.ID, self.search_by_subject_xpath)
    
    def click_on_search_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.click_on_search_button_xpath).click()
        
    def click_on_delete_button(self):
        time.sleep(2)
        self.driver.find_element(By.ID, self.click_on_delete_button_xpath).click()
        
    def click_on_edit_button(self):
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,self.click_on_edit_button_xpath).click()
        
    def get_text_of_questions(self):
        time.sleep(2)
        return self.driver.find_element(By.XPATH, self.get_text_of_question_name_xpath).text

    def section_open_of_multiple_image_choice_question_section(self):
        login = Login(self.driver)
        login.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        login.click_on_multiple_image_choice_question_section()
        
    def add_new_question_multiple_image_choice_question(self):
        self.section_open_of_multiple_image_choice_question_section()
        old_row = 0
        for old_row_data in self.row_count_of_existing_table():
            old_row = old_row + 1
        self.click_on_add_new_question_button()
        self.click_on_close_button()
        new_row = 0
        for new_row_data in self.row_count_of_existing_table():
            new_row = new_row + 1
        if old_row == new_row:
            assert True
        else:
            assert False
            
    def add_new_question_with_all_valid_input(self,question_title, optionA, optionB, optionC, optionD, add_question):
        self.section_open_of_multiple_image_choice_question_section()
        self.click_on_add_new_question_button()
        self.input_question_title(question_title)
        self.driver.find_element(By.XPATH, self.subject_choosen_xpath).click()
        if optionA: 
            self.input_optionA(optionA)
        if optionB:
            self.input_optionB(optionB)
        if optionC:
            self.input_optionC(optionC)
        if optionD:
            self.input_optionD(optionD)
        if optionA and optionC:
            self.input_optionA(optionA)
            self.input_optionC(optionC)
        if optionA and optionB:
            self.input_optionA(optionA)
            self.input_optionB(optionB)
        if optionA and optionD:
            self.input_optionA(optionA)
            self.input_optionD(optionD)
        if optionA and optionB and optionC:
            self.input_optionA(optionA)
            self.input_optionB(optionB)
            self.input_optionC(optionC)
        if optionA and optionB and optionC and optionD:
            self.input_optionA(optionA)
            self.input_optionB(optionB)
            self.input_optionC(optionC)
            self.input_optionD(optionD)
        self.checked_right_answer_options()
        if add_question:
            self.add_question_button()
        else:
            self.click_on_close_button()
        time.sleep(1)
        
    def display_validation_messsage_required(self, screenshot):
        if 'This field is required' in self.display_validation_message():
            assert True
        else:
            self.driver.save_screenshot(screenshot)
            assert False
            
    def display_success_message_for_multiple_image_choice_question(self, message, screenshot):
        if message in self.display_success_message():
            assert True
        else:
            self.driver.save_screenshot(screenshot)
            assert False

    def search_functionality_for_multiple_image_choice_question(self, question_title, subject):
        self.section_open_of_multiple_image_choice_question_section()
        if question_title:
            self.search_by_question_title().send_keys(question_title)
        if subject:
            wait = WebDriverWait(self.driver, 10)
            select = wait.until(EC.presence_of_element_located((By.ID, self.search_by_subject_xpath)))
            select = Select(select)
            subject = select.select_by_visible_text(subject)
        self.click_on_search_button()
        time.sleep(2)
        return subject
    
    def search_after_row_count(self, screenshot):
        if self.row_count_of_existing_table():
            assert True
        else:
            self.driver.save_screenshot(screenshot)
            assert False
            
    def delete_row_in_existing_table(self, accept, screenshot):
        self.section_open_of_multiple_image_choice_question_section()
        old_row = 0
        for old_row_data in self.row_count_of_existing_table():
            old_row = old_row + 1
        self.click_on_delete_button()
        if accept:
            self.driver.switch_to.alert.accept()
            if 'Question deleted successfully' in self.display_success_message():
                assert True
            else:
                self.driver.save_screenshot(screenshot)
                assert False
        else:
            self.driver.switch_to.alert.dismiss()
            new_row = 0
            for new_row_data in self.row_count_of_existing_table():
                new_row = new_row + 1
            if old_row == new_row:
                assert True
            else:
                self.driver.save_screenshot(screenshot)
                assert False
                
    def edit_row_in_existing_table(self, close, clear,clear_subject, screenshot):
        self.section_open_of_multiple_image_choice_question_section()
        previous_question = self.get_text_of_questions()
        self.click_on_edit_button()
        if close:
            self.click_on_close_button()
            new_question = self.get_text_of_questions()
            if previous_question == new_question:
                assert True
            else:
                self.driver.save_screenshot(screenshot)
                assert False
        else:
            if clear and clear_subject:
                time.sleep(5)
                self.driver.find_element(By.ID, self.question_title_xpath).clear()
                self.driver.find_element(By.XPATH, self.click_on_edit_button_and_also_select_subject_dropdown_xpath).click()
                self.add_question_button()
                time.sleep(2)
                if PARSLEY_REQUIRED in self.display_validation_message():
                    assert True
                else:
                    self.driver.save_screenshot(screenshot)
                    assert False
            elif clear:
                time.sleep(5)
                self.driver.find_element(By.ID, self.question_title_xpath).clear()
                self.add_question_button()
                time.sleep(2)
                if PARSLEY_REQUIRED in self.display_validation_message():
                    assert True
                else:
                    self.driver.save_screenshot(screenshot)
                    assert False
            elif clear_subject:
                time.sleep(5)
                self.driver.find_element(By.XPATH, self.click_on_edit_button_and_also_select_subject_dropdown_xpath).click()
                self.add_question_button()
                time.sleep(2)
                if PARSLEY_REQUIRED in self.display_validation_message():
                    assert True
                else:
                    self.driver.save_screenshot(screenshot)
                    assert False
            else:
                self.add_question_button()
                if QUESTION_UPDATE in self.display_success_message():
                    assert True
                else:
                    self.driver.save_screenshot(screenshot)
                    assert False
                    
    def edit_question_of_existing_table_using_change_question(self, question_title, subject, screenshot):
        self.section_open_of_multiple_image_choice_question_section()
        self.click_on_edit_button()
        time.sleep(2)
        if question_title and subject:
            self.driver.find_element(By.ID, self.question_title_xpath).clear()
            self.driver.find_element(By.ID, self.question_title_xpath).send_keys(question_title)
            self.driver.find_element(By.XPATH, self.updated_subject_input_xpath).click()
        elif question_title:
            self.driver.find_element(By.ID, self.question_title_xpath).clear()
            self.driver.find_element(By.ID, self.question_title_xpath).send_keys(question_title)
        elif subject:
            self.driver.find_element(By.XPATH, self.updated_subject_input_xpath).click()
        self.add_question_button()
        if QUESTION_UPDATE in self.display_success_message():
            assert True
        else:
            self.driver.save_screenshot(screenshot)
            assert False
