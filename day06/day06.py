def solve(series, marker_size):
    for i in range(len(series) - marker_size):
        marker_idx = i + marker_size
        chunk = series[i:marker_idx]
        if len(set(chunk)) == marker_size:
            return marker_idx


def main():
    series = input().strip()
    print(solve(series, 4))
    print(solve(series, 14))

if __name__ == "__main__":
    main()
