import sys

def Round(n, k, l):
    if n == 2:
        return 0, 0, 0
    else:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n // 2 + 1

        if k % 2 == 0:
            k = k // 2
        else:
            k = k // 2 + 1

        if l % 2 == 0:
            l = l // 2
        else:
            l = l // 2 + 1
        
        if k == l:
            return 0, 0, 0
        else:
            return n, k, l
        

N, kim, lim = map(int, sys.stdin.readline().split())

cnt = 0
while N:
    N, kim, lim = Round(N, kim, lim)
    cnt = cnt + 1

print(cnt)
