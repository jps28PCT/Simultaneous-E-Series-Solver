"""
This test is for the engineering notation parser and engineering notation string formatter.
"""

import unittest
from e_vals import eng_note, eng_to_float


class test_engineering_notation(unittest.TestCase):
  testFloat = 3.1415926535897932384
  
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




if __name__ == '__main__':
    unittest.main()
