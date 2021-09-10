n = int(input())
a = [[]] * 50
c = []
for i in range(n):
    b = input()
    a[len(b)-1] = a[len(b)-1] + [b]
for i in range(50):
    a[i] = sorted(list(set(a[i])))
    c = c + a[i]
for i in range(len(c)):
    print(c[i])
