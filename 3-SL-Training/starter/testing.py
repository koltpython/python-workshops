def fibonacci(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    if not isinstance(n, int):
        raise ValueError("n must be exact integer")
    if n + 1 == n:
        raise OverflowError("n too large")

    if n == 0:
        return 0

    pass
