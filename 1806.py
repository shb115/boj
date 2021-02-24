import sys

N, S = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
start, end = 0, 0
cnt = 100001
summ = A[0]

while end < N:
    if summ >= S:
        cnt = min(cnt, end - start + 1)
        summ = summ - A[start]
        start = start + 1        
    else:
        end = end + 1
        if end >= N:
            break
        summ = summ + A[end]

if cnt == 100001:
    print(0)
else:
    print(cnt)
