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

  def test_float_to_eng_ascii_prefixes(self):
    prefixes_cases = [
              (self.TEST_FLOAT*10**-24, "3.1416 y"),
              (self.TEST_FLOAT*10**-23, "31.416 y"),
              (self.TEST_FLOAT*10**-22, "314.16 y"),
              (self.TEST_FLOAT*10**-21, "3.1416 z"),
              (self.TEST_FLOAT*10**-20, "31.416 z"),
              (self.TEST_FLOAT*10**-19, "314.16 z"),
              (self.TEST_FLOAT*10**-18, "3.1416 a"),
              (self.TEST_FLOAT*10**-17, "31.416 a"),
              (self.TEST_FLOAT*10**-16, "314.16 a"),
              (self.TEST_FLOAT*10**-15, "3.1416 f"),
              (self.TEST_FLOAT*10**-14, "31.416 f"),
              (self.TEST_FLOAT*10**-13, "314.16 f"),
              (self.TEST_FLOAT*10**-12, "3.1416 p"),
              (self.TEST_FLOAT*10**-11, "31.416 p"),
              (self.TEST_FLOAT*10**-10, "314.16 p"),
              (self.TEST_FLOAT*10**-9,  "3.1416 n"),
              (self.TEST_FLOAT*10**-8,  "31.416 n"),
              (self.TEST_FLOAT*10**-7,  "314.16 n"),
              (self.TEST_FLOAT*10**-6,  "3.1416 u"),
              (self.TEST_FLOAT*10**-5,  "31.416 u"),
              (self.TEST_FLOAT*10**-4,  "314.16 u"),
              (self.TEST_FLOAT*10**-3,  "3.1416 m"),
              (self.TEST_FLOAT*10**-2,  "31.416 m"),
              (self.TEST_FLOAT*10**-1,  "314.16 m"),
              (self.TEST_FLOAT*10**0,   "3.1416  "),
              (self.TEST_FLOAT*10**1,   "31.416  "),
              (self.TEST_FLOAT*10**2,   "314.16  "),
              (self.TEST_FLOAT*10**3,   "3.1416 k"),
              (self.TEST_FLOAT*10**4,   "31.416 k"),
              (self.TEST_FLOAT*10**5,   "314.16 k"),
              (self.TEST_FLOAT*10**6,   "3.1416 M"),
              (self.TEST_FLOAT*10**7,   "31.416 M"),
              (self.TEST_FLOAT*10**8,   "314.16 M"),
              (self.TEST_FLOAT*10**9,   "3.1416 G"),
              (self.TEST_FLOAT*10**10,  "31.416 G"),
              (self.TEST_FLOAT*10**11,  "314.16 G"),
              (self.TEST_FLOAT*10**12,  "3.1416 T"),
              (self.TEST_FLOAT*10**13,  "31.416 T"),
              (self.TEST_FLOAT*10**14,  "314.16 T"),
              (self.TEST_FLOAT*10**15,  "3.1416 P"),
              (self.TEST_FLOAT*10**16,  "31.416 P"),
              (self.TEST_FLOAT*10**17,  "314.16 P"),
              (self.TEST_FLOAT*10**18,  "3.1416 E"),
              (self.TEST_FLOAT*10**19,  "31.416 E"),
              (self.TEST_FLOAT*10**20,  "314.16 E"),
              (self.TEST_FLOAT*10**21,  "3.1416 Z"),
              (self.TEST_FLOAT*10**22,  "31.416 Z"),
              (self.TEST_FLOAT*10**23,  "314.16 Z"),
              (self.TEST_FLOAT*10**24,  "3.1416 Y"),
              (self.TEST_FLOAT*10**25,  "31.416 Y"),
              (self.TEST_FLOAT*10**26,  "314.16 Y")]
    
    for test_value, expected in prefixes_cases:
      with self.subTest(test_value=test_value):
        returnedStr = eng_note(inputValue=test_value, numSigFigs=5, encoding="ASCII")
        self.assertEqual(returnedStr, expected)

  def test_float_to_eng_utf8_prefixes(self):
    prefixes_cases = [
              (self.TEST_FLOAT*10**-24, "3.1416 y"),
              (self.TEST_FLOAT*10**-23, "31.416 y"),
              (self.TEST_FLOAT*10**-22, "314.16 y"),
              (self.TEST_FLOAT*10**-21, "3.1416 z"),
              (self.TEST_FLOAT*10**-20, "31.416 z"),
              (self.TEST_FLOAT*10**-19, "314.16 z"),
              (self.TEST_FLOAT*10**-18, "3.1416 a"),
              (self.TEST_FLOAT*10**-17, "31.416 a"),
              (self.TEST_FLOAT*10**-16, "314.16 a"),
              (self.TEST_FLOAT*10**-15, "3.1416 f"),
              (self.TEST_FLOAT*10**-14, "31.416 f"),
              (self.TEST_FLOAT*10**-13, "314.16 f"),
              (self.TEST_FLOAT*10**-12, "3.1416 p"),
              (self.TEST_FLOAT*10**-11, "31.416 p"),
              (self.TEST_FLOAT*10**-10, "314.16 p"),
              (self.TEST_FLOAT*10**-9,  "3.1416 n"),
              (self.TEST_FLOAT*10**-8,  "31.416 n"),
              (self.TEST_FLOAT*10**-7,  "314.16 n"),
              (self.TEST_FLOAT*10**-6,  "3.1416 \u03BC"),
              (self.TEST_FLOAT*10**-5,  "31.416 \u03BC"),
              (self.TEST_FLOAT*10**-4,  "314.16 \u03BC"),
              (self.TEST_FLOAT*10**-3,  "3.1416 m"),
              (self.TEST_FLOAT*10**-2,  "31.416 m"),
              (self.TEST_FLOAT*10**-1,  "314.16 m"),
              (self.TEST_FLOAT*10**0,   "3.1416  "),
              (self.TEST_FLOAT*10**1,   "31.416  "),
              (self.TEST_FLOAT*10**2,   "314.16  "),
              (self.TEST_FLOAT*10**3,   "3.1416 k"),
              (self.TEST_FLOAT*10**4,   "31.416 k"),
              (self.TEST_FLOAT*10**5,   "314.16 k"),
              (self.TEST_FLOAT*10**6,   "3.1416 M"),
              (self.TEST_FLOAT*10**7,   "31.416 M"),
              (self.TEST_FLOAT*10**8,   "314.16 M"),
              (self.TEST_FLOAT*10**9,   "3.1416 G"),
              (self.TEST_FLOAT*10**10,  "31.416 G"),
              (self.TEST_FLOAT*10**11,  "314.16 G"),
              (self.TEST_FLOAT*10**12,  "3.1416 T"),
              (self.TEST_FLOAT*10**13,  "31.416 T"),
              (self.TEST_FLOAT*10**14,  "314.16 T"),
              (self.TEST_FLOAT*10**15,  "3.1416 P"),
              (self.TEST_FLOAT*10**16,  "31.416 P"),
              (self.TEST_FLOAT*10**17,  "314.16 P"),
              (self.TEST_FLOAT*10**18,  "3.1416 E"),
              (self.TEST_FLOAT*10**19,  "31.416 E"),
              (self.TEST_FLOAT*10**20,  "314.16 E"),
              (self.TEST_FLOAT*10**21,  "3.1416 Z"),
              (self.TEST_FLOAT*10**22,  "31.416 Z"),
              (self.TEST_FLOAT*10**23,  "314.16 Z"),
              (self.TEST_FLOAT*10**24,  "3.1416 Y"),
              (self.TEST_FLOAT*10**25,  "31.416 Y"),
              (self.TEST_FLOAT*10**26,  "314.16 Y")]
    
    for test_value, expected in prefixes_cases:
      with self.subTest(test_value=test_value):
        returnedStr = eng_note(inputValue=test_value, numSigFigs=5, encoding="UTF-8")
        self.assertEqual(returnedStr, expected)


if __name__ == '__main__':
    unittest.main()
