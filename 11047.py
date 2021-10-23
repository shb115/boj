#문제에서 주어진 N, K, A
N, K = map(int,input().split())
A = [int(input()) for i in range(N)]

A.reverse()

now = K     #현재 K값
cnt = 0     #경우의 수

for i in range(N):
    if A[i] <= now:
        cnt = cnt + (now // A[i])
        now = now % A[i]
        
print(cnt)
