import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(1000000)]

dp[0], dp[1] = 1, 2

for i in range(2, N):
    dp[i] = (dp[i -1] + dp[i - 2]) % 15746

print(dp[N - 1])
