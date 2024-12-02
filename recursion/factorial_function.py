def factorial(n: int):
    """Compute the value of the factorial function.

    Execution logic: 不斷跑遞迴直到達到 base case
    factorial(2) -> 2 * factorial(1)<---|
    factorial(1) -> 1 * factorial(0)<---|
    factorial(0) -> 1 ------------------|
    """
    # 檢查n是不是整數
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    # 根據階層函數的定義，n只能是正整數或0，當n是負值時，引發值異常
    if n < 0:
        raise ValueError("n must be positive number or zero.")
    # base case: 0! = 1
    if n == 0:
        return 1
    # recursive case: n! = n * (n-1)!
    if n > 0:
        return n * factorial(n - 1)
