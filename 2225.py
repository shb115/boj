N, K = map(int, input().split())
dp = [[0 for _ in range(N + 1)] for __ in range(K + 1)]

for i in range(N + 1):
    dp[1][i] = 1

for i in range(1, K + 1):
    for j in range(N + 1):
        for k in range(j + 1):
            dp[i][j] = dp[i][j] + dp[i - 1][k]
            
print(dp[K][N] % 1000000000)
