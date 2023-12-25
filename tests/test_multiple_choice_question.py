import pytest
from Utilities.constants import *
from Utilities.return_message import *

@pytest.mark.usefixtures("setup_and_teardown")
class TestMultipleChoiceQuestion:
    
    def test_001(self):
        self.log.getthelogs().info('TEST CASE, test_001')
        self.multiple_choice_question.add_question_multiple_choice_question(HINDI, PASSAGE_VALUE)
