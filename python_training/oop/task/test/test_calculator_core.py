from unittest import TestCase, main
from core.calculator import Calculator

class CoreCalculatorTests(TestCase):
    
    def setUp(self):
        self.calculator = Calculator()

    def test_add_successful(self):
        
        x = 5
        y = 5
        expected_res = x + y

        res = self.calculator.add(x, y)

      
        print(self.calculator.add.__doc__)
        self.assertEqual(res, expected_res)

    def test_subtract_successful(self):
        
        x = 10
        y = 5
        expected_res = x - y

        res = self.calculator.subtract(x, y)
        self.assertEqual(res, expected_res)

    def test_multiply_successful(self):
        
        x = 5 
        y = 5
        expected_res = x * y

        res = self.calculator.multiply(x, y)
        self.assertEqual(res, expected_res)

    def test_divide_successful(self):
        
        x = 10
        y = 5
        expected_res = 10 / 5

        res = self.calculator.divide(x, y)
        self.assertEqual(res, expected_res)


    def test_zero_division_returns_friendly_error(self):
        
        x = 10
        y = 0
        expected_res = "Cannot divide by zero."

        res = self.calculator.divide(x, y)
        self.assertEqual(res, expected_res)

    def test_pow2_successful(self):
        
        x = 5
        expected_res = x ** 2

        res = self.calculator.pow2(x)
        self.assertEqual(res, expected_res)

    def test_non_integer_returns_friendly_error(self):
        
        x = "O"
        y = 9

        expected_res = "Please provide valid integers."

        res = self.calculator.add(x, y)
        self.assertEqual(res, expected_res)

        res = self.calculator.multiply(x, y)
        self.assertEqual(res, expected_res)

        res = self.calculator.subtract(x, y)
        self.assertEqual(res, expected_res)

        res = self.calculator.divide(x, y)
        self.assertEqual(res, expected_res)

        res = self.calculator.pow2(x, y)
        self.assertEqual(res, expected_res)


if __name__ == "__main__":
    main()