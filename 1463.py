x = int(input())
if x == 1:
    print(0)
elif x == 2:
    print(1)
else:
    memo = [0] * x
    memo[1], memo[2] = 1,1
    for i in range(3, x):
        if (i + 1) % 3 == 0 and (i + 1) % 2 == 0:
            memo[i] = min(memo[((i + 1) // 3) - 1], memo[((i + 1) // 2) - 1], memo[i - 1]) + 1
        elif (i + 1) % 3 == 0 and (i + 1) % 2 != 0:
            memo[i] = min(memo[((i + 1) // 3) - 1], memo[i - 1]) + 1
        elif (i + 1) % 3 != 0 and (i + 1) % 2 == 0:
            memo[i] = min(memo[((i + 1) // 2) - 1], memo[i - 1]) + 1
        else:
            memo[i] = memo[i - 1] + 1
    print(memo[x - 1])
