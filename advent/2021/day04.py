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
            return True
    for column in columns(board):
        if set(column).issubset(set(called)):
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
    winning_boards = set()
    for i in range(5, len(numbers)):
        called_numbers = numbers[:i + 1]
        for board_number, board in enumerate(boards):
            if board_number in winning_boards:
                continue
            if wins(board, called_numbers):
                winning_number = int(called_numbers[-1])
                winning_boards.add(board_number)
                if len(winning_boards) == 100:
                    final_board = boards[board_number]
                    final_score = winning_number * board_score(final_board, called_numbers)
                    return final_score
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
    with binding(**globals()):
        print(do(4, 60368, 17435))
