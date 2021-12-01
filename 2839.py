a = int(input())
x, y, i = 0, 0, 0
while 3 * x + 5 * y != a:
    y = a//5 - i
    if y < 0:
        break
    x = (a - 5 * y)//3
    i = i + 1
if 3 * x + 5 * y == a:
    print(x+y)
else:
    print(-1)
