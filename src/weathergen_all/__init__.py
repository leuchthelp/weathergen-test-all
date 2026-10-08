import timeit

import numpy as np


def main() -> None:
    TEST = np.array([i %2 > 0 for i in range(10000)])

    tmp = TEST[:10]
    print(
        f"For list of {len(tmp)} bool - buildin all(): ",
        timeit.timeit(lambda: all(tmp)),
    )
    print(
        f"For list of {len(tmp)} bool - np.array().all(): ",
        timeit.timeit(lambda: tmp.all()),
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
        timeit.timeit(lambda: tmp.all()),
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
        timeit.timeit(lambda: tmp.all()),
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
        timeit.timeit(lambda: tmp.all()),
    )
    print(
        f"For list of {len(tmp)} bool - np.all(): ",
        timeit.timeit(lambda: np.all(tmp)),
    )
