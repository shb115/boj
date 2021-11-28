import sys
from math import gcd, factorial

def dfs(L, visit, rest):
    if visit == (1 << N) - 1:
        if rest == 0:
            return 1
        else:
            return 0

    if dp[visit][rest] != -1:
        return dp[visit][rest]

    for i in range(N):
        if visit & (1 << i) == 0:
            dp[visit][rest] = dp[visit][rest] + dfs(L + leng[i], visit | (1 << i), (rest + sqr[i][L]) % K)

    dp[visit][rest] = dp[visit][rest] + 1

    return dp[visit][rest]

N = int(sys.stdin.readline())
Set = [int(sys.stdin.readline()) for _ in range(N)]
K = int(sys.stdin.readline())

dp = [[-1 for __ in range(K)] for _ in range(1 << N)]

leng = [len(str(Set[i])) for i in range(N)]
sqr = [[-1 for __ in range(sum(leng))] for _ in range(1 << N)]

for i in range(N):
    for j in range(sum(leng)):
        sqr[i][j] = (Set[i] * (10 ** j)) % K

temp = dfs(0, 0, 0)

f = factorial(N)
    
if temp == 0:
    print('0/1')
else:
    g = gcd(dp[0][0], f)
    print('{}/{}'.format(temp // g, f // g))
