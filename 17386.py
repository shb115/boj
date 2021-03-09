def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1, p2, p3, p4 = [x1, y1], [x2, y2], [x3, y3], [x4, y4]

if ccw(p1, p2, p3) * ccw(p1, p2, p4) > 0 or ccw(p3, p4, p1) * ccw(p3, p4, p2) > 0:
    print(0)
elif ccw(p1, p2, p3) * ccw(p1, p2, p4) == 0 and ccw(p3, p4, p1) * ccw(p3, p4, p2) == 0:
    if p1 >= p2:
        p1, p2 = p2, p1

    if p3 >= p4:
        p3, p4 = p4, p3

    if p4 >= p1 and p2 >= p3:
        print(1)
    else:
        print(0)
else:
    print(1)
