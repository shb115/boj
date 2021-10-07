def ds(st, en):
    if st == en:
        return st
    elif en - st == 1:
        cnt = 0
        for k in K_list:
            cnt = cnt + k // en
        if cnt >= N:
            return en
        else:
            return st
    else:
        cnt = 0
        mid = (st + en) // 2
        for k in K_list:
            cnt = cnt + k // mid
        if cnt >= N:
            return ds(mid, en)
        else:
            return ds(st, mid)

K, N = map(int, input().split())
K_list = [int(input()) for _ in range(K)]
st, en = 0, max(K_list)
print(ds(st,en))
