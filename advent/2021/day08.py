from advent.tools import *


def day8_1(puzzle_input: List[Tuple]):
    return sum([len([output
                     for output in outputs
                     if len(output) in [2, 3, 4, 7]])
                for signals, outputs in puzzle_input
                ])


def get_digits(output):
    return None


def day8_2(puzzle_input: List[Tuple]):
    signals = {'abcdefg': 8, 'bcdef': 5, 'acdfg': 2, 'abcdf': 3, 'abd': 7, 'abcdef': 9, 'bcdefg': 6, 'abef': 4,
               'abcdeg': 0, 'ab': 1}
    result = [[signals.get(''.join(sorted(output)))
               for output in outputs]
              for signals, outputs in puzzle_input
              ]
    return None


def parse_input(line):
    signal, _, output = line.partition(' | ')
    return atoms(signal), atoms(output)


if __name__ == '__main__':
    in8 = data(8, parse_input)

    test_input = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
    """
    testlines = list(tuple(map(parse_input, [line for line in test_input.split('\n') if line])))
    print(day8_2(testlines))

    """
    with binding(**globals()):
        print(do(8))
    """
