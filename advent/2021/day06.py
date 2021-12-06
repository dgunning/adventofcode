from advent.tools import *
from copy import copy
from collections import defaultdict
from typing import Dict


def simulate(timers, days=80):
    day_counts = dict(Counter(timers))

    day = 0
    while day < days:
        next_day_counts: Dict[int, int] = defaultdict(int)
        for f in range(1, 9):
            next_day_counts[f - 1] += day_counts.get(f, 0)
        next_day_counts[6] += day_counts.get(0, 0)
        next_day_counts[8] += day_counts.get(0, 0)

        day_counts = copy(next_day_counts)
        day += 1
    return sum(list(day_counts.values()))


def day6_1(timers):
    return simulate(timers, 80)


def day6_2(timers):
    return simulate(timers, 256)


if __name__ == '__main__':
    in6 = data(6, int, sep=',')

    with binding(**globals()):
        print(do(6))
