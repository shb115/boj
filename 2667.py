import sys
sys.setrecursionlimit(50000)

def dfs(x, y):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    if zone[x][y] == '0':
        return 0

    visited.append([x, y])

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and zone[nx][ny] == '1' and [nx, ny] not in visited:
            dfs(nx, ny)

    return 1

N = int(sys.stdin.readline())
zone = [list(input()) for _ in range(N)]
visited = []
ans = 0
cnt = [0]
ans_cnt = []

for i in range(N):
    for j in range(N):
        if [i, j] in visited:
            continue
        ans = ans + dfs(i, j)
        if len(visited) != cnt[-1]:
            cnt.append(len(visited))        

print(ans)
for i in range(ans):
    ans_cnt.append(cnt[i + 1] - cnt[i])
ans_cnt.sort()
for i in range(ans):
    print(ans_cnt[i])
