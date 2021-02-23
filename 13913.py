from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)

def bfs():
    while queue:
        x = queue.popleft()
        if x == K:
            break
        dx = [-1, 1, x]
        for i in range(3):
            nx = x + dx[i]
            if 0 <= nx <= 100000 and visited[nx] == 0:
                queue.append(nx)
                visited[nx] = visited[x] + 1        

N, K = map(int, input().split())
visited = [0 for _ in range(100001)]
visited[N] = 1
queue = deque()
queue.append(N)
reconstruct = []
reconstruct.append(K)

bfs()

k = K

while N != k:
    if 0 <= k - 1 <= 100000 and visited[k - 1] == visited[k] - 1:        
        k = k - 1
        reconstruct.append(k)
    elif 0 <= k + 1 <= 100000 and visited[k + 1] == visited[k] - 1:
        k = k + 1
        reconstruct.append(k)
    elif k % 2 == 0 and 0 <= k // 2 <= 100000 and visited[k // 2] == visited[k] - 1:
        k = k // 2
        reconstruct.append(k)

reconstruct.reverse()

print(visited[K] - 1)
for i in reconstruct:
    print(i, end = ' ')
