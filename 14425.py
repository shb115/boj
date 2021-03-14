import sys

N, M = map(int, sys.stdin.readline().split())
S = [sys.stdin.readline() for _ in range(N)]

cnt = 0

for _ in range(M):
    if sys.stdin.readline() in S:
        cnt = cnt + 1

print(cnt)
