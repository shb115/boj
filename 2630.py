def dca(f):
    if len(f) == 1 and f[0] == '0':
        return (1, 0)
    elif len(f) == 1 and f[0] == '1':
        return (0, 1)
    if len(set(f)) == 1 and len(set(f[0])) == 2 and f[0][0] == '0':
        return (1, 0)
    elif len(set(f)) == 1 and len(set(f[0])) == 2 and f[0][0] == '1':
        return (0, 1)
    else:
        n = len(f)
        f1 = [f[i][:n - 1] for i in range(n // 2)]
        f2 = [f[i][:n - 1] for i in range(n // 2, n)]
        f3 = [f[i][n:] for i in range(n // 2)]
        f4 = [f[i][n:] for i in range(n // 2, n)]
        return (dca(f1)[0] + dca(f2)[0] + dca(f3)[0] + dca(f4)[0], dca(f1)[1] + dca(f2)[1] + dca(f3)[1] + dca(f4)[1])


n = int(input())
cp = [input() for i in range(n)]

a = dca(cp)

print(a[0])
print(a[1])
