import sys
from functools import cmp_to_key


def parse_pairs():
    with open(sys.argv[1] if len(sys.argv) > 1 else "input") as f:
        pairs = f.read().strip().split("\n\n")

    pairs = [tuple(map(eval, p.split("\n"))) for p in pairs]
    return pairs


def is_pair_in_right_order(fst, snd):
    if isinstance(fst, int) and isinstance(snd, int):
        return 0 if fst == snd else -1 if fst < snd else 1
    if isinstance(fst, int):
        return is_pair_in_right_order([fst], snd)
    if isinstance(snd, int):
        return is_pair_in_right_order(fst, [snd])

    for p in zip(fst, snd):
        r = is_pair_in_right_order(*p)
        if r:
            return r

    return 0 if len(fst) == len(snd) else -1 if len(fst) < len(snd) else 1


def main():
    pairs = parse_pairs()
    right_order_idx = []
    for idx, p in enumerate(pairs, 1):
        if is_pair_in_right_order(*p) == -1:
            right_order_idx.append(idx)

    print(sum(right_order_idx))

    packets = [packet for pair in pairs for packet in pair]
    dp1, dp2 = [[2]], [[6]]
    packets.extend([dp1, dp2])
    sorted_packets = sorted(packets, key=cmp_to_key(is_pair_in_right_order))
    decoder_key = (sorted_packets.index(dp1) + 1) * (sorted_packets.index(dp2) + 1)
    print(decoder_key)


if __name__ == "__main__":
    main()
