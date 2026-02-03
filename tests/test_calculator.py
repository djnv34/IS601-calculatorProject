import pytest

from calculator.calculator import (
    addOperator,
    subtractOperator,
    multiplyOperator,
    divideOperator
)


def test_add():
    assert addOperator(2, 3) == 5


def test_subtract():
    assert subtractOperator(5, 3) == 2


def test_multiply():
    assert multiplyOperator(4, 3) == 12


def test_divide():
    assert divideOperator(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divideOperator(10, 0)