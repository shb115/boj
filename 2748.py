memo = [0,1] + [0] * 89

def fibo(n):
    global memo
    if n == 0:
        return 0
    else:
        if memo[n] != 0:
            return memo[n]
    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]
print(fibo(int(input())))
