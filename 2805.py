import sys

def ds(st, en):
    if st == en:
        return st
    elif en - st == 1:
        cnt = 0
        for n in tree:
            cnt = cnt + max(n - en, 0)
        if cnt >= M:
            return en
        else:
            return st
    else:
        mid = (st + en) // 2
        cnt = 0
        for n in tree:
            cnt = cnt + max(n - mid, 0)
        if cnt >= M:
            return ds(mid, en)
        else:
            return ds(st, mid)

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
st, en = 0, max(tree)
print(ds(st, en))
