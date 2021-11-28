N = int(input())
dp = [1, 1]
for i in range(1, N):
    dp.append(dp[i] + dp[i - 1])
print(dp[N - 1])
