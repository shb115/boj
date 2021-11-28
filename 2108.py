import sys
from collections import Counter

def finder(a):
    c = Counter(a)
    rank = c.most_common()
    t = rank[0][1]
    i = 0
    b = []
    while i < len(rank):
        if rank[i][1] != t:
            break
        b = b + [rank[i][0]]
        i = i + 1
    if len(b) >= 2:
        return sorted(b)[1]
    else:
        return sorted(b)[0]

n = int(input())
a = [int(sys.stdin.readline()) for i in range(n)]

print(round(sum(a)/n))
print(sorted(a)[n//2])
print(finder(a))
print(max(a)-min(a))
