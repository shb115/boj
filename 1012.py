import sys
sys.setrecursionlimit(50000)

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if field[x][y] == 0:
        return 0

    visited.append([x, y])
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1 and [nx, ny] not in visited:
            dfs(nx, ny)
            
    return 1

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    field = [[0 for __ in range(M)] for ___ in range(N)]
    for __ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        field[b][a] = 1
    visited = []
    ans = 0
    for i in range(N):
        for j in range(M):
            if [i, j] in visited:
                continue
            ans = ans + dfs(i, j)
    print(ans)
