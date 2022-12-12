import fileinput
from collections import deque


def bfs_dist(grid, start, end):
    queue = deque([(start, [])])
    seen = set()
    while queue:
        node, path = queue.popleft()
        if node in seen:
            continue
        if node == end:
            return len(path)

        seen.add(node)
        height = grid[node]
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = node[0] + dx, node[1] + dy
            neighbor_height = grid.get(neighbor)
            if neighbor_height is None:
                continue
            if neighbor_height - height <= 1:
                queue.append((neighbor, path + [neighbor]))

    return float("inf")


def parse():
    grid = {}
    start, end = None, None
    for y, line in enumerate(fileinput.input()):
        for x, c in enumerate(line.strip()):
            if c == "S":
                start = x, y
                c = "a"
            elif c == "E":
                end = x, y
                c = "z"
            grid[x, y] = ord(c) - ord("a")

    return grid, start, end


def main():
    grid, start, end = parse()
    print(bfs_dist(grid, start, end))
    print(min(bfs_dist(grid, k, end) for k, v in grid.items() if v == 0))


if __name__ == "__main__":
    main()
