T = int(input())

for _ in range(T):
    n = int(input())
    room = [0 for __ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            room[j] = (room[j] + 1) % 2

    print(room.count(1))
