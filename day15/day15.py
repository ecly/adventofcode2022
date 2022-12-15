import fileinput
import itertools
import re


def parse_sensors():
    sensors = {}
    for line in fileinput.input():
        sx, sy, bx, by = map(int, re.findall(r"-?\d+", line))
        sensors[sx, sy] = bx, by

    return sensors


def manhatten(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def cannot_contain_beacon(sensors, x, y) -> bool:
    return any(mh >= manhatten(x, y, sx, sy) for sx, sy, mh in sensors)


def get_not_beacon_count_for_row(sensors, beacons, row):
    max_dist = max(mh for _, _, mh in sensors)
    min_x = min(x for x, _, _ in list(sensors)) - max_dist
    max_x = max(x for x, _, _ in list(sensors)) + max_dist
    return sum(
        cannot_contain_beacon(sensors, x, row) and (x, row) not in beacons
        for x in range(min_x, max_x)
    )


def get_circumference(x, y, md):
    md += 1
    for i in range(md):
        for dx, dy in itertools.product([md - i, -md + i], [i, -i]):
            yield x + dx, y + dy


def get_undetected_beacon(sensors, max_coord):
    for x, y, md in sensors:
        for cx, cy in get_circumference(x, y, md):
            if not (0 <= cx <= max_coord and 0 <= cy <= max_coord):
                continue
            if not cannot_contain_beacon(sensors, cx, cy):
                return cx, cy


def main():
    # 13s for both with pypy3 (7.3.9)
    # 113s for both with python (3.10.18)
    sensor_to_beacon = parse_sensors()
    beacons = set(sensor_to_beacon.values())
    sensors = [
        (x, y, manhatten(x, y, bx, by)) for (x, y), (bx, by) in sensor_to_beacon.items()
    ]
    y = 2_000_000
    print(get_not_beacon_count_for_row(sensors, beacons, y))
    x, y = get_undetected_beacon(sensors, y * 2)
    print(x * 4_000_000 + y)


if __name__ == "__main__":
    main()
