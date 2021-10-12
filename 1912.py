n = int(input())
a = list(map(int,input().split()))
memo = [-1000 for i in range(n)]
memo[0] = a[0]
for i in range(1, n):
    memo[i] = max(0,memo[i - 1]) + a[i]    
print(max(memo))
