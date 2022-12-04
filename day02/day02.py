import sys

ROCK, PAPER, SCISSORS = 1, 2, 3
BEATS = {ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER}
LOSES = {v: k for k, v in BEATS.items()}


def parse_input():
    decrypt_opponent = {"A": ROCK, "B": PAPER, "C": SCISSORS}
    decrypt_me = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}

    lines = sys.stdin.read().splitlines()
    plays = [l.split() for l in lines]
    return [(decrypt_opponent[o], decrypt_me[m]) for o, m in plays]


def score(a, b):
    if a == b:
        return a + 3
    if BEATS[a] == b:
        return a + 6

    return a


def play_to_pick(opponent, result):
    if result == ROCK:
        return BEATS[opponent]
    if result == PAPER:
        return opponent

    return LOSES[opponent]


def main():
    plays = parse_input()
    results = [score(m, o) for o, m in plays]
    print(sum(results))

    new_plays = [(o, play_to_pick(o, m)) for o, m in plays]
    new_results = [score(m, o) for o, m in new_plays]
    print(sum(new_results))


if __name__ == "__main__":
    main()
