"""
This test is for the engineering notation parser and engineering notation string formatter.
"""

import unittest
from e_vals import eng_note, eng_to_float


class test_engineering_notation(unittest.TestCase):
  TEST_FLOAT = 3.1415926535897932384
  
  def test_float_to_eng_zero(self):
    returnedStr = eng_note(inputValue=0.0, numSigFigs=1)
    self.assertEqual(returnedStr, "0  ")

  def test_float_to_eng_ascii_inf(self):
      returnedStr = eng_note(inputValue=float('inf'), numSigFigs=1, encoding="ASCII")
      self.assertEqual(returnedStr, "inf  ")

  def test_float_to_eng_utf8_inf(self):
      returnedStr = eng_note(inputValue=float('inf'), numSigFigs=1, encoding="UTF-8")
      self.assertEqual(returnedStr, "\u221E  ")

  def test_float_to_eng_ascii_neg_inf(self):
      returnedStr = eng_note(inputValue=float('-inf'), numSigFigs=1, encoding="ASCII")
      self.assertEqual(returnedStr, "-inf  ")

  def test_float_to_eng_utf8_neg_inf(self):
      returnedStr = eng_note(inputValue=float('-inf'), numSigFigs=1, encoding="UTF-8")
      self.assertEqual(returnedStr, "-\u221E  ")

  def test_float_to_eng_sig_figs(self):
    sig_fig_cases = [
                (1,  "3  "),
                (2,  "3.1  "),
                (3,  "3.14  "),
                (4,  "3.142  "),
                (5,  "3.1416  "),
                (6,  "3.14159  "),
                (7,  "3.141593  "),
                (8,  "3.1415927  "),
                (9,  "3.14159265  "),
                (10, "3.141592654  "),
                (11, "3.1415926536  "),
                (12, "3.14159265359  "),
                (13, "3.141592653590  "),
                (14, "3.1415926535898  "),
                (15, "3.14159265358979  "),
                (16, "3.141592653589793  ")]
    for sig_fig, expected in sig_fig_cases:
      with self.subTest(sig_fig=sig_fig):
        returnedStr = eng_note(inputValue=self.TEST_FLOAT, numSigFigs=sig_fig)
        self.assertEqual(returnedStr, expected)

if __name__ == '__main__':
    unittest.main()
