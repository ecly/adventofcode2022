import sys


def sign(i):
    return 0 if i == 0 else 1 if i > 0 else -1


class Knot:
    def __init__(self, tail=None):
        self.tail = tail
        self.x, self.y = 0, 0
        self.visited = {(self.x, self.y)}

    def move(self, dx, dy, steps=1):
        for _ in range(steps):
            self.x += dx
            self.y += dy
            self.visited.add((self.x, self.y))
            if self.tail:
                self.tail.chase(self.x, self.y)

    def chase(self, hx, hy):
        htdx, htdy = hx - self.x, hy - self.y

        # we are still touching
        if abs(htdx) <= 1 and abs(htdy) <= 1:
            return

        tdx, tdy = sign(htdx), sign(htdy)
        self.move(tdx, tdy)


def solve(knots, moves):
    directions = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}
    for direction, steps in moves:
        dx, dy = directions[direction]
        knots[0].move(dx, dy, steps)

    return knots[-1].visited


def get_knots(count):
    knots = []
    for _ in range(0, count):
        tail = knots[-1] if knots else None
        knots.append(Knot(tail))

    return knots[::-1]


def parse_moves():
    moves = []
    for line in sys.stdin:
        direction, steps = line.split()
        moves.append((direction, int(steps)))

    return moves


def main():
    moves = parse_moves()
    knots1 = get_knots(2)
    visited1 = solve(knots1, moves)
    print(len(visited1))

    knots2 = get_knots(10)
    visited2 = solve(knots2, moves)
    print(len(visited2))


if __name__ == "__main__":
    main()
