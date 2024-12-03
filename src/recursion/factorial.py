"""
factorial module

This module is used to compute the factorial of non-negative integers.
"""


def factorial(n: int) -> int:
    """Compute the factorial of a non-negative integer n.

    Args:
        n (int): A non-negative integer.
    Returns:
        int: The factorial of n.
    """
    # 如果輸入不是整數，引發型別錯誤
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    # 如果輸入是負整數，引發值錯誤
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    # 如果輸入是0，回傳1 (base case)
    if n == 0:
        return 1
    # 如果輸入是正整數，回傳 `n`乘以`factorial(n-1)` (recursive case)
    return n * factorial(n - 1)
