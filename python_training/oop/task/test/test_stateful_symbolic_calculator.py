
from unittest import TestCase, main as unittest_main
from core.stateful_calculator import StatefulSymbolicCalculator


class CalculatorBufferTests(TestCase):

    def setUp(self):
        self.calculator = StatefulSymbolicCalculator()

    def test_input_string_split(self):
        """
        Confirm that an inputted string returns the expected list of strings.
        """

        addition_input = "5 + 5"
        expected_res = ("5", "+", "5")

        res = self.calculator._split_input_string(addition_input)
        self.assertEqual(expected_res, res)


    def test_addition_string_returns_appropriate_calculation(self):
        """
        Confirm that if a user supplies the following operands,
        the appropriate core method is called.
        """
        
        addition_input = "5 + 5"
        expected_res = 5 + 5
        
        res = self.calculator.calculate_from_input(addition_input)
        self.assertEqual(expected_res, res)

        subtraction_input = "10 - 5"
        expected_res = 10 - 5

        res = self.calculator.calculate_from_input(subtraction_input)
        self.assertEqual(expected_res, res)

        multiplication_input = "5 x 5"
        expected_res = 5 * 5

        res = self.calculator.calculate_from_input(multiplication_input)
        self.assertEqual(expected_res, res)

        division_input = "10 / 5"
        expected_res = 10 / 5
        
        res = self.calculator.calculate_from_input(division_input)
        self.assertEqual(expected_res, res)


if __name__ == "__main__":
    unittest_main()

