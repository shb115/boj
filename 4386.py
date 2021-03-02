import sys

def find_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

n = int(sys.stdin.readline())
star = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]

distance = [[0 for _ in range(n)] for __ in range(n)]

for i in range(n):
    x1, y1 = star[i][0], star[i][1]
    for j in range(i + 1, n):
        x2, y2 = star[j][0], star[j][1]

        distance[i][j] = find_distance(x1, y1, x2, y2)
        distance[j][i] = distance[i][j]

MST = [0]
ans = 0

while len(MST) != n:
    flag = [1000000, 100]
    
    for i in MST:
        for j in range(n):
            if j not in MST:
                if distance[i][j] < flag[0]:
                    flag[0] = distance[i][j]
                    flag[1] = j
                    
    MST.append(flag[1])
    ans = ans + flag[0]
            
print(round(ans, 2))
