import sys
from collections import deque

def bfs():
    q = deque()
    q.append([A, ''])
    while q:
        n, ans = q.popleft()
        if n == B:
            return ans
        dn = [(2 * n) % 10000, (n - 1) % 10000, ((n * 10) + (n // 1000)) % 10000, (n // 10) + ((n % 10) * 1000)]
        dans = ['D', 'S', 'L', 'R']
        for i in range(4):
            nn = dn[i]
            if nn not in visited:
                q.append([nn, ans + dans[i]])
                visited.append(nn)

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    visited = [A]
        
    print(bfs())
