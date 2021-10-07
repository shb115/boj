import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):    
    if x == M - 1 and y == N - 1:
        return 1    
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if mapp[nx][ny] < mapp[x][y]:
                dp[x][y] = dp[x][y] + dfs(nx, ny)
    return dp[x][y]

if __name__ == '__main__':

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    M, N = map(int, sys.stdin.readline().split())
    mapp = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    dp = [[-1 for _ in range(N)] for __ in range(M)]

    print(dfs(0,0))
