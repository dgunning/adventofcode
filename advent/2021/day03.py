from advent.tools import *
from collections import Counter


def most_common(bits: List[int], pos, check_equals: bool = False):
    common_count = Counter([bit[pos] for bit in bits]).most_common()
    if (check_equals
            and common_count[0][1] == common_count[1][1]):
        return '1'
    else:
        return common_count[0][0]


def day3_1(nums):
    width = len(nums[0])
    gamma = ''.join([most_common(nums, i) for i in range(width)])
    epsilon = ''.join('1' if x == '0' else '0' for x in gamma)
    return int(gamma, 2) * int(epsilon, 2)


def day3_2(nums):
    width = len(nums[0])
    oxy_list, co2_list = nums, nums
    o2_rating, co2_rating = None, None

    for i in range(width):
        most_common_digit = most_common(oxy_list, i, check_equals=True)
        if len(oxy_list) > 1:
            oxy_list = [d for d in oxy_list if d[i] == most_common_digit]
        if len(oxy_list) == 1:
            o2_rating = oxy_list[0]
            break

    for i in range(width):
        least_common_digit = '1' if most_common(co2_list, i, check_equals=True) == '0' else '0'
        if len(co2_list) > 1:
            co2_list = [d for d in co2_list if d[i] == least_common_digit]
        if len(co2_list) == 1:
            co2_rating = co2_list[0]
            break

    return int(o2_rating, 2) * int(co2_rating, 2)


if __name__ == '__main__':
    in3 = data(3)
    test_input = ['00100',
                  '11110',
                  '10110',
                  '10111',
                  '10101',
                  '01111',
                  '00111',
                  '11100',
                  '10000',
                  '11001',
                  '00010',
                  '01010']
    # print(day3_2(test_input))
    with binding(**globals()):
        print(do(3, 2972336, 3368358))
