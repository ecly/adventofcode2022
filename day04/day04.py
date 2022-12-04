import sys


def parse(line):
    f, s = line.split(",")
    fl, fh = map(int, f.split("-"))
    sl, sh = map(int, s.split("-"))
    return fl, fh, sl, sh


def main():
    lines = sys.stdin.read().splitlines()
    contained = 0
    overlap = 0
    for line in lines:
        fl, fh, sl, sh = parse(line)
        s1 = set(range(fl, fh + 1))
        s2 = set(range(sl, sh + 1))
        if s1.issubset(s2) or s2.issubset(s1):
            contained += 1
        if s1 & s2:
            overlap += 1

    print(contained)
    print(overlap)


if __name__ == "__main__":
    main()
