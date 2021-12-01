n = int(input())
stair = [int(input()) for i in range(n)]
if n == 1:
    print(stair[0])
else:
    memo = [0, stair[0], stair[0] + stair[1]]
    for i in range(3,n+1):
        memo.append(max(memo[i - 2] + stair[i - 1], memo[i - 3] + stair[i - 1] + stair[i - 2]))
    print(memo[n])
