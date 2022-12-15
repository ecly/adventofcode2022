import fileinput
import itertools


def parse_rocks():
    sign = lambda x: 0 if not x else -1 if x < 0 else 1

    rocks = {}
    for line in fileinput.input():
        paths = line.strip().split(" -> ")
        for lp, hp in zip(paths, paths[1:]):
            lx, ly = map(int, lp.split(","))
            hx, hy = map(int, hp.split(","))
            dx = sign(hx - lx) or 1
            dy = sign(hy - ly) or 1
            for x in range(lx, hx + dx, dx):
                for y in range(ly, hy + dy, dy):
                    rocks[x, y] = True

    return rocks


def grain_fall(rocks, max_y):
    sx, sy = 500, 0
    while True:
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            nx, ny = sx + dx, sy + dy
            if (nx, ny) not in rocks and ny < max_y:
                sx, sy = nx, ny
                break
        else:
            return sx, sy


def pour_sand(rocks):
    max_y_rock = max(y for _, y in rocks)
    max_y_floor = max_y_rock + 2
    p1, p2 = None, None
    for sands in itertools.count():
        sx, sy = grain_fall(rocks, max_y_floor)
        if not p1 and sy >= max_y_rock:
            p1 = sands
        if (sx, sy) == (500, 0):
            p2 = sands + 1
            break

        rocks[sx, sy] = True

    return p1, p2


def main():
    rocks = parse_rocks()
    print(*pour_sand(rocks), sep="\n")


if __name__ == "__main__":
    main()
