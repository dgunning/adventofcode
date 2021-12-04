from rich import print
from advent.tools import *

"""
Giant Squid

At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case,
the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; 
in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get
 the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if 
you choose that board?


"""

BingoNumbers = List[str]
Board = List[List[str]]


def columns(matrix: List[List[object]]):
    for y in range(len(matrix[0])):
        yield [matrix[x][y] for x in range(len(matrix[0]))]


def wins(board: Board, called: List[str]):
    for row in board:
        if set(row).issubset(set(called)):
            print('Found winning board -> row {set(row) & set(called)}')
            return True
    for column in columns(board):
        if set(column).issubset(set(called)):
            print('Found winning board -> column {set(column) & set(called)}')
            return True


def board_score(board, called):
    return sum([sum([int(c)
                     for c in row if c not in called])
                for row in board])


def day4_1(puzzle_input):
    numbers, boards = puzzle_input
    for i in range(5, len(numbers)):
        called_numbers = numbers[:i + 1]
        for board in boards:
            if wins(board, called_numbers):
                winning_number = int(called_numbers[-1])
                return winning_number * board_score(board, called_numbers)


def day4_2(puzzle_input):
    numbers, boards = puzzle_input
    return None


def bingo_game(puzzle_input: List[List[str]]) -> Tuple[BingoNumbers, Board]:
    numbers = list(atoms(puzzle_input[0][0], sep=','))
    boards = [[list(map(int, row.split()))
               for row in raw_board]
              for raw_board in puzzle_input[1:]]
    print(f'There are {len(set(numbers))} numbers and {len(boards)} boards')
    return numbers, boards


if __name__ == '__main__':
    in4 = bingo_game(data(4, str.splitlines, sep='\n\n'))

    test_numbers = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    test_boards = [
                      [3, 15, 0, 2, 22],
                      [9, 18, 13, 17, 5],
                      [19, 8, 7, 25, 23],
                      [20, 11, 10, 24, 4],
                      [14, 21, 16, 12, 6]
                  ], [
                      [14, 21, 17, 24, 4],
                      [10, 16, 15, 9, 19],
                      [18, 8, 23, 26, 20],
                      [22, 11, 13, 6, 5],
                      [2, 0, 12, 3, 7]
                  ]

    print(day4_1((test_numbers, test_boards)))

    with binding(**globals()):
        print(do(4))
