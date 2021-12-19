from advent.tools import *
from collections import defaultdict


def count_paths_to_end(cave, visited_caves, one_off):
    if cave == 'end':
        return 1
    if cave.islower():
        visited_caves.add(cave)
    total = sum(count_paths_to_end(next_cave, visited_caves, one_off)
                for next_cave in paths[cave]
                if next_cave not in visited_caves)
    if one_off == ' ':
        total += sum(count_paths_to_end(next_cave, visited_caves, next_cave)
                     for next_cave in paths[cave]
                     if next_cave in visited_caves and next_cave != 'start'
                     )
    if cave != one_off:
        visited_caves.discard(cave)
    return total


def day12_1(in12):
    return count_paths_to_end('start', set(), '')


def day12_2(in12):
    return count_paths_to_end('start', set(), ' ')


if __name__ == '__main__':
    paths = in12 = defaultdict(list)
    for cave1, cave2 in [l.split('-') for l in data(12)]:
        paths[cave1].append(cave2)
        paths[cave2].append(cave1)

    with binding(**globals()):
        print(do(12))
    # in12 = mapt(lambda l: tuple(l.split('-')), data(12))
    # print(in12)
