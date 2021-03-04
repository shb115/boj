import sys
sys.setrecursionlimit(10 ** 6)

def dfs(node):
    visit.add(node)

    if len(edge[node]) <= 1:
        return True

    for i in edge[node]:
        if not i in visit:
            if dfs(i):
                earlyadopter.add(node)
            elif not i in earlyadopter:
                earlyadopter.add(node)

    return False

N = int(sys.stdin.readline())

edge = [[] for _ in range(N + 1)]
visit = set()
earlyadopter = set()

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    
    edge[a].append(b)
    edge[b].append(a)

for i in range(N + 1):
    if len(edge[i]) > 1:
        dfs(i)
        break

if N == 2:
    print(1)
else:
    print(len(earlyadopter))
