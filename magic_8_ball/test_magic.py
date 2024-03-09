# TODO create a test case to test each of the following functions,

# generate_url_for_question
#  - check that the expected URL is returned for an example question. 

# extract_answer_from_response
#  - one test should create some example dictionaries that match the expected response from the API,
#  and check that the correct answer is extracted and returned.
#  - another test should create example dictionaries with a different structure to the one returned from the API, 
#  and check that the function returns None.

import unittest
from unittest.mock import patch
from functions_magic import generate_url_for_question, extract_answer_from_response

class TestFunctionMagic(unittest.TestCase):

    def test_generate_url_for_question(self):
        # Test with an example question
        question = "What is your name?"
        expected_url = "https://magic-8-ball-mctc.uc.r.appspot.com/magic/JSON/What is your name?"
        self.assertEqual(generate_url_for_question(question), expected_url)

    def test_extract_answer_from_response(self):
        # Test with a valid response dictionary
        valid_response = {
            'question': 'Will it be sunny tomorrow?',
            'answer': 'Yes',
            'type': 'Affirmative'
            }
        self.assertEqual(extract_answer_from_response(valid_response), 'Yes')

        # Test with an invalid response dictionary
        invalid_response = {
            'invalid_key': 'Invalid value'
            }
        self.assertIsNone(extract_answer_from_response(invalid_response))

#  TODO to think about - what else could you test about this program? 
#  What types of expected and unexpected behavior might happen? You may be able to write tests for some 
#  of your ideas now. We'll talk about ways to test other aspects of this program in class.

# Testing URL if your question is empty
    def test_generate_url_for_empty_question(self):
        question = ""
        expected_url = "https://magic-8-ball-mctc.uc.r.appspot.com/magic/JSON/"
        self.assertEqual(generate_url_for_question(question), expected_url)
# Testing URL if your question contain special characters
    def test_generate_url_for_special_character(self):
        question = ",.,.,.'[]"
        expected_url = "https://magic-8-ball-mctc.uc.r.appspot.com/magic/JSON/,.,.,.'[]"
        self.assertEqual(generate_url_for_question(question), expected_url)
# Testing response if your question is empty
    def test_response_with_empty_question(self):
        valid_response = {
            'question': '',
            'answer': '',
            'type': 'Affirmative'
            }
        self.assertEqual(extract_answer_from_response(valid_response),'')



if __name__ == '__main__':
    unittest.main()



