"""
Practice Exercise: Calculator Module

This module contains a simple calculator with several intentional bugs.
"""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exponent):
    """Calculate base raised to exponent."""
    if exponent < 0:
        if base == 0:
            raise ValueError("Cannot raise zero to a negative power")
        return 1 / power(base, -exponent)
    result = 1
    for i in range(exponent):
        result = result * base
    return result


def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    # Use iterative approach to avoid recursion limit
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def average(numbers):
    """Calculate average of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    # Validate that all elements are numeric
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError(f"All elements must be numeric, got {type(num).__name__}")
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
