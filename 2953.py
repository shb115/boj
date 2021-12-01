import sys

point = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
sumpoint = [0 for _ in range(5)]

for i in range(5):
    sumpoint[i] = sum(point[i])

print(sumpoint.index(max(sumpoint)) + 1, max(sumpoint))
