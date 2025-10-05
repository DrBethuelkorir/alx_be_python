import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---------- ADDITION TESTS ----------
    def test_addition_positive_numbers(self):
        """Test addition with positive numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_mixed_signs(self):
        """Test addition with one positive and one negative number."""
        self.assertEqual(self.calc.add(-2, 3), 1)
        self.assertEqual(self.calc.add(2, -3), -1)

    def test_addition_with_zero(self):
        """Test addition where one operand is zero."""
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)

    # ---------- SUBTRACTION TESTS ----------
    def test_subtraction_positive_numbers(self):
        """Test subtraction with positive numbers."""
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtraction_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtraction_mixed_signs(self):
        """Test subtraction with one positive and one negative number."""
        self.assertEqual(self.calc.subtract(5, -3), 8)
        self.assertEqual(self.calc.subtract(-5, 3), -8)

    def test_subtraction_with_zero(self):
        """Test subtraction involving zero."""
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # ---------- MULTIPLICATION TESTS ----------
    def test_multiplication_positive_numbers(self):
        """Test multiplication with positive numbers."""
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiplication_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-4, -3), 12)

    def test_multiplication_mixed_signs(self):
        """Test multiplication with one positive and one negative number."""
        self.assertEqual(self.calc.multiply(-4, 3), -12)
        self.assertEqual(self.calc.multiply(4, -3), -12)

    def test_multiplication_with_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(100, 0), 0)

    # ---------- DIVISION TESTS ----------
    def test_division_positive_numbers(self):
        """Test division with positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_division_mixed_signs(self):
        """Test division with one positive and one negative number."""
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))

    def test_division_zero_numerator(self):
        """Test division when numerator is zero."""
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division_float_result(self):
        """Test division that results in a float."""
        self.assertEqual(self.calc.divide(7, 2), 3.5)


if __name__ == "__main__":
    unittest.main()
