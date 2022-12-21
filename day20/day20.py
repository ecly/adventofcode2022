import copy
import fileinput
import uuid


class IntWrapper:
    def __init__(self, value, idx):
        self.value = int(value)
        self.idx = idx
        self.hash = uuid.uuid4()

    def __eq__(self, o):
        return o.hash == self.hash

    def __repr__(self):
        return str(self.value)


def get_new_idx(idx, value, size):
    if value == 0:
        return idx

    new_idx = idx + value
    mod = size - 1

    if new_idx >= size:
        new_idx = new_idx % mod
    if new_idx < 0:
        new_idx = size - (abs(new_idx) % mod) - 1

    return new_idx


def mix(ns):
    for n in ns:
        idx = n.idx
        new_idx = get_new_idx(idx, n.value, len(ns))
        for nn in ns:
            if nn == n:
                continue

            if idx > nn.idx and new_idx <= nn.idx:
                nn.idx += 1
            elif idx < nn.idx and new_idx >= nn.idx:
                nn.idx -= 1

        n.idx = new_idx


def get_groves(ns):
    zero_idx = next(n.idx for n in ns if n.value == 0)
    grove_idx = [(zero_idx + g) % len(ns) for g in (1000, 2000, 3000)]
    groves = [n.value for n in ns if n.idx in grove_idx]
    return groves


def main():
    ns = [IntWrapper(l, i) for i, l in enumerate(fileinput.input())]

    ns1 = copy.deepcopy(ns)
    mix(ns1)
    print(sum(get_groves(ns1)))

    ns2 = copy.deepcopy(ns)
    for n in ns2:
        n.value *= 811589153

    for i in range(10):
        mix(ns2)

    print(sum(get_groves(ns2)))


if __name__ == "__main__":
    main()
