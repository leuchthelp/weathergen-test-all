import logging
import timeit
from collections.abc import Callable, Generator
from typing import NotRequired, TypedDict

import numpy as np
from pathos.multiprocessing import ProcessPool
from rich.logging import RichHandler

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()],
)
logger = logging.getLogger(__name__)


class Template(TypedDict):
    n: int
    func: Callable
    ctx: str
    pre_gen: NotRequired[list[bool] | Generator[bool]]


def printable(template: Template) -> str:
    arg = template["n"] if "pre_gen" not in template else template["pre_gen"]

    return (
        f"For list of {template['n']} bool per sample - {template['ctx']}: %f seconds"
        % timeit.timeit(lambda: template["func"](arg))
    )


def main() -> None:
    ns = [10, 100, 1000, 10_000, 20_000, 30_000]

    pre_gen_list_all = lambda pre_gen: all(pre_gen)
    pre_gen_list_numpy_all = lambda pre_gen: bool(np.array(pre_gen).all())
    pre_gen_list_all_numpy_on_array = lambda pre_gen: bool(np.all(np.array(pre_gen)))

    templates: list[Template] = []
    # Pre_gens as list
    for n in ns:
        pre_gen = [True for i in range(n)]

        template: Template = {
            "n": n,
            "ctx": "pre_gen as list - buildin all(...)",
            "func": pre_gen_list_all,
            "pre_gen": pre_gen,
        }
        templates.append(template)

        template = {
            "n": n,
            "ctx": "pre_gen as list - np.array(...).all()",
            "func": pre_gen_list_numpy_all,
            "pre_gen": pre_gen,
        }
        templates.append(template)

        template = {
            "n": n,
            "ctx": "pre_gen as list - np.all(np.array(...))",
            "func": pre_gen_list_all_numpy_on_array,
            "pre_gen": pre_gen,
        }
        templates.append(template)

    pool = ProcessPool()
    for out in pool.imap(printable, templates):
        logger.info(out)

    templates = []
    # Pre_gens as generator (generator cannot be pickled)
    for n in ns:
        pre_gen = (True for i in range(n))

        template: Template = {
            "n": n,
            "ctx": "pre_gen as generator - buildin all(...)",
            "func": pre_gen_list_all,
            "pre_gen": pre_gen,
        }
        templates.append(template)

        template = {
            "n": n,
            "ctx": "pre_gen as generator - np.array(...).all()",
            "func": pre_gen_list_numpy_all,
            "pre_gen": pre_gen,
        }
        templates.append(template)

        template = {
            "n": n,
            "ctx": "pre_gen as generator - np.all(np.array(...))",
            "func": pre_gen_list_all_numpy_on_array,
            "pre_gen": pre_gen,
        }
        templates.append(template)

    for template in templates:
        logger.info(printable(template))
