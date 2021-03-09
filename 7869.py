import math

x1, y1, r1, x2, y2, r2 = map(float, input().split())

d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

if d >= r1 + r2:
    print('%.3f' % 0)
else:
    if d <= r1 - r2:
        print('%.3f' % round(math.pi * r2 * r2, 3))
    elif d <= r2 - r1:
        print('%.3f' % round(math.pi * r1 * r1, 3))
    else:
        theta1 = 2 * math.acos((d * d + r1 * r1 - r2 * r2) / (2 * d * r1))
        theta2 = 2 * math.acos((d * d + r2 * r2 - r1 * r1) / (2 * d * r2))
        
        S = (theta1 * r1 * r1 + theta2 * r2 * r2) / 2
        T = (math.sin(theta1) * r1 * r1 + math.sin(theta2) * r2 * r2) / 2

        print('%.3f' % round(S - T, 3))
