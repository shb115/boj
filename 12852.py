N = int(input())
if N == 1:
    print(0)
    print(1)
elif N == 2 :
    print(1)
    print(2, 1)
else:
    dp = [0 for _ in range(N + 1)]
    dp[2], dp[3] = 1, 1
    cal = [0 for _ in range(N + 1)]
    cal[2], cal[3] = 2, 1
    ans = str(N)
    
    for i in range(4, N + 1):
        if i % 3 == 0 and i % 2 == 0:
            dp[i] = min(dp[i // 3], dp[i // 2], dp[i - 1]) + 1
            if dp[i // 3] == dp[i] - 1:
                cal[i] = 1
            elif dp[i // 2] == dp[i] - 1:
                cal[i] = 2
            else:
                cal[i] = 3
        elif i % 3 == 0:
            dp[i] = min(dp[i // 3], dp[i - 1]) + 1
            if dp[i // 3] == dp[i] - 1:
                cal[i] = 1
            else:
                cal[i] = 3
        elif i % 2 == 0:
            dp[i] = min(dp[i // 2], dp[i - 1]) + 1
            if dp[i // 2] == dp[i] - 1:
                cal[i] = 2
            else:
                cal[i] = 3
        else:
            dp[i] = dp[i - 1] + 1
            cal[i] = 3

    a = N
    while a != 1:
        if cal[a] == 1:
            a = a // 3
        elif cal[a] == 2:
            a = a // 2
        else:
            a = a - 1
        ans = ans + ' ' + str(a)
    
    print(dp[N])
    print(ans)
