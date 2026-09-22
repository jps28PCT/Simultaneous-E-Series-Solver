"""
This test is for the input validation functions.
"""

import unittest
import re
from e_vals import InvalidValueError, component_check, relationship_check, e_series_selection_check, decade_check


class test_input_validation(unittest.TestCase):

    ### COMPONENT CHECK

    def test_component_invalid_output_str(self):
        returnedStr = component_check(component="R1", out="TEST")
        self.assertEqual(returnedStr, "NONE SELECTED")

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

    def test_relationship_invalid_output_str(self):
        returnedStr = relationship_check(relationship="3.3 = 5 * (R2 / (R1 + R2))", out="TEST")
        self.assertEqual(returnedStr, "NONE SELECTED")

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
    

    ### E-SERIES SELECTION CHECK

    def test_e_series_selection_invalid_output_str(self):
        returnedStr = e_series_selection_check(e_series_selection=24, out="TEST")
        self.assertEqual(returnedStr, "NONE SELECTED")

    def test_e_series_selection_valid_str(self):
        e_series = [3, 6, 12, 24, 48, 96, 192]
        for e_series_selection in e_series:
            with self.subTest(e_series_selection=e_series_selection):
                returnedStr = e_series_selection_check(e_series_selection=e_series_selection, out="str")
                self.assertEqual(returnedStr, "")

    def test_e_series_selection_valid_err(self):
        e_series = [3, 6, 12, 24, 48, 96, 192]
        for e_series_selection in e_series:
            with self.subTest(e_series_selection=e_series_selection):
                e_series_selection_check(e_series_selection=e_series_selection, out="exception")
                pass

    def test_e_series_selection_invalid_str(self):
        invalid = [-3, 0, 2, '1k', True]
        for value in invalid:
            with self.subTest(value=value):
                returnedStr = e_series_selection_check(e_series_selection=value, out="str")
                self.assertEqual(returnedStr, "Value must be a valid E-Series number.")
    
    def test_e_series_selection_invalid_err(self):
        invalid = [-3, 0, 2, '1k', True]
        for value in invalid:
            with self.subTest(value=value):
                with self.assertRaisesRegex(InvalidValueError, "Value must be a valid E-Series number."):
                    e_series_selection_check(e_series_selection=value, out="exception")
    


    ### DECADE CHECK

    def test_decade_invalid_output_str(self):
        returnedStr = decade_check(decade=100, out="TEST")
        self.assertEqual(returnedStr, "NONE SELECTED")

    def test_decade_check_valid_str(self):
        test_value = 1e-12
        round_to = 12
        while test_value <= 100e12:
            with self.subTest(test_value=test_value):
                returnedStr = decade_check(decade=round(test_value, round_to), out="str")
                self.assertEqual(returnedStr, "")

            test_value = test_value * 10
            round_to -= 1
            if round_to < 0:
                round_to = 0

    def test_decade_check_valid_err(self):
        test_value = 1e-12
        round_to = 12
        while test_value <= 100e12:
            with self.subTest(test_value=test_value):
                decade_check(decade=round(test_value, round_to), out="exception")
                pass

            test_value = test_value * 10
            round_to -= 1
            if round_to < 0:
                round_to = 0

    def test_decade_zero_str(self):
        returnedStr = decade_check(decade=0, out="str")
        self.assertEqual(returnedStr, "Decade cannot be zero.")

    def test_decade_zero_err(self):
        with self.assertRaisesRegex(InvalidValueError, "Decade cannot be zero."):
            decade_check(decade=0, out="exception")

    def test_decad_negative_str(self):
        returnedStr = decade_check(decade=-1, out="str")
        self.assertEqual(returnedStr, "Decade cannot be negative.")
    
    def test_decade_negative_err(self):
        with self.assertRaisesRegex(InvalidValueError, "Decade cannot be negative."):
            decade_check(decade=-1, out="exception")

    def test_decade_invalid_str(self):
        invalid = [0.02, 0.3, 4, 50, 600]
        for value in invalid:
            with self.subTest(value=value):
                returnedStr = decade_check(decade=value, out="str")
                self.assertEqual(returnedStr, "Value must be a decade expressed a power of 10.")
    
    def test_decade_invalid_err(self):
        invalid = [0.02, 0.3, 4, 50, 600]
        for value in invalid:
            with self.subTest(value=value):
                with self.assertRaisesRegex(InvalidValueError, "Value must be a decade expressed a power of 10."):
                    decade_check(decade=value, out="exception")
    

if __name__ == '__main__':
    unittest.main()
