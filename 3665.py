import sys
from collections import deque

tc = int(sys.stdin.readline())

for _ in range(tc):
    n = int(sys.stdin.readline())
    last_rank = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())

    graph = dict()
    indegree = [0 for __ in range(n + 1)]
    q = deque([])
    change = set([])
    ans = []

    for i in range(1, n + 1):
        graph[i] = []

    for __ in range(m):
        a, b = map(int, sys.stdin.readline().split())

        if last_rank.index(a) < last_rank.index(b):
            graph[b].append(a)
            indegree[a] = indegree[a] + 1
        else:
            graph[a].append(b)
            indegree[b] = indegree[b] + 1

        change.add(a)
        change.add(b)

    for i in change:
        if indegree[i] == 0:
            q.append(i)

    for i in range(len(q) - 1):
        if last_rank.index(q[i]) > last_rank.index(q[i + 1]):
            tmp = q[i]
            q[i] = q[i + 1]
            q[i + 1] = tmp

    while q:
        t = q.popleft()

        for i in graph[t]:
            indegree[i] = indegree[i] - 1

            if indegree[i] == 0:
                q.append(i)

        ans.append(t)
