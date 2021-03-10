import sys
from collections import deque
sys.setrecursionlimit(50000)

M, N = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i, j])

while queue:
    a, b = queue[0][0], queue[0][1]
    queue.popleft()
    for i in range(4):
        x, y = a + dx[i], b + dy[i]
        if 0 <= x < N and 0 <= y < M and tomato[x][y] == 0:
            queue.append([x, y])
            tomato[x][y] = tomato[a][b] + 1

ans = max(map(max, tomato)) - 1

for i in range(N):
    if 0 in tomato[i]:
        ans = -1
        break

print(ans)
