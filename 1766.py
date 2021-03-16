import sys

N, M = map(int, sys.stdin.readline().split())

graph = dict()
indegree = [0 for _ in range(N + 1)]
q = []
ans = []

for i in range(1, N + 1):
    graph[i] = []

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())

    graph[A].append(B)
    indegree[B] = indegree[B] + 1

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    q.sort(reverse = True)
    question = q.pop()

    for i in graph[question]:
        indegree[i] = indegree[i] - 1

        if indegree[i] == 0:
            q.append(i)

    ans.append(question)

print(*ans)
