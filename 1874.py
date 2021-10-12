n = int(input())
s = []
pm = []
c = 1
p = 1
for i in range(n):
    m = int(input())
    while c <= m:
        s.append(c)
        pm.append('+')
        c = c + 1
    if s[-1] == m:
        s.pop()
        pm.append('-')
    else:
        p = 0
if p == 0:
    print('NO')
else:
    for i in pm:
        print(i)
