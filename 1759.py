import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
a = list(sys.stdin.readline().split())

vowel = ['a', 'e', 'i', 'o', 'u']
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
             'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

a.sort()
b = list(combinations(a, L))
c = [False] * len(b)

for i in range(len(b)):
    for j in vowel:
        if j in b[i]:
            c[i] = True
            break
    cnt_c = 0
    for j in consonant:
        if j in b[i]:
            cnt_c = cnt_c + 1
    if cnt_c >= 2 and c[i] == True:
        c[i] = True
    else:
        c[i] = False

for i in range(len(b)):
    if c[i]:
        print(''.join(b[i]))
