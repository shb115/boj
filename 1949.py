import sys
sys.setrecursionlimit(10 ** 6)

def dfs(node):
    visit.append(node)
    dp[node][0] = population[node - 1]

    for i in edge[node]:
        if i not in visit:
            dfs(i)
            dp[node][0] = dp[node][0] + dp[i][1]
            dp[node][1] = dp[node][1] + max(dp[i][1], dp[i][0])

N = int(sys.stdin.readline())
population = list(map(int, sys.stdin.readline().split()))

edge = [[] for _ in range(N + 1)]
visit = []
dp = [[0, 0] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())

    edge[a].append(b)
    edge[b].append(a)

dfs(1)

print(max(dp[1]))
