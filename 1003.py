memo = [(1,0),(0,1)] + [(0,0)] * 39

def newfibo(n):
    global memo
    if n == 0:
        return (1,0)
    else:
        if memo[n] != (0,0):
            return memo[n]
    memo[n] = (newfibo(n - 1)[0] + newfibo(n - 2)[0], newfibo(n - 1)[1] + newfibo(n - 2)[1])
    return memo[n]
    
t = int(input())
for i in range(t):
    n = int(input())
    print(newfibo(n)[0],newfibo(n)[1])
