import math
import unittest
from contextlib import redirect_stdout
from io import StringIO

from logitfunction.core import logitfunction, main


class TestLogitFunction(unittest.TestCase):
    def test_logitfunction_valid_input(self):
        # Test valid inputs
        self.assertAlmostEqual(logitfunction(0.5), 0.0, places=7)
        self.assertAlmostEqual(logitfunction(0.25), -1.3862943611, places=7)
        self.assertAlmostEqual(logitfunction(0.75), 1.0986122887, places=7)

    def test_logitfunction_invalid_input(self):
        # Test invalid inputs
        self.assertTrue(math.isnan(logitfunction(-0.1)))
        self.assertTrue(math.isnan(logitfunction(0.0)))
        self.assertTrue(math.isnan(logitfunction(1.0)))
        self.assertTrue(math.isnan(logitfunction(1.1)))


class TestMainFunction(unittest.TestCase):
    def test_main_valid_input(self):
        # Capture the output of the main function
        with StringIO() as captured_output, redirect_stdout(captured_output):
            main(["", "0.5"])
            self.assertEqual(captured_output.getvalue().strip(), "0.0")

    def test_main_invalid_input(self):
        # Test invalid input handling
        with StringIO() as captured_output, redirect_stdout(captured_output):
            main(["", "-0.1"])
            self.assertEqual(captured_output.getvalue().strip(), "nan")

        with StringIO() as captured_output, redirect_stdout(captured_output):
            main(["", "1.0"])
            self.assertEqual(captured_output.getvalue().strip(), "nan")


if __name__ == "__main__":
    unittest.main()
