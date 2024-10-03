from example_module import compute_fibonacci
import timeit


def fibonacci(n: int, memo: dict[int, int]):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


def compute_fibonacci_python(n):
    memo = {}
    result = fibonacci(n, memo)
    return result


def main():
    # Time compute_fibonacci_python vs compute_fibonacci using the timeit module
    n = 980

    t1 = timeit.timeit(
        f"compute_fibonacci_python({n})",
        globals=globals(),
        number=1000
    )
    print(f"Python took: {t1}s")

    t2 = timeit.timeit(
        f"compute_fibonacci({n})",
        globals=globals(),
        number=1000
    )
    print(f"Rust took: {t2}s")

    print(f"Rust was {t1 / t2:.2f} times faster than Python")


if __name__ == "__main__":
    main()