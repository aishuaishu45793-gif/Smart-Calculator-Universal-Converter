
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot calculate modulus with zero.")
    return a % b


def power(a, b):
    return a ** b


def percentage(value, percent):
    return value * percent / 100
