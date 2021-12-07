from advent.tools import *
from statistics import mean, median


def day7_1(positions):
    target = max((len(positions) // 2) + 1, int(mean(positions)) + 1)
    return min([
        sum([abs(crab - p)
             for crab in positions]
            )
        for p in range(min(positions), target)])


def day7_2(positions):
    target = max((len(positions) // 2) + 1, int(mean(positions)) + 1)
    return min([
        sum([sum(range(abs(crab - p) + 1))
             for crab in positions]
            )
        for p in range(min(positions), target)]
    )


if __name__ == '__main__':
    in7 = data(7, int, sep=',')

    test_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    with binding(**globals()):
        print(do(7))
