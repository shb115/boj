import sys
from itertools import combinations

cnt = 0
while 1:
    a = list(map(int, sys.stdin.readline().split()))
    if a == [0]:
        break
    if cnt != 0:
        print()
    c = list(combinations(a[1:], 6))
    for i in c:
        for j in i:
            print(j, end = ' ')
        print()
    cnt = cnt + 1
