import sys

N, K = map(int, sys.stdin.readline().split())
N_list = [int(sys.stdin.readline()) for _ in range(N)]

dp = [1] + [0 for _ in range(10000)]

for n in N_list:
    for i in range(n, K + 1):
        dp[i] = dp[i] + dp[i - n]

print(dp[K])
