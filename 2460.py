dp = [0 for _ in range(10)]
a, b = map(int, input().split())
dp[0] = b
for i in range(1, 10):
    a, b = map(int, input().split())
    dp[i] = dp[i - 1] + b - a
print(max(dp))
