import sys
from collections import defaultdict

cycles = defaultdict(list)
cycle = 0
for line in sys.stdin:
    match line.strip().split():
        case ["noop"]:
            cycle += 1
            cycles[cycle].append(None)
        case ["addx", x]:
            cycle += 2
            cycles[cycle].append(int(x))

register = 1
cycle_to_value = {}
for i in range(1, max(cycles.keys()) + 1):
    ops = cycles[i]
    cycle_to_value[i] = register

    for op in ops:
        if isinstance(op, int):
            register += op

print(sum(i * cycle_to_value[i] for i in (20, 60, 100, 140, 180, 220)))


for i in range(1, max(cycles.keys()) + 1):
    sprite_pos = cycle_to_value.get(i)
    draw_pos = (i - 1) % 40
    is_visible = abs(sprite_pos - draw_pos) <= 1
    print("#" if is_visible else ".", end="")
    if i % 40 == 0:
        print()
