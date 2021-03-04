import sys

def dfs(node):
    visit.append(node)
    dp[node][0] = wei[node - 1]
    trace[node][0].append(node)
    
    for i in edge[node]:
        if i not in visit:
            dfs(i)
            dp[node][0] = dp[node][0] + dp[i][1]

            for j in trace[i][1]:
                trace[node][0].append(j)

            if dp[i][1] >= dp[i][0]:
                dp[node][1] = dp[node][1] + dp[i][1]
                for j in trace[i][1]:
                    trace[node][1].append(j)
            else:
                dp[node][1] = dp[node][1] + dp[i][0]
                for j in trace[i][0]:
                    trace[node][1].append(j)

n = int(sys.stdin.readline())
wei = list(map(int, sys.stdin.readline().split()))

edge = [[] for _ in range(n + 1)]
visit = []
dp = [[0, 0] for _ in range(n + 1)]
trace = [[[], []] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    
    edge[a].append(b)
    edge[b].append(a)

dfs(1)

if dp[1][0] >= dp[1][1]:
    print(dp[1][0])
    a = sorted(trace[1][0])
    print(*a)
else:
    print(dp[1][1])
    a = sorted(trace[1][1])
    print(*a)
