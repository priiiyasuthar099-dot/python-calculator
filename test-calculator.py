import pytest
from src import main

def test_add():
    assert main.add(2, 3) == 5
    assert main.add(-1, 1) == 0

def test_subtract():
    assert main.subtract(5, 2) == 3
    assert main.subtract(0, 3) == -3

def test_multiply():
    assert main.multiply(3, 4) == 12
    assert main.multiply(-2, -5) == 10

def test_divide():
    assert main.divide(10, 2) == 5
    assert pytest.approx(main.divide(1, 3), rel=1e-9) == 1/3

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        main.divide(5, 0)
