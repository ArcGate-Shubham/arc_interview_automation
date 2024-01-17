from selenium.webdriver.common.by import By


class Locators:
    ADD_NEW_QUESTION_BUTTON = (By.CSS_SELECTOR, 'button.AddRecordBtn')
    INPUT_SUBJECT = (By.ID, 'IBSQ_subject')
    INPUT_QUESTION_TITLE = (By.ID, 'IBSQ_question')
    INPUT_ANSWER_KEYS = (By.ID, 'IBSQ_answer_key')
    INPUT_IMAGE = (By.XPATH, '//input[@type="file"]')
    SAVE_BUTTON = (By.ID, 'save-button')
    CLOSE_BUTTON = (By.ID, 'close-button')
    DISPLAY_MESSAGE = (By.ID, 'notice')
    PARSLEY_REQUIRED = (By.CLASS_NAME, 'parsley-required')
    PARSLEY_MAXFILESIZE = (By.CLASS_NAME, 'parsley-maxFileSize')
    PARSLEY_FILEEXTENSION = (By.CLASS_NAME, 'parsley-fileextension')
    GET_QUESTION_TEXT = (By.CSS_SELECTOR, 'td.EditData')
    PARSLEY_PATTERN = (By.CLASS_NAME, 'parsley-pattern')
    
class SubjectPageLocators:
    INPUT_SUBJECT = (By.NAME, 'subject')