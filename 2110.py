def howmuch(d):
    cnt = 1
    cur_N = N_list[0]
    for i in range(1, N):
        if cur_N + d <= N_list[i]:
            cnt = cnt + 1
            cur_N = N_list[i]
    return cnt

def bs(st, en):
    if st == en:
        return st
    elif en - st == 1:
        h = howmuch(en)
        if h >= C:
            return en
        else:
            return st
    else:
        mid = (st + en) // 2
        h = howmuch(mid)
        if h >= C:
            return bs(mid, en)
        else:
            return bs(st, mid)        

N, C = map(int, input().split())
N_list = sorted([int(input()) for _ in range(N)])
N_list.sort()
st, en = 1, N_list[-1] - N_list[0]
print(bs(st, en))
