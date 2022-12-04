import sys

elves = sys.stdin.read().split("\n\n")
calories = []
for elf in elves:
    calories.append(sum(map(int, elf.splitlines())))

calories.sort()
print(calories[-1])
print(sum(calories[-3:]))
