import re
import sys
from copy import deepcopy


def pos_to_stack_id(pos):
    return 1 if pos == 1 else 1 + (pos - 1) // 4


def parse():
    input_ = sys.stdin.read()
    start_lines, move_lines = input_.split("\n\n")
    start_lines = start_lines.split("\n")
    stacks = {}
    for m in re.finditer(r"\d", start_lines[-1]):
        stack_id = pos_to_stack_id(m.start())
        stacks[stack_id] = []

    for line in start_lines[-1::-1]:
        for m in re.finditer("[A-Z]", line):
            stack_id = pos_to_stack_id(m.start())
            stacks[stack_id].append(m.group())

    moves = []
    for line in move_lines.strip().split("\n"):
        move = tuple(map(int, re.findall(r"\d+", line)))
        moves.append(move)

    return stacks, moves


def execute_part1(stacks, moves):
    stacks = deepcopy(stacks)
    for (quantity, from_, to) in moves:
        from_stack = stacks[from_]
        to_stack = stacks[to]
        for _ in range(quantity):
            to_stack.append(from_stack.pop())

    return stacks


def execute_part2(stacks, moves):
    stacks = deepcopy(stacks)
    for (quantity, from_, to) in moves:
        from_stack = stacks[from_]
        to_stack = stacks[to]

        chunk = [from_stack.pop() for _ in range(quantity)]
        to_stack.extend(chunk[::-1])

    return stacks


def get_top_crates(stacks):
    top_crates = []
    for s in sorted(stacks):
        top_crates.append(stacks[s][-1])

    return "".join(top_crates)


def main():
    stacks, moves = parse()

    rearranged_stacks_part1 = execute_part1(stacks, moves)
    print(get_top_crates(rearranged_stacks_part1))

    rearranged_stacks_part2 = execute_part2(stacks, moves)
    print(get_top_crates(rearranged_stacks_part2))


if __name__ == "__main__":
    main()
