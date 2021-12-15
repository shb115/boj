a = input()
b = input()
dp = [[0 for _ in range(len(b))] for __ in range(len(a))]

for i in range(len(a)):
    if a[i] == b[0]:
        dp[i][0] = 1
    else:
        dp[i][0] = dp[i - 1][0]

for j in range(len(b)):
    if b[j] == a[0]:
        dp[0][j] = 1
    else:
        dp[0][j] = dp[0][j - 1]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[len(a) - 1][len(b) - 1])
