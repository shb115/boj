import sys

def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
    
x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

p1, p2, p3, p4 = [x1, y1], [x2, y2], [x3, y3], [x4, y4]

if ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0 and ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0:
    if ccw(p1, p2, p3) * ccw(p1, p2, p3) == 0 and ccw(p3, p4, p1) * ccw(p3, p4, p2) == 0:
        if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            print(1)
            if min(x1, x2) == max(x3, x4) and min(y1, y2) == max(y3, y4):
                print(min(x1, x2), min(y1, y2))
            elif min(x3, x4) == max(x1, x2) and min(y3, y4) == max(y1, y2):
                print(min(x3, x4), min(y3, y4))
            else:
                if ccw(p1, p2, p4) * ccw(p3, p4, p1) != 0 or ccw(p1, p2, p3) * ccw(p3, p4, p1) != 0:
                    print(*p2)
                elif ccw(p1, p2, p4) * ccw(p3, p4, p2) != 0 or ccw(p1, p2, p3) * ccw(p3, p4, p2) != 0:
                    print(*p1)
        else:
            print(0)
    else:
        print(1)
        if x2 != x1 and x4 != x3:
            g1, g2 = (y2 - y1) / (x2 - x1), (y4 - y3) / (x4 - x3)
            b1, b2 = -g1 * x1 + y1, -g2 * x3 + y3
            print((b1 - b2) / (g2 - g1), (g2 * b1 - g1 * b2) / (g2 - g1))
        elif x2 == x1 and x4 != x3:
            g2 = (y4 - y3) / (x4 - x3)
            print(x1, g2 * (x1 - x3) + y3)
        elif x4 == x3 and x2 != x1:
            g1 = (y2 - y1) / (x2- x1)
            print(x3, g1 * (x3 - x1) + y1)
else:
    print(0)
