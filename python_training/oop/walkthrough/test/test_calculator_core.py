# TDD - Test-Driven Development 
# BDD - Behaviour-Driven Development

# TDD - Write tests before writing code.


from unittest import TestCase, mock, main as unittest_main
from core.calculator import Calculator


class CoreCalcTests(TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_successful(self):
        """Test if core addition function returns expected result"""

        x, y = 5, 5
        expected_res = x + y

        res = self.calculator.add(x, y)
        self.assertEqual(expected_res, res)
    


if __name__ == "__main__":
    unittest_main()
