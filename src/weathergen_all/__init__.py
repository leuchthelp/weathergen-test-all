import timeit

import numpy as np


def main() -> None:
    TEST = [True for _ in range(10000)]

    tmp = TEST[:10]
    print(
        f"For list of {len(tmp)} bool - buildin all(): ",
        timeit.timeit(lambda: all(tmp)),
    )
    print(
        f"For list of {len(tmp)} bool - np.array().all(): ",
        timeit.timeit(lambda: np.array(tmp).all()),
    )
    print(
        f"For list of {len(tmp)} bool - np.all(): ",
        timeit.timeit(lambda: np.all(tmp)),
    )

    tmp = TEST[:100]
    print(
        f"For list of {len(tmp)} bool - buildin all(): ",
        timeit.timeit(lambda: all(tmp)),
    )
    print(
        f"For list of {len(tmp)} bool - np.array().all(): ",
        timeit.timeit(lambda: np.array(tmp).all()),
    )
    print(
        f"For list of {len(tmp)} bool - np.all(): ",
        timeit.timeit(lambda: np.all(tmp)),
    )

    tmp = TEST[:1000]
    print(
        f"For list of {len(tmp)} bool - buildin all(): ",
        timeit.timeit(lambda: all(tmp)),
    )
    print(
        f"For list of {len(tmp)} bool - np.array().all(): ",
        timeit.timeit(lambda: np.array(tmp).all()),
    )
    print(
        f"For list of {len(tmp)} bool - np.all(): ",
        timeit.timeit(lambda: np.all(tmp)),
    )

    tmp = TEST
    print(
        f"For list of {len(tmp)} bool - buildin all(): ",
        timeit.timeit(lambda: all(tmp)),
    )
    print(
        f"For list of {len(tmp)} bool - np.array().all(): ",
        timeit.timeit(lambda: np.array(tmp).all()),
    )
    print(
        f"For list of {len(tmp)} bool - np.all(): ",
        timeit.timeit(lambda: np.all(tmp)),
    )
