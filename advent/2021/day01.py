from advent.tools import *


def day1_1(nums):
    """How many measurements are larger than the previous measurement?"""
    return quantify(map(lambda i: nums[i] > nums[i - 1],
                        range(1, len(nums))
                        )
                    )


def day1_2(nums):
    "How many sliding window sums are greater than the previous"
    return quantify(map(lambda i:
                        sum(nums[i - 3:i]) > sum(nums[i - 4: i - 1]),
                        range(4, len(nums) + 1)
                        )
                    )


if __name__ == '__main__':
    in1: Set[int] = list(data(1, int))
    print(do(1, globals()))