from advent.tools import *


@dataclass(frozen=True, eq=True)
class Dot:
    x: int
    y: int


class Paper:

    def __init__(self, dots: List[Dot], width: int = None, height: int = None):
        self.dots = dots
        self.width = width or max(dots, key=lambda d: d.x).x + 1
        self.height = height or max(dots, key=lambda d: d.y).y + 1

    def display(self):
        for y in range(self.height):
            row = ''.join(['#' if Dot(x, y) in self.dots else ' ' for x in range(self.width)])
            print(row)

        print('\n\n')

    def fold(self, at):
        axis, plane = at
        if axis == 'y':
            dots = {Dot(dot.x, plane - (dot.y - plane))
                    if dot.y > plane else dot
                    for dot in self.dots}
            return Paper(dots, width=self.width, height=self.height // 2)
        elif axis == 'x':
            dots = {Dot(plane - (dot.x - plane), dot.y)
                    if dot.x > plane else dot
                    for dot in self.dots}
            return Paper(dots, width=self.width // 2, height=self.height)

    def visible(self) -> int:
        return len(self.dots)

    def __repr__(self):
        return f"Paper width={self.width} height={self.height}"


def day13_1(puzzle_input):
    paper, folds = puzzle_input
    folded: Paper = paper.fold(at=folds[0])
    return folded.visible()


def day13_2(puzzle_input):
    paper, folds = puzzle_input
    for fold in folds:
        paper = paper.fold(at=fold)
    paper.display()
    return None


if __name__ == '__main__':
    dots, fold_str = data(13, sep='\n\n')
    paper = Paper(set([Dot(*mapt(int, dot.split(',')))
                       for dot in atoms(dots)]))

    folds = [(line[11:12], int(line[13:]))
             for line in atoms(fold_str, sep='\n')
             ]

    in13 = (paper, folds)
    with binding(**globals()):
        print(do(13))
