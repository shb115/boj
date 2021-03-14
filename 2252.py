import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

leng = dict()
indegree = [0 for _ in range(N + 1)]
q = deque([])

for i in range(1, N + 1):
    leng[i] = []

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())

    leng[A].append(B)
    indegree[B] = indegree[B] + 1

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    stu = q.popleft()

    for i in leng[stu]:
        indegree[i] = indegree[i] - 1
        
        if indegree[i] == 0:
            q.append(i)

    print(stu, end = ' ')
