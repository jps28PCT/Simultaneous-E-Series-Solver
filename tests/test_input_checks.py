"""
This test is for the input validation functions.
"""

import unittest
from e_vals import InvalidValueError, component_check, relationship_check, e_series_selection_check, decade_check


class test_input_validation(unittest.TestCase):

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



if __name__ == '__main__':
    unittest.main()
