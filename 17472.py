import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    if island[x][y] == 0:
        return 0

    visited.append([x, y])
    island[x][y] = ans

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and island[nx][ny] == 1 and [nx, ny] not in visited:
            dfs(nx, ny)

    return 1

def find(x):
    if parent[x] == x:
        return x

    return find(parent[x])

def union(a, b):
    a, b = find(a), find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, sys.stdin.readline().split())
island = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

island_t = [[0 for _ in range(N)] for __ in range(M)]
visited = []
ans = 1
distance = []
answer = 0

for i in range(N):
    for j in range(M):
        if [i, j] in visited:
            continue
        
        ans = ans + dfs(i, j)

for i in range(N):
    for j in range(M):
        island_t[j][i] = island[i][j]

parent = [i for i in range(ans)]

for i in range(N):
    point = 10
    
    for j in range(M):
        if island[i][j] != 0:
            if point != 10 and island[i][j] != island[i][point]:
                d = j - point - 1
                if d > 1:
                    distance.append([d, island[i][j], island[i][point]])
            point = j
            

for i in range(M):
    point = 10
    
    for j in range(N):
        if island_t[i][j] != 0:
            if point != 10 and island_t[i][j] != island_t[i][point]:
                d = j - point - 1
                if d > 1:
                    distance.append([d, island_t[i][j], island_t[i][point]])
            point = j        

distance.sort()

for c, a, b in distance:
    if find(a) != find(b):
        union(a, b)
        answer = answer + c

for i in range(1, ans):
    parent[i] = find(i)

if len(set(parent)) == 2:
    print(answer)
else:
    print(-1)
