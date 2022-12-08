import itertools
import sys


def get_visible_from_outside_in_line(line):
    visible = [line[0]]
    for tree in line[1:]:
        if tree[-1] > visible[-1][-1]:
            visible.append(tree)

    return visible


def get_visible_trees_from_tree_in_line(line):
    height = line[0][-1]
    visible = []
    for tree in line[1:]:
        visible.append(tree)
        if tree[-1] >= height:
            break

    return visible


def get_scenic_score_for_tree(tree, rows, columns):
    (i, j), _ = tree

    up = columns[j][i::-1]
    left = rows[i][j:]
    right = rows[i][j::-1]
    down = columns[j][i:]

    scenic_score = 1
    all_visible_trees = set()
    for line in [up, left, down, right]:
        visible_trees = get_visible_trees_from_tree_in_line(line)
        all_visible_trees.update(visible_trees)
        scenic_score *= len(visible_trees)

    return scenic_score, all_visible_trees


def get_max_scenic_score(rows):
    columns = list(zip(*rows))

    return max(
        get_scenic_score_for_tree(t, rows, columns)
        for t in itertools.chain.from_iterable(rows)
    )


def get_visible_trees(rows):
    columns = list(zip(*rows))
    grids = [rows, columns]
    visible_trees = set()

    for grid in grids:
        for l in grid:
            fwd_trees = get_visible_from_outside_in_line(l)
            bwd_trees = get_visible_from_outside_in_line(l[::-1])
            visible_trees.update(fwd_trees + bwd_trees)

    return visible_trees


def parse_grid():
    grid = []
    for i, line in enumerate(sys.stdin.read().splitlines()):
        row = []
        for j, c in enumerate(line):
            height = int(c)
            row.append(((i, j), height))

        grid.append(row)

    return grid


def visualize(grid, visible_trees):
    """Utility function for visualizing a set of visible trees on a grid."""
    for row in grid:
        for tree in row:
            sys.stdout.write("X" if tree in visible_trees else str(tree[-1]))
        print()


def main():
    grid = parse_grid()
    visible_trees = get_visible_trees(grid)
    print(len(visible_trees))

    scenic_score, _ = get_max_scenic_score(grid)
    print(scenic_score)


if __name__ == "__main__":
    main()
