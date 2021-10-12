import sys


def dfs(x,y):
    
    if x == N - 1 and y == N - 1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    
    dx = [game[x][y], 0]
    dy = [0, game[x][y]]
    
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            dp[x][y] = dp[x][y] + dfs(nx, ny)
            
    return dp[x][y]
    

if __name__ == '__main__':
    
    N = int(input())
    game = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dp = [[-1 for _ in range(N)] for __ in range(N)]
    
    print(dfs(0,0))
