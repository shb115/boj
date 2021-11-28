import sys

N = int(sys.stdin.readline())

cnt = 1

for _ in range(N):
    cnt = cnt - 1 + int(sys.stdin.readline())

print(cnt)
