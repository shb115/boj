memo = [0,1,1,1,2] + [0] * 100
lastpoint = 5

def cnt(n):
    global memo, lastpoint
    if n == 0 or n == 1:
        return n    
    else:
        if memo[n] == 0:
            for i in range(lastpoint,n + 1):
                memo[i] = (cnt(i - 1) + cnt(i - 5))
            lastpoint = n
    return memo[n]

for i in range(int(input())):
    print(cnt(int(input())))
