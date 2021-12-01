import sys
sys.setrecursionlimit(50000)

def dfs(x, y):
    dx = [-1, -1, -1, 1, 1, 1, 0, 0]
    dy = [0, -1, 1, 0, -1, 1, -1, 1]

    if field[x][y] == 0:
        return 0

    visited.append([x, y])

    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1 and [nx, ny] not in visited:
            dfs(nx, ny)

    return 1

w, h = map(int, sys.stdin.readline().split())
while w != 0 or h != 0:
    field = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = []
    ans = 0
    for i in range(h):
        for j in range(w):
            if [i, j] not in visited:
                ans = ans + dfs(i, j)
    print(ans)
    w, h = map(int, sys.stdin.readline().split())
