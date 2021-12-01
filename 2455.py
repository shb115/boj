import sys

station = [list(map(int,sys.stdin.readline().split())) for _ in range(4)]
people = [0 for _ in range(4)]

people[0] = station[0][1]
for i in range(1, 4):
    people[i] = people[i - 1] + station[i][1] - station[i][0]

print(max(people))
