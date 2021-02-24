import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(N)]
checklist = [-1 for _ in range(N)]

for i in range(1, N):
    check = -1
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            check = j
    checklist[i] = check

maximum = max(dp)
a = dp.index(maximum)
ans = str(A[a])

while a > 0:
    a = checklist[a]
    if a >= 0:
        ans = str(A[a]) + ' ' + ans

print(maximum)
print(ans)
