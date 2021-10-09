def cnt(n):
    c = 0
    for i in range(1,4):
        c = c + n // (5 ** i)
    return c

print(cnt(int(input())))
