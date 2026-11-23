import math

def square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(number)

def factorial(number):
    if number < 0 or not float(number).is_integer():
        raise ValueError("Factorial requires a non-negative integer.")
    return math.factorial(int(number))

def sine(angle):
    return math.sin(math.radians(angle))

def cosine(angle):
    return math.cos(math.radians(angle))

def tangent(angle):
    if math.isclose(math.cos(math.radians(angle)), 0, abs_tol=1e-12):
        raise ValueError("Tangent is undefined for this angle.")
    return math.tan(math.radians(angle))

def logarithm(number):
    if number <= 0:
        raise ValueError("Logarithm requires a positive number.")
    return math.log10(number)

def natural_log(number):
    if number <= 0:
        raise ValueError("Natural logarithm requires a positive number.")
    return math.log(number)
