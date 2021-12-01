import sys

N = int(input())
ox = list(map(int, sys.stdin.readline().split()))
point = [0 for _ in range(N)]

if ox[0] == 1:
    point[0] = 1

for i in range(1, N):
    if ox[i] == 1:
        point[i] = point[i - 1] + 1
    else:
        point[i] = 0

print(sum(point))
