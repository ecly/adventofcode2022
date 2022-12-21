import fileinput
from collections import defaultdict


def parse_grid2d():
    grid2d = defaultdict(set)
    for l in fileinput.input():
        x, y, z = map(int, l.split(","))
        grid2d[x, y].add(z)

    return grid2d


def count_exposed_sides_xy(grid2d, x, y):
    sides = 0
    ns = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    zs = grid2d[x, y]
    sides += sum((z - 1 not in zs) + (z + 1 not in zs) for z in zs)
    for dx, dy in ns:
        nx, ny = x + dx, y + dy
        nzs = grid2d[nx, ny]
        sides += len(zs.difference(nzs))

    return sides

def get_cube_surface_area(grid2d):
    exposed_sides = 0
    for x, y in list(grid2d):
        exposed_sides += count_exposed_sides_xy(grid2d, x, y)

    return exposed_sides

def get_air_bubble_surface_area(grid2d):
    sf = 0
    candidates = []
    for x, y in list(grid2d):
        zs = grid2d[x,y]
        if not zs:
            continue

        for z in set(range(min(zs), max(zs))).difference(zs):
            candidates.append((x,y,z))

    print(candidates)



def main():
    grid2d = parse_grid2d()
    surface_area = get_cube_surface_area(grid2d)
    print(surface_area)

    # TODO: part 2 not done yet
    air_bubble_surface_area = get_air_bubble_surface_area(grid2d)
    print(surface_area - air_bubble_surface_area)


main()
