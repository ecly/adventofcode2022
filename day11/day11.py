import copy
import re
import sys
from collections import deque
from dataclasses import dataclass
from functools import reduce
from math import gcd
from typing import Deque


@dataclass
class Monkey:
    idx: int
    items: Deque[int]
    eval_op: str
    test: int
    true: int
    false: int
    inspect_counter: int = 0

    def inspect(self, item, relief_divisor):
        # pylint: disable=unused-variable,eval-used
        # cheeky eval hacks
        old = item
        self.inspect_counter += 1
        worry_level = eval(self.eval_op) // relief_divisor
        return worry_level


def get_ints(line):
    return list(map(int, re.findall(r"\d+", line)))


def parse_monkeys():
    with open(sys.argv[1]) as f:
        monkey_strings = f.read().split("\n\n")

    monkeys = {}
    for monkey_string in monkey_strings:
        idx, items, op, test, true, false = monkey_string.strip().split("\n")
        monkey = Monkey(
            get_ints(idx)[0],
            deque(get_ints(items)),
            op.split(" = ")[1],
            get_ints(test)[0],
            get_ints(true)[0],
            get_ints(false)[0],
        )
        monkeys[monkey.idx] = monkey

    return monkeys


def play_round(monkeys, relief_divisor):
    for monkey in monkeys.values():
        while monkey.items:
            item = monkey.items.popleft()
            worry_level = monkey.inspect(item, relief_divisor)
            throw_to = monkey.true if worry_level % monkey.test == 0 else monkey.false
            monkeys[throw_to].items.append(worry_level)


def lcm(x, y):
    return x * y // gcd(x, y)


def truncate_worry_levels(monkeys, mod):
    for m in monkeys.values():
        m.items = deque([i % mod for i in m.items])


def get_monkey_business(monkeys, rounds, relief_divisor):
    monkeys = copy.deepcopy(monkeys)
    # we use the shared lcm to truncate worry levels to deal avoid slowing down
    # python with operations on huge numbers
    worry_level_mod = reduce(lcm, [m.test for m in monkeys.values()], 1)
    for _ in range(rounds):
        play_round(monkeys, relief_divisor)
        truncate_worry_levels(monkeys, worry_level_mod)

    ms = sorted(monkeys.values(), key=lambda m: m.inspect_counter)
    return ms[-1].inspect_counter * ms[-2].inspect_counter


def main():
    monkeys = parse_monkeys()
    print(get_monkey_business(monkeys, 20, 3))
    print(get_monkey_business(monkeys, 10000, 1))


if __name__ == "__main__":
    main()
