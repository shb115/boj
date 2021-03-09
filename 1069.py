X, Y, D, T = map(int, input().split())

d = (X * X + Y * Y) ** 0.5

if D <= T:
    print(d)
else:
    if d % D == 0:
        print((d // D) * T)
    else:
        if d // D == 0:
            print(min((d // D) * T + d % D, (d // D + 1) * T + D - d % D, (d // D + 2) * T))
        else:
            print(min((d // D) * T + d % D, (d // D + 1) * T))
