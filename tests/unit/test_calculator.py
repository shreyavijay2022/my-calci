from src.calculator import add, subtract, divide, multiply

class TestMultiplyDivide:
    """Test multiplication and division operations"""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers"""
        assert multiply(3, 4) == 12
        assert multiply(7, 8) == 56

    def test_multiply_by_zero(self):
        """Test multiplying by zero"""
        assert multiply(5, 0) == 0
        assert multiply(0, 10) == 0

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers"""
        assert multiply(-2, 3) == -6
        assert multiply(-4, -5) == 20

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers"""
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers"""
        assert divide(-10, 2) == -5
        assert divide(-12, -3) == 4

import pytest
from src.calculator import power, square_root

class TestAdvancedOperations:
    """Test power and square root operations"""

    def test_power_positive_numbers(self):
        """Test power with positive numbers"""
        assert power(2, 3) == 8
        assert power(5, 2) == 25

    def test_power_zero_exponent(self):
        """Test power with zero exponent"""
        assert power(5, 0) == 1
        assert power(0, 0) == 1

    def test_square_root_positive_numbers(self):
        """Test square root of positive numbers"""
        assert square_root(4) == 2
        assert square_root(9) == 3
        assert square_root(16) == 4

    def test_square_root_negative_raises_error(self):
        """Test that square root of negative raises ValueError"""
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            square_root(-4)
