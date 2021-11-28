import sys, copy
from collections import deque

N, M = map(int, sys.stdin.readline().split())
zone = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

visited = [[[0, 0] for _ in range(M)] for __ in range(N)]
visited[0][0][0] = 1
queue = deque()
queue.append([0, 0, 0])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

while queue:
    a, b, c = queue[0][0], queue[0][1], queue[0][2]
    if [a, b] == [N - 1, M - 1]:
        break
    queue.popleft()
    for i in range(4):
        na, nb = a + dx[i], b + dy[i]
        if 0 <= na < N and 0 <= nb < M:
            if zone[na][nb] == '0' and visited[na][nb][c] == 0:
                queue.append([na, nb, c])
                visited[na][nb][c] = visited[a][b][c] + 1
            elif zone[na][nb] == '1' and c == 0:
                queue.append([na, nb, 1])
                visited[na][nb][1] = visited[a][b][0] + 1

if visited[N - 1][M - 1] == [0, 0]:
    print(-1)
else:
    if visited[N - 1][M - 1][0] == 0:
        print(visited[N - 1][M - 1][1])
    else:
        print(min(visited[N - 1][M - 1]))
