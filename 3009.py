a = [0, 0, 0]
for i in range(3):
    a[i] = list(map(int,input().split()))
x = [a[0][0], a[1][0], a[2][0]]
y = [a[0][1], a[1][1], a[2][1]]
for i in range(3):
    if x.count(x[i]) == 1:
        xx = x[i]
        break
for i in range(3):
    if y.count(y[i]) == 1:
        yy = y[i]
        break
print(xx,yy)
