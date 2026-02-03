def addOperator(a, b):
    return a + b


def subtractOperator(a, b):
    return a - b


def multiplyOperator(a, b):
    return a * b


def divideOperator(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
