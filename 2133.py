N = int(input())
dp = [0 for _ in range(31)]
dp[2] = 3

for i in range(4, N + 2, 2):
    dp[i] = dp[i - 2] * 3
    for j in range(4, i, 2):
        dp[i] = dp[i] + dp[i - j] * 2
    dp[i] = dp[i] + 2

print(dp[N])
