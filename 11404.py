import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
inf = 100000 * 100 + 1
dp = [[inf for _ in range(n)] for __ in range(n)]
for i in range(n):
    dp[i][i] = 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    dp[a - 1][b - 1] = min(dp[a - 1][b - 1], c)

for d in range(n):
    for x in range(n):
        for y in range(n):
            dp[x][y] = min(dp[x][y], dp[x][d] + dp[d][y])

for i in range(n):
    for j in range(n):
        if dp[i][j] == inf:
            dp[i][j] = '0'
        else:
            dp[i][j] = str(dp[i][j])

for i in range(n):
    print(' '.join(dp[i]))
