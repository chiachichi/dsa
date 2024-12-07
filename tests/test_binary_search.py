"""This module is used to test `src/recursion_binary_search.py`"""

from src.recursion.binary_search import binary_search


def test_normal_cases():
    assert (
        binary_search(data=[1, 3, 4, 6, 9, 22], target=3, low=0, high=5)
        is True
    )
    assert (
        binary_search(data=[1, 3, 4, 6, 9, 22], target=10, low=0, high=5)
        is False
    )


def test_edge_cases():
    assert binary_search(data=[1], target=1, low=0, high=0) is True
    assert binary_search(data=[1], target=0, low=0, high=0) is False
