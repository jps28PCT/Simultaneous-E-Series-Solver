"""
This test is for the input validation functions.
"""

import unittest
import re
from e_vals import InvalidValueError, component_check, relationship_check, e_series_selection_check, decade_check


class test_input_validation(unittest.TestCase):

    ### COMPONENT CHECK

    def test_component_valid_str(self):
        returnedStr = component_check(component="R1", out="str")
        self.assertEqual(returnedStr, "")

    def test_component_valid_err(self):
        component_check(component="R1", out="exception")
        pass

    def test_component_first_letter_str(self):
        returnedStr = component_check(component="1R", out="str")
        self.assertEqual(returnedStr, "First character is not a letter.")
    
    def test_component_first_letter_err(self):
        with self.assertRaisesRegex(InvalidValueError, "First character is not a letter."):
            component_check(component="1R", out="exception")

    def test_component_other_symbols_str(self):
        returnedStr = component_check(component="R!", out="str")
        self.assertEqual(returnedStr, "Contains characters other than letters, numbers, or underscore.")

    def test_component_other_symbols_err(self):
        with self.assertRaisesRegex(InvalidValueError, "Contains characters other than letters, numbers, or underscore."):
            component_check(component="R!", out="exception")

    def test_component_keywords_str(self):
        keywords = ['pi','e', 'phi', 'sqrt_2','sqrt_3','Y', 'Z', 'E', 'P', 'T', 
                        'G', 'M', 'k', 'm', 'u', 'n', 'p', 'f', 'a', 'z', 'y' ]
        for keyword in keywords:
            with self.subTest(keyword=keyword):
                returnedStr = component_check(component=keyword, out="str")
                self.assertEqual(returnedStr, "Component name cannot be reserved keyword.")

    def test_component_keywords_err(self):
        keywords = ['pi','e', 'phi', 'sqrt_2','sqrt_3','Y', 'Z', 'E', 'P', 'T', 
                        'G', 'M', 'k', 'm', 'u', 'n', 'p', 'f', 'a', 'z', 'y' ]
        for keyword in keywords:
            with self.subTest(keyword=keyword):
                with self.assertRaisesRegex(InvalidValueError, "Component name cannot be reserved keyword."):
                    component_check(component=keyword, out="exception")

    ### RELATIONSHIP CHECK

    def test_relationship_valid_str(self):
        returnedStr = relationship_check(relationship="3.3 = 5 * (R2 / (R1 + R2))", out="str")
        self.assertEqual(returnedStr, "")

    def test_relationship_valid_err(self):
        relationship_check(relationship="3.3 = 5 * (R2 / (R1 + R2))", out="exception")
        pass

    def test_relationship_no_equal_sign_str(self):
        returnedStr = relationship_check(relationship="5 * (R2 / (R1 + R2))", out="str")
        self.assertEqual(returnedStr, "Relationship equation must contain an equals sign.")

    def test_relationship_no_equal_sign_err(self):
        with self.assertRaisesRegex(InvalidValueError, re.escape("Relationship equation must contain an equals sign.")):
            relationship_check(relationship="5 * (R2 / (R1 + R2))", out="exception")

    def test_relationship_caret_str(self):
        returnedStr = relationship_check(relationship="10*k = 1/((2*pi*R1*C1)^(1/2))", out="str")
        self.assertEqual(returnedStr, "Caret cannot be used for exponentiation. Use two asterisks (A**B).")
    
    def test_relationship_caret_err(self):
        with self.assertRaisesRegex(InvalidValueError, re.escape("Caret cannot be used for exponentiation. Use two asterisks (A**B).")):
            relationship_check(relationship="10*k = 1/((2*pi*R1*C1)^(1/2))", out="exception")
    


if __name__ == '__main__':
    unittest.main()
