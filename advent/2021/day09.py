from advent.tools import *
import math

# credit to https://www.reddit.com/user/4HbQ/


def neighbours(x, y):
    return filter(lambda n: n in heights,  # remove points
                  [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)])  # outside grid


def is_low_point(point):
    return all(heights[point] < heights[n]
               for n in neighbours(*point))


def day9_1(heights):
    return sum([heights[point] + 1
                for point in heights
                if is_low_point(point)])


def day9_2(height):
    def count_basin(p):
        if height[p] == 9: return 0  # stop counting at ridge
        del height[p]  # prevent further visits
        return 1 + sum(map(count_basin, neighbours(*p)))

    basins = [count_basin(p) for p in low_points]
    return math.prod(sorted(basins)[-3:])


if __name__ == '__main__':
    in9 = heights = {(x, y): int(h)
                     for y, l in enumerate(data(9))
                     for x, h in enumerate(l.strip())
                     }
    low_points = list(filter(is_low_point, heights))

    with binding(**globals()):
        print(do(9))
