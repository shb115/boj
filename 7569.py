import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for __ in range(H)]

dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
queue = deque()

for i in range(N):
    for j in range(M):
        for k in range(H):
            if tomato[k][i][j] == 1:
                queue.append([k, i, j])

while queue:
    a, b, c = queue[0][1], queue[0][2], queue[0][0]
    queue.popleft()
    for i in range(6):
        x, y, z = a + dx[i], b + dy[i], c + dz[i]
        if 0 <= x < N and 0 <= y < M and 0 <= z < H and tomato[z][x][y] == 0:
            queue.append([z, x, y])
            tomato[z][x][y] = tomato[c][a][b] + 1

isTrue = False
max_num = 0
for z in range(H):
    for x in range(N):
        for y in range(M):
            if tomato[z][x][y] == 0:
                isTrue = True
            max_num = max(max_num, tomato[z][x][y])

if isTrue == True:
    print(-1)
else:
    print(max_num - 1)
