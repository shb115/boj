result = ['E', 'A', 'B', 'C', 'D']
for _ in range(3):
    game = list(map(int, input().split()))
    print(result[game.count(0)])
