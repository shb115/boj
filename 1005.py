import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    time = list(map(int, sys.stdin.readline().split()))

    graph = dict()
    indegree = [0 for _ in range(N + 1)]
    q = deque([])
    dp = [0 for _ in range(N + 1)]

    for i in range(1, N + 1):
        graph[i] = []

    for __ in range(K):
        X, Y = map(int, sys.stdin.readline().split())

        graph[X].append(Y)
        indegree[Y] = indegree[Y] + 1

    W = int(sys.stdin.readline())

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i - 1]

    while q:
        build = q.popleft()

        for i in graph[build]:
            indegree[i] = indegree[i] - 1
            dp[i] = max(dp[build] + time[i - 1], dp[i])

            if indegree[i] == 0:
                q.append(i)

    print(dp[W])
