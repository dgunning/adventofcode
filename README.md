# Advent of Code

In this repo I implement the solutions to Google Advent of Code competition.

## References
The solutions are influenced by Peter Norvig's solutions from 2020. You will find his core library in the file *advent/pytudes.py*

# Solutions

## Day 1


## Day 2

## Day 3

## Day 4

## Day 5

Given a list of lines e.g. count how many points on the line overlap. 
A line is specified as a pair of points e.g. **645,570** -> **517,570**

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