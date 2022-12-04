import string
import sys

priority = {c: i for i, c in enumerate(string.ascii_letters, 1)}
lines = sys.stdin.read().splitlines()

result = 0
for line in lines:
    mid = len(line) // 2
    fst, snd = set(line[:mid]), set(line[mid:])
    intersection = fst & snd
    assert len(intersection) == 1
    result += priority[intersection.pop()]

print(result)

result = 0
for i in range(0, len(lines), 3):
    candidates = set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2])
    assert len(candidates) == 1
    result += priority[candidates.pop()]

print(result)
