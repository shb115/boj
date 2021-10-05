A, B = map(int, input().split())

l = []

for i in range(46):
    a = [i] * i
    l = l + a

print(sum(l[A - 1:B]))
