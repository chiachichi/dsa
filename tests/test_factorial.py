"""
test_factorial module

This module is used to test the `factorial` function 
from `src/recursion/factorial.py`.
"""

import pytest
from src.recursion.factorial import factorial


def test_normal_cases():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800


def test_edge_cases():
    assert factorial(0) == 1
    assert factorial(1) == 1


def test_large_input():
    """測試大輸入是否會觸發遞迴限制"""
    with pytest.raises(RecursionError):
        factorial(1000)


def test_type_error():
    """測試輸入型別錯誤"""
    with pytest.raises(TypeError):
        factorial(2.5)
    with pytest.raises(TypeError):
        factorial("hello")


def test_value_error():
    """測試輸入值錯誤"""
    with pytest.raises(ValueError):
        factorial(-1)
