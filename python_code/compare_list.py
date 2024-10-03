from example_module import get_all_numbers
import timeit


def get_all_numbers_python(n: int) -> list[int]:
    return list(range(n))


def main():
    # Time compute_fibonacci_python vs compute_fibonacci using the timeit module
    n = int(10e6)

    t1 = timeit.timeit(
        f"get_all_numbers_python({n})",
        globals=globals(),
        number=1
    )
    print(f"Python took: {t1}s")

    t2 = timeit.timeit(
        f"get_all_numbers({n})",
        globals=globals(),
        number=1
    )
    print(f"Rust took: {t2}s")

    print(f"Rust was {t1 / t2:.2f} times faster than Python")


if __name__ == "__main__":
    main()