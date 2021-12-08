from advent.tools import *


def day8_1(puzzle_input: List[Tuple]):
    return sum([len([output
                     for output in outputs
                     if len(output) in [2, 3, 4, 7]])
                for signals, outputs in puzzle_input
                ])


def day8_2(puzzle_input: List[Tuple]):
    # Store the digits that we know the lengths of
    digit_length_map = {2: '1', 3: '7', 4: '4', 7: '8'}

    decoded_outputs = []
    for signals, outputs in puzzle_input:
        codes = {digit_length_map.get(len(o)): set(o)
                 for o in list(signals) + list(outputs)
                 if len(o) in digit_length_map
                 }

        digits = ''
        for output in outputs:
            outs = set(output)
            if len(output) == 5:
                if outs.issuperset(codes['7']):
                    # 3 contains all the segments in 7
                    digits += '3'
                elif outs.issuperset(codes['4'] - codes['1']):
                    # 5 contains the segents in 4 not in 1
                    digits += '5'
                else:
                    digits += '2'
            elif len(output) == 6:
                if outs.issuperset(codes['4']):
                    # 9 contains the segments in 4
                    digits += '9'
                elif len(outs & codes['1']) == 1:
                    # 6 contains one segment of 1
                    digits += '6'
                else:
                    digits += '0'
            else:
                digits += digit_length_map[len(outs)]

        decoded_outputs.append(int(digits))
    return sum(decoded_outputs)


if __name__ == '__main__':
    def parse_input(line):
        signal, _, output = line.partition(' | ')
        return atoms(signal), atoms(output)


    in8 = data(8, parse_input)

    with binding(**globals()):
        print(do(8))
