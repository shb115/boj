import sys
sys.setrecursionlimit(10 ** 6)

def dfs(start):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i)

N = int(sys.stdin.readline())
tree = dict()
for i in range(N):
    tree[i + 1] = []
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
parents = [0 for _ in range(N + 1)]

dfs(1)
for i in range(2, N + 1):
    print(parents[i])
