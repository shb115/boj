import sys
sys.setrecursionlimit(50000)

def bfs(x, y):
    queue = [[x, y]]

    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == '1':                
                queue.append([nx, ny])
                maze[nx][ny] = maze[a][b] + 1

N, M = map(int, sys.stdin.readline().split())
maze = [list(input()) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
maze[0][0] = 1

bfs(0, 0)
print(maze[N - 1][M - 1])
