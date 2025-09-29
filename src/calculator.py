"""
Calculator Module - Basic arithmetic operations
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b

def divide(a, b):
    """Divide a by b"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def power(a, b): 
    return a ** b 

def square_root(a):
    """Calculate square root of a"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a ** 0.5

