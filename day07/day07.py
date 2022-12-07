import sys
from collections import defaultdict, deque
from pathlib import PosixPath


def parse_dirs():
    dirs = defaultdict(list)
    current_dir = PosixPath()
    for line in sys.stdin:
        tokens = line.split()
        if tokens[0] == "$":
            if tokens[1] == "ls":
                continue

            current_dir = (current_dir / tokens[2]).resolve()
        else:
            name = current_dir / tokens[1]
            size = None if tokens[0] == "dir" else int(tokens[0])
            dirs[current_dir].append((name, size))

    return dirs


def get_dir_sizes(dirs):
    sizes = defaultdict(int)
    queue = deque([PosixPath("/")])
    while queue:
        dir_path = queue.popleft()
        dir_size = 0
        for child_path, size in dirs[dir_path]:
            if size is None:
                queue.append(child_path)
            else:
                dir_size += size

        sizes[dir_path] += dir_size
        for parent in dir_path.parents:
            sizes[parent] += dir_size

    return sizes


def main():
    dirs = parse_dirs()
    sizes = get_dir_sizes(dirs)
    print(sum(size for size in sizes.values() if size < 100000))

    free_space = 70000000 - sizes[PosixPath("/")]
    needed_free = 30000000
    print(min(v for v in sizes.values() if free_space + v > needed_free))


if __name__ == "__main__":
    main()
