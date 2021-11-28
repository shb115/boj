import sys

def cnt(n):
    c = 0

    for i in range(N):
        if (1 << i) & n:
            c = c + 1

    return c

N = int(sys.stdin.readline())
D = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [200000 for _ in range(1 << N)]
dp[0] = 0

for i in range(1 << N):
    c = cnt(i)
    for j in range(N):
        if not (i & (1 << j)):
            dp[i | 1 << j] = min(dp[i | 1 << j], dp[i] + D[c][j])

print(dp[-1])
