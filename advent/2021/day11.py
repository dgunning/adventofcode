from advent.tools import *


def neighbours(x, y):
    return filter(lambda p: p in energy and p != (x, y),
                  [(n, m)
                   for n in range(x - 1, x + 2)
                   for m in range(y - 1, y + 2)]
                  )


def step_and_count(energy):
    flash = []
    for p in energy:
        energy[p] += 1
        if energy[p] == 10:
            flash.append(p)
    count = 0
    while len(flash) > 0:
        count += len(flash)
        next_flash = []
        for p in flash:
            for n in neighbours(*p):
                energy[n] += 1
                if energy[n] == 10:
                    next_flash.append(n)
        flash = next_flash
    for p in energy:
        if energy[p] > 9:
            energy[p] = 0
    return count


def day11_1(energy):
    return sum([step_and_count(energy) for i in range(100)])


def day11_2(energy):
    rows, cols = max(k[0] for k in energy) + 1, max(k[1] for k in energy) + 1
    steps = 100
    while True:
        steps += 1
        if step_and_count(energy) == rows * cols:
            break
    return steps


if __name__ == '__main__':
    in11 = energy = {(x, y): int(h)
                     for y, l in enumerate(data(11))
                     for x, h in enumerate(l.strip())
                     }
    with binding(**globals()):
        print(do(11))

# print(list(neighbours(2, 2)))
# print(energy)
