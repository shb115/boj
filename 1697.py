from collections import deque

def bfs():
    while queue:
        a = queue.popleft()
        if a == K:
            break
        dx = [-1, 1, a]
        for i in range(3):
            na = a + dx[i]
            if 0 <= na <= 100000 and visited[na] == 0:
                queue.append(na)
                visited[na] = visited[a] + 1

N, K = map(int, input().split())
visited = [0 for _ in range(100001)]
visited[N] = 1
queue = deque()
queue.append(N)
bfs()
print(visited[K] - 1)
