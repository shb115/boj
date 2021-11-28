def cnt(n):
    c1, c2 = 0, 0
    for i in range(1,14):
        c2 = c2 + n // (5 ** i)
    for i in range(1,32):
        c1 = c1 + n // (2 ** i)    
    return [c1, c2]

n, m = map(int,input().split())

t = cnt(n)[0] - cnt(m)[0] - cnt(n - m)[0]
f = cnt(n)[1] - cnt(m)[1] - cnt(n - m)[1]
print(min(t,f))
