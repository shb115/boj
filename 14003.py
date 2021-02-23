import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
array = []
index = []

for a in A:
    i = bisect_left(array, a)
    index.append(i)
    if len(array) <= i:
        array.append(a)
    else:
        array[i] = a

leng = len(array)
print(leng)

index = index[::-1]
A = A[::-1]
point = index.index(leng - 1)
ans = [A[point]]
k = leng - 2
for i in range(point + 1, N):
    if index[i] == k:
        ans.append(A[i])
        k = k - 1

ans = ans[::-1]
for i in ans:
    print(i, end = ' ')
