"""This module is used to implement binary search algorithm."""


def binary_search(data: list[int], target: int, low: int, high: int):
    """Return True if `target` in the interval
       from data[low] to data[high] (inclusive) else False

    Args:
        data (list[int]): An increasing sequence.
        target (int): Target value.
        low (int): Min index of interval.
        high (int): Max index of interval.
    """

    if low > high:  # interval is empty
        return False
    mid = int((low + high) / 2)  # median index of interval
    if target == data[mid]:  # gotcha! stop searching
        return True
    if target < data[mid]:  # search left side
        return binary_search(
            data, target, low, mid - 1
        )  # `return` the recursion result
    if target > data[mid]:  # search right side
        return binary_search(
            data, target, mid + 1, high
        )  # `return` the recursion result
