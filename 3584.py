import sys
from collections import deque

def lca(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]

    while parent[a] != parent[b]:
        a = parent[a]
        b = parent[b]

    if a == b:
        return a
    else:
        return parent[a]

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    parent = dict()
    child = dict()
    depth = [0 for _ in range(N + 1)]
    q = deque([])

    for i in range(1, N + 1):
        parent[i] = 0
        child[i] = []

    for _ in range(N - 1):
        A, B = map(int, sys.stdin.readline().split())

        parent[B] = A
        child[A].append(B)

    a, b = map(int, sys.stdin.readline().split())

    for i in range(1, N + 1):
        if parent[i] == 0:
            q.append(i)

    while q:
        k = q.popleft()

        for i in child[k]:
            depth[i] = depth[k] + 1
            q.append(i)

    print(lca(a, b))
