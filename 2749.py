m = 10 ** 6
p = 15 * m // 10

def mul(a, b):
    n = len(a)
    c = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            t = 0
            for k in range(n):
                t = (t + a[i][k] * b[k][j]) % m
            c[i].append(t)
    return c

n = int(input())
n = n % p

n_bin = []
i = 1
j = 0
while n != 0:
    if n >= i:
        i = i * 2
        j = j + 1
    else:
        n_bin.append(j - 1)
        n = n - i // 2
        i = 1
        j = 0

mat = [[1, 1], [1, 0]]

b = []
for i in n_bin:
    c = mat
    for j in range(i):
        c = mul(c, c)
    b.append(c)

d = b[0]
for i in range(1, len(b)):
    d = mul(d, b[i])

print(d[0][1])
