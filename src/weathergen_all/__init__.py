import timeit

import numpy as np


def main() -> None:
    n = 10
    print(
        f"For list of {n} bool - buildin all(): ",
        timeit.timeit(lambda: all(True for i in range(n))),
    )
    print(
        f"For list of {n} bool - np.array().all(): ",
        timeit.timeit(lambda: np.array(True for i in range(n)).all()),
    )
    print(
        f"For list of {n} bool - np.all(): ",
        timeit.timeit(lambda: np.all(np.array(True for i in range(n)))),
    )

    n = 100
    print(
        f"For list of {n} bool - buildin all(): ",
        timeit.timeit(lambda: all(True for i in range(n))),
    )
    print(
        f"For list of {n} bool - np.array().all(): ",
        timeit.timeit(lambda: np.array(True for i in range(n)).all()),
    )
    print(
        f"For list of {n} bool - np.all(): ",
        timeit.timeit(lambda: np.all(np.array(True for i in range(n)))),
    )

    n = 1000
    print(
        f"For list of {n} bool - buildin all(): ",
        timeit.timeit(lambda: all(True for i in range(n))),
    )
    print(
        f"For list of {n} bool - np.array().all(): ",
        timeit.timeit(lambda: np.array(True for i in range(n)).all()),
    )
    print(
        f"For list of {n} bool - np.all(): ",
        timeit.timeit(lambda: np.all(np.array(True for i in range(n)))),
    )

    n = 10000
    print(
        f"For list of {n} bool - buildin all(): ",
        timeit.timeit(lambda: all(True for i in range(n))),
    )
    print(
        f"For list of {n} bool - np.array().all(): ",
        timeit.timeit(lambda: np.array(True for i in range(n)).all()),
    )
    print(
        f"For list of {n} bool - np.all(): ",
        timeit.timeit(lambda: np.all(np.array(True for i in range(n)))),
    )
