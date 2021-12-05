# Advent of Code

In this repo I implement the solutions to Google Advent of Code competition.

## References
The solutions are influenced by Peter Norvig's solutions from 2020. You will find his core library in the file *advent/pytudes.py*

# Solutions

## Day 1
Given a list of integers, count how many integers are larger than the previous one.

For **part 1** the solution is just looking at each number and comparing it with the previous number.

For **part 2** the solution is for each number looking back at a window of size 3.
```python
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
```

## Day 2
Given a series of navigation directions, find the final position of the submarine.

```python
Instruction = Tuple[str, int]
Course = List[Instruction]

```
Then we navigate the course and return the multiplication of the final height and depth

```python
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
```
For part 2 the navigation changes to account for the **aim** of the submarine.

```python
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
```

## Day 3
Given a list of binary inputs find the most and least common bits in each position.

```python
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
```

Part 2 involves filtering by *most* and *least* common, 
then using the remaining to generate the answer
```python
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
```
## Day 4

## Day 5

Given a list of lines e.g. count how many points on the line overlap. 

A line is specified as a pair of points 

e.g. **645,570** -> **517,570**

The easiest way to model the problem is as a **Line** class composed of a pair of **Point**s
```python
@dataclass(frozen=True, eq=True, order=True)
class Point:
    x: int
    y: int


@dataclass(frozen=True, eq=True)
class Line:
    start: Point
    stop: Point
```
Then the **Line** class implements the function property points as follows
```python
 @cached_property
    def points(self):
        if self.horizontal:
            return [Point(x, self.start.y)
                    for x in range(min([self.start.x, self.stop.x]),
                                   max([self.start.x, self.stop.x]) + 1)
                    ]
        elif self.vertical:
            return [Point(self.start.x, y)
                    for y in range(min([self.start.y, self.stop.y]),
                                   max([self.start.y, self.stop.y]) + 1)
                    ]

        else:
            sorted_points = sorted([self.start, self.stop], key=lambda p: p.x)
            y_step = 1 if sorted_points[0].y < sorted_points[1].y else -1
            y = sorted_points[0].y
            points = list()
            for x in range(sorted_points[0].x, sorted_points[1].x + 1):
                point = Point(x, y)
                points.append(point)
                y += y_step

            return points

```
Then the solution is just counting how may points overlap. For this we use a **Counter**
after filtering for horizontal and vertical lines, for part 1.

```python
def day5_1(vents):
    return quantify(Counter([point
                             for line in vents
                             for point in line.points
                             if (line.horizontal or line.vertical)
                             ]).items(),
                    lambda item: item[1] > 1
                    )

```
For part 2, we do the same without filtering.

```python
def day5_2(vents):
    return quantify(Counter([point
                             for line in vents
                             for point in line.points
                             ]).items(),
                    lambda item: item[1] > 1
                    )
```