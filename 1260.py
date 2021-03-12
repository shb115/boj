import sys
from collections import deque

def dfs(graph, start_node):
    visit = []
    stack = [start_node]

    for i in range(N):
        graph[i + 1].sort(reverse=True)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    for i in range(len(visit)):
        visit[i] = str(visit[i])
        
    return ' '.join(visit)

def bfs(graph, start_node):
    visit = []
    queue = deque([start_node])

    for i in range(N):
        graph[i + 1].sort()
    
    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
        
    for i in range(len(visit)):
        visit[i] = str(visit[i])

    return ' '.join(visit)

graph = dict()

N, M, V = map(int,sys.stdin.readline().split())

for i in range(N):
    graph[i + 1] = []

for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

print(dfs(graph,V))
print(bfs(graph,V))
