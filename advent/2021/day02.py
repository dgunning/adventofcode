from advent.tools import *
from dataclasses import dataclass

Course = List[Instruction]


@dataclass
class Point:
    x: int
    y: int
    aim: int = None


def navigate(course: Course, loc: Point = Point(0, 0)):
    # Follow the course for the submarine and return the horizontal and vertical positions
    for direction, n in course:
        if direction == 'forward':
            loc.x += n
        elif direction == 'down':
            loc.y += n
        elif direction == 'up':
            loc.y -= n

    return loc


def day2_1(course: Course):
    loc = navigate(course)
    return loc.x * loc.y


def navigate_with_aim(course: Course, loc: Point = Point(0, 0, 0)):
    # Follow the course for the submarine and return the horizontal and vertical positions
    for direction, n in course:
        if direction == 'forward':
            loc.x += n
            loc.y += n * loc.aim
        elif direction == 'down':
            loc.aim += n
        elif direction == 'up':
            loc.aim -= n

    return loc


def day2_2(course: Course):
    loc = navigate_with_aim(course)
    return loc.x * loc.y


if __name__ == '__main__':
    in2: Course = data(2, atoms)
    test_course = [
        ('forward', 5),
        ('down', 5),
        ('forward', 8),
        ('up', 3),
        ('down', 8),
        ('forward', 2)
    ]
    with binding(**globals()):
        print(do(2, 1698735, 1594785890))
