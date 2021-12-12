from advent.tools import *
from statistics import median

scores = {')': 3, '}': 1197, '>': 25137, ']': 57}
open_close = {'(': ')', '{': '}', '<': '>', '[': ']'}


def parse_syntax(line) -> Tuple[int, str]:
    stack = ['']
    for c in line:
        if c == stack[-1]:
            stack.pop()
        elif c in open_close:
            stack.append(open_close[c])
        else:
            return scores[c], cat(reversed(stack))
    return 0, cat(reversed(stack))


def day10_1(in10):
    return sum(parse_syntax(line)[0] for line in in10)


def day10_2(lines):
    bracket_trans = str.maketrans(')]}>', '1234')

    return median(int(completion.translate(bracket_trans), base=5)
                  for e, completion in map(parse_syntax, lines)
                  if e == 0)


if __name__ == '__main__':
    in10 = data(10)

    with binding(**globals()):
        print(do(10))
