import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    if dp[x][y] < 0:
        dp[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and bambu[x][y] < bambu[nx][ny]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny))
        dp[x][y] = dp[x][y] + 1

    return dp[x][y]

N = int(input())
bambu = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[-1 for _ in range(N)] for __ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, dfs(i, j))
        
print(ans)
