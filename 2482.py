N = int(input())
K = int(input())
dp = [[0 for _ in range(K + 1)] for __ in range(N + 1)]

for i in range(N + 1):
    dp[i][1] = i
    dp[i][0] = 1

for i in range(2, N + 1):
    for j in range(2, K + 1):
        dp[i][j] = (dp[i - 2][j - 1] + dp[i - 1][j]) % 1000000003

dp[N][K] = dp[N - 3][K - 1] + dp[N - 1][K]
print(dp[N][K] % 1000000003)
