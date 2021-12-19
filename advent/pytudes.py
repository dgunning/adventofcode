import itertools
import operator
import re
from contextlib import contextmanager
from functools import reduce
from itertools import chain, combinations
from collections import Set
from typing import Tuple, List, Union


def test_data(test_input: str, parser=str, sep='\n') -> list:
    "Split the test data into sections separated by `sep`, and apply `parser` to each"
    sections = test_input.strip().split(sep)
    return list(map(parser, sections))


def data(day: int, parser=str, sep='\n') -> list:
    "Split the day's input file into sections separated by `sep`, and apply `parser` to each."
    with open(f'input/day{day:02}.txt') as f:
        sections = f.read().rstrip().split(sep)
        return list(map(parser, sections))


def do(day, *answers) -> List[int]:
    "E.g., do(3) returns [day3_1(in3), day3_2(in3)]. Verifies `answers` if given."
    g = globals()
    got = []
    for part in (1, 2):
        fname = f'day{day}_{part}'
        if fname in g:
            got.append(g[fname](g[f'in{day}']))
            if len(answers) >= part:
                assert got[-1] == answers[part - 1], (
                    f'{fname}(in{day}) got {got[-1]}; expected {answers[part - 1]}')
        else:
            got.append(None)
    return got


@contextmanager
def binding(**kwds):
    """
    Bind global variables within a context; revert to old values on exit.
    This is needed if the do() function is called from another module. Here is how it needs to be called

    with binding(**globals()):
        part1, part2 = do(1)
    """
    old_values = {k: globals()[k] for k in kwds if k in globals()}
    try:
        globals().update(kwds)
        yield  # Stuff within the context gets run here.
    finally:
        globals().update(old_values)


Number = Union[float, int]
Atom = Union[Number, str]
Char = str  # Type used to indicate a single character
_s: Set = None
cat = ''.join
flatten = chain.from_iterable


def quantify(iterable, pred=bool) -> int:
    "Count the number of items in iterable for which pred is true."
    return sum(1 for item in iterable if pred(item))


def first(iterable, default=None) -> object:
    "Return first item in iterable, or default."
    return next(iter(iterable), default)


def prod(numbers) -> Number:
    "The product of an iterable of numbers."
    return reduce(operator.mul, numbers, 1)


def dot(A, B) -> Number:
    "The dot product of two vectors of numbers."
    return sum(a * b for a, b in zip(A, B))


def ints(text: str) -> Tuple[int]:
    "Return a tuple of all the integers in text."
    return mapt(int, re.findall('-?[0-9]+', text))


def lines(text: str) -> List[str]:
    "Split the text into a list of lines."
    return text.strip().splitlines()


def mapt(fn, *args):
    "Do map(fn, *args) and make the result a tuple."
    return tuple(map(fn, *args))


def atoms(text: str, ignore=r'', sep=None) -> Tuple[Union[int, str]]:
    "Parse text into atoms separated by sep, with regex ignored."
    text = re.sub(ignore, '', text)
    return mapt(atom, text.split(sep))


def atom(text: str, types=(int, str)):
    "Parse text into one of the given types."
    for typ in types:
        try:
            return typ(text)
        except ValueError:
            pass


def transpose(lst: List[List[object]], fillvalue=None):
    "Transpose a list of lists"
    return list(map(list, itertools.zip_longest(*lst, fillvalue=fillvalue)))
