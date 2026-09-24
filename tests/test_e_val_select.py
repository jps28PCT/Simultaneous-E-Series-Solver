"""
This test is for the main solver engine. It may take a while to fully run.

When writing tests, all intended test outputs must be coprime () LCM = 1 ) to ensure only one valid solution set.
e_val_select() is not to be used to calculate the outputs to test against.
"""

import unittest
from e_vals import e_val_select


class test_e_val_select(unittest.TestCase):

    def test_fully_determined(self):
    # Tests fully determined case
        components = "R1 R2 R3"
        relationships = [
            "2879 = 1/((1/R2) + (1/R3))",   # Adding R2 and R3 in parallel
            "3699 = R1 + 2879",             # Adding R1 in series with R2||R3
            "0.001 = 11 / R2"               # Current through R2 when applying 11V across it
        ]
        e_series_selection = (
            24,                 # R1
            24,                 # R2
            24                  # R3
        )
        decade_selection = (
            100,                # R1
            10000,              # R2
            1000                # R3
        )
        test_solution = {"R1":(820, 0.0), "R2":(11000, 0.0), "R3":(3900, 9.157219994310748e-05)}

        solution = e_val_select(components=components, relationships=relationships, e_series_selection=e_series_selection, decade_selection=decade_selection)
        with self.subTest(solution=solution, test_solution=test_solution):
            for key in test_solution:
                self.assertEqual(solution[key][0], test_solution[key][0])           # Check component values match exactly
                self.assertAlmostEqual(solution[key][1], test_solution[key][1])     # Check error is close


if __name__ == '__main__':
    unittest.main()