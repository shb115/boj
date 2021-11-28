import sys

V, E = map(int, sys.stdin.readline().split())

inf = sys.maxsize
dp = [[inf for _ in range(V)] for __ in range(V)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    dp[a - 1][b - 1] = c

for d in range(V):
    for x in range(V):
        for y in range(V):
            dp[x][y] = min(dp[x][y], dp[x][d] + dp[d][y])

answer = inf
for i in range(V):
    answer = min(answer, dp[i][i])

if answer == inf:
    print(-1)
else:
    print(answer)
