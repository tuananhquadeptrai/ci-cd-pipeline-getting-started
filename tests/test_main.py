# tests/test_main.py

from src.main import add
import pytest

def test_add_function_positive():
    """
    Tests the add function with positive numbers.
    This test ensures that the basic addition of two positive integers works correctly.
    """
    assert add(1, 2) == 3
    assert add(5, 5) == 10

def test_add_function_negative():
    """
    Tests the add function with negative numbers.
    This test checks the function's ability to handle addition
    involving negative values.
    """
    assert add(-1, -1) == -2
    assert add(-5, 5) == 0

def test_add_function_float():
    """
    Tests the add function with floating-point numbers.
    This ensures the function is not limited to integers.
    """
    assert add(2.5, 2.5) == 5.0
