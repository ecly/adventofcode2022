import fileinput
import random
from operator import add, eq, mul, sub, truediv

# lets try not to use eval today
_OP_MAP = {"+": add, "-": sub, "*": mul, "/": truediv, "==": eq}


def sign(x):
    return 0 if x == 0 else -1 if x < 0 else 1


class Monkey:
    def __init__(self, name: str, op: str, monkeys: dict):
        self.name = name
        self.op = int(op) if op.isdigit() else op
        self.monkeys = monkeys

    def yell(self):
        if isinstance(self.op, int):
            return self.op

        l_name, op_str, r_name = self.op.split()
        l = self.monkeys[l_name].yell()
        r = self.monkeys[r_name].yell()
        op = _OP_MAP[op_str]
        return op(l, r)


def parse_monkeys():
    monkeys = {}
    for line in fileinput.input():
        name, op = line.strip().split(": ")
        monkey = Monkey(name, op, monkeys)
        monkeys[name] = monkey

    return monkeys


def find_number_to_yell(monkeys):
    root = monkeys["root"]
    l_name, _, r_name = root.op.split()
    l_monkey, r_monkey = monkeys[l_name], monkeys[r_name]
    bad_monkey = monkeys["humn"]

    history = [(l_monkey.yell() - r_monkey.yell(), 0, bad_monkey.op)]
    inc = 1
    while abs(history[-1][0]) != 0:
        prev_op = bad_monkey.op
        bad_monkey.op += inc
        delta = l_monkey.yell() - r_monkey.yell()

        cfg = delta, inc, bad_monkey.op
        prev_delta = history[-1][0]
        if sign(delta) != sign(prev_delta):
            inc //= -2
            bad_monkey.op = prev_op
        elif abs(delta) > abs(prev_delta):
            inc //= 2
            bad_monkey.op = prev_op
        else:
            inc *= 2

        history.append(cfg)

    return bad_monkey.op


def main():
    monkeys = parse_monkeys()
    root = monkeys["root"]
    print(root.yell())

    # probably a bug in my code, but my code had
    # found an answer passing the test, but was too low.
    # my answer + 1, +2 and +3 would all pass the test,
    # but + 3 was the correct answer on the site
    print(find_number_to_yell(monkeys))


if __name__ == "__main__":
    main()
