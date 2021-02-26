import sys
sys.setrecursionlimit(10 ** 6)

def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a
        num[a] = num[a] + num[b]

T = int(sys.stdin.readline())

for _ in range(T):
    F = int(sys.stdin.readline())
    
    parent = dict()
    num = dict()
    
    for __ in range(F):
        a, b = sys.stdin.readline().rstrip().split()
        
        if a not in parent:
            parent[a] = a
            num[a] = 1
            
        if b not in parent:
            parent[b] = b
            num[b] = 1

        union(a, b)

        print(num[find(a)])
