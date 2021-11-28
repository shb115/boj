import sys
from collections import deque

# DFS
def dfs(graph, start_node):
    visit = []
    stack = [start_node]

    for i in range(N):
        graph[i + 1].sort(reverse = True)

    while stack:
        node = stack.pop()  # 가장 최근에 첨가된 노드를 선택
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    for i in range(len(visit)):
        visit[i] = str(visit[i])
        
    print(' '.join(visit))

# BFS
def bfs(graph, start_node):
    visit = []
    queue = deque([start_node])

    for i in range(N):
        graph[i + 1].sort()
    
    while queue:
        node = queue.popleft()  # 인접한 모든 정점을 우선 방문
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
        
    for i in range(len(visit)):
        visit[i] = str(visit[i])

    print(' '.join(visit))


# 문제에서 주어진 N, M, V
N, M, V = map(int,sys.stdin.readline().split())

# 경로
graph = dict()
for i in range(N):
    graph[i + 1] = []

# 문제에서 주어진 간선이 연결하는 두 정점의 번호
for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, V)
bfs(graph, V)
