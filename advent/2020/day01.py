from advent.tools import *


def day_1_1(nums):
    "Find 2 distinct numbers that sum to 2020 and return their product"
    return first(x * y
                 for x in nums
                 for y in nums & {2020 - x}
                 if x != y)


def day_1_2(nums):
    "Find 3 distinct numbers that sum to 2020, and return their product."
    return first(x * y * z
                 for x, y in combinations(nums, 2)
                 for z in nums & {2020 - x - y}
                 if x != z != y)


if __name__ == '__main__':
    in1: Set[int] = set(data(1, int))
    print(day_1_1(in1))
    print(day_1_2(in1))
