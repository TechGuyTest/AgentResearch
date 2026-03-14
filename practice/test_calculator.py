"""
Unit Tests for Calculator Module

These tests expose bugs in the calculator.py module.
"""

import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from practice.calculator import (
    add, subtract, multiply, divide, 
    power, factorial, average
)


class TestAdd(unittest.TestCase):
    """Tests for the add function."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        self.assertEqual(add(-2, -3), -5)
    
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        self.assertEqual(add(-2, 3), 1)
    
    def test_add_zero(self):
        """Test adding zero."""
        self.assertEqual(add(5, 0), 5)


class TestSubtract(unittest.TestCase):
    """Tests for the subtract function."""
    
    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        self.assertEqual(subtract(5, 3), 2)
    
    def test_subtract_negative_result(self):
        """Test subtraction resulting in negative number."""
        self.assertEqual(subtract(3, 5), -2)
    
    def test_subtract_zero(self):
        """Test subtracting zero."""
        self.assertEqual(subtract(5, 0), 5)


class TestMultiply(unittest.TestCase):
    """Tests for the multiply function."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        self.assertEqual(multiply(3, 4), 12)
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        self.assertEqual(multiply(5, 0), 0)
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        self.assertEqual(multiply(-3, -4), 12)


class TestDivide(unittest.TestCase):
    """Tests for the divide function."""
    
    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        self.assertEqual(divide(10, 2), 5)
    
    def test_divide_by_one(self):
        """Test dividing by one."""
        self.assertEqual(divide(10, 1), 10)
    
    def test_divide_by_zero(self):
        """Test dividing by zero - should handle gracefully."""
        with self.assertRaises(ValueError):
            divide(10, 0)  # This should raise ValueError, not ZeroDivisionError


class TestPower(unittest.TestCase):
    """Tests for the power function."""
    
    def test_power_positive_exponent(self):
        """Test power with positive exponent."""
        self.assertEqual(power(2, 3), 8)
    
    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        self.assertEqual(power(5, 0), 1)
    
    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        # This should return a fraction, not 1
        self.assertEqual(power(2, -2), 0.25)


class TestFactorial(unittest.TestCase):
    """Tests for the factorial function."""
    
    def test_factorial_zero(self):
        """Test factorial of zero."""
        self.assertEqual(factorial(0), 1)
    
    def test_factorial_one(self):
        """Test factorial of one."""
        self.assertEqual(factorial(1), 1)
    
    def test_factorial_five(self):
        """Test factorial of five."""
        self.assertEqual(factorial(5), 120)
    
    def test_factorial_recursion_limit(self):
        """Test that factorial doesn't cause infinite recursion."""
        # This should complete without RecursionError
        result = factorial(10)
        self.assertEqual(result, 3628800)


class TestAverage(unittest.TestCase):
    """Tests for the average function."""
    
    def test_average_positive_numbers(self):
        """Test average of positive numbers."""
        self.assertEqual(average([1, 2, 3, 4, 5]), 3.0)
    
    def test_average_single_number(self):
        """Test average of single number."""
        self.assertEqual(average([5]), 5.0)
    
    def test_average_empty_list(self):
        """Test average of empty list - should handle gracefully."""
        with self.assertRaises(ValueError):
            average([])  # Should raise ValueError for empty list
    
    def test_average_non_numeric_values(self):
        """Test average with non-numeric values - should raise ValueError."""
        # BUG: Currently raises TypeError instead of ValueError
        # After fix, should raise ValueError with clear message
        with self.assertRaises(ValueError):
            average(['a', 'b', 'c'])
    
    def test_average_mixed_types(self):
        """Test average with mixed numeric and non-numeric values."""
        # BUG: Currently raises TypeError instead of ValueError
        # After fix, should raise ValueError with clear message
        with self.assertRaises(ValueError):
            average([1, 2, 'three', 4])


class TestPowerEdgeCases(unittest.TestCase):
    """Additional tests for power function edge cases."""
    
    def test_power_zero_base_negative_exponent(self):
        """Test power with zero base and negative exponent - should raise ValueError."""
        # BUG: Currently raises ZeroDivisionError
        # After fix, should raise ValueError with clear message
        with self.assertRaises(ValueError):
            power(0, -2)
    
    def test_power_zero_base_zero_exponent(self):
        """Test power with zero base and zero exponent (0^0 is mathematically undefined)."""
        # Conventionally returns 1 in many implementations
        result = power(0, 0)
        self.assertIn(result, [1, 0])  # Either 1 (convention) or 0 is acceptable
    
    def test_power_large_exponent(self):
        """Test power with large exponent."""
        result = power(2, 10)
        self.assertEqual(result, 1024)


class TestFactorialEdgeCases(unittest.TestCase):
    """Additional tests for factorial function edge cases."""
    
    def test_factorial_large_number(self):
        """Test factorial with large number - should handle without RecursionError."""
        # BUG: Currently causes RecursionError for n >= 1000
        # This test will fail until the bug is fixed
        try:
            result = factorial(100)
            self.assertGreater(result, 0)
        except RecursionError:
            self.fail("factorial(100) should not cause RecursionError")
    
    def test_factorial_very_large_number(self):
        """Test factorial with very large number."""
        # This should complete without RecursionError after fix
        try:
            result = factorial(500)
            self.assertGreater(result, 0)
        except RecursionError:
            self.fail("factorial(500) should not cause RecursionError")


if __name__ == '__main__':
    unittest.main()
