import sys
from collections import deque
sys.setrecursionlimit(50000)

T = int(sys.stdin.readline())

for _ in range(T):
    I = int(sys.stdin.readline())
    start = list(map(int, sys.stdin.readline().split()))
    end = list(map(int, sys.stdin.readline().split()))

    board = [[0 for _ in range(I)] for __ in range(I)]

    dx, dy = [1, 2, 2, 1, -1, -2, -2, -1], [2, 1, -1, -2, -2, -1, 1, 2]
    queue = deque([start])

    while queue:
        x, y = queue[0][0], queue[0][1]
        queue.popleft()

        if [x, y] == end:
            break
        
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and board[nx][ny] == 0:
                queue.append([nx, ny])
                board[nx][ny] = board[x][y] + 1

    print(board[end[0]][end[1]])
