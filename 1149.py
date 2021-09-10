n = int(input())
cost = [list(map(int,input().split())) for i in range(n)]
memo = [[]] * n
for i in range(n):
    if i == 0:
        for j in range(3):
            memo[0] = memo[0] + [cost[0][j]]
    else:
        for j in range(3):
            if j == 0:
                memo[i] = memo[i] + [cost[i][j] + min(memo[i - 1][1],memo[i - 1][2])]
            elif j == 1:
                memo[i] = memo[i] + [cost[i][j] + min(memo[i - 1][0],memo[i - 1][2])]
            else:
                memo[i] = memo[i] + [cost[i][j] + min(memo[i - 1][0],memo[i - 1][1])]
print(min(memo[n-1]))
