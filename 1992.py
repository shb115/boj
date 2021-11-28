def dca(f):
    if len(set(f)) == 1 and len(set(f[0])) == 1 and f[0][0] == '0':
        return '0'
    elif len(set(f)) == 1 and len(set(f[0])) == 1 and f[0][0] == '1':
        return '1'
    else:
        n = len(f)
        f1 = [f[i][:n // 2] for i in range(n // 2)]
        f2 = [f[i][:n // 2] for i in range(n // 2, n)]
        f3 = [f[i][n // 2:] for i in range(n // 2)]
        f4 = [f[i][n // 2:] for i in range(n // 2, n)]
        return '(' + dca(f1) + dca(f3) + dca(f2) + dca(f4) + ')'


n = int(input())
cp = [input() for i in range(n)]

print(dca(cp))
