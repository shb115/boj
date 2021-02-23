import sys

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

m, n = len(a) - 1, len(b) - 1
print(dp[m][n])
ans = ''

while m != 0 and n != 0:
    if dp[m][n] == dp[m - 1][n]:
        m = m - 1
    elif dp[m][n] == dp[m][n - 1]:
        n = n - 1
    else:
        ans = a[m] + ans
        m, n = m - 1, n - 1

while 1:
    if m == 0 and n == 0:
        if dp[m][n] == 1:
            ans = a[m] + ans
        break
        
    elif m == 0:
        if dp[m][n] == 1 and dp[m][n - 1] == 0:
            ans = b[n] + ans
            break
        else:
            n = n - 1
    else:
        if dp[m][n] == 1 and dp[m - 1][n] == 0:
            ans = a[m] + ans
            break
        else:
            m = m - 1

print(ans)
