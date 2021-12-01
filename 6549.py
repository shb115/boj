while True:
    n, *l=list(map(int, input().split()))
    l.append(0)
    if n == 0:
        break
    s = []
    m = 0
    for i, h in enumerate(l):
        while s and l[s[-1]] > h:
            ih = l[s.pop()]
            if s:
                w = i - s[-1] -1
            else:
                w = i
            m = max(m, w * ih)
        s.append(i)
    print(m)
