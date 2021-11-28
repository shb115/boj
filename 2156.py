n = int(input())
wine = [int(input()) for i in range(n)]

if n == 1:
    print(wine[0])
else:
    memo = [0, wine[0], wine[0] + wine[1]]
    for i in range(3,n+1):
        memo.append(max(memo[i - 1], memo[i - 2] + wine[i - 1], memo[i - 3] + wine[i - 1] + wine[i - 2]))
    print(max(memo))
