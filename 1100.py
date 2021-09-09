chessboard = [input() for _ in range(8)]
answer = 0
for i in range(0, 8, 2):
    for j in range(0, 8, 2):
        if chessboard[i][j] == 'F':
            answer = answer + 1
for i in range(1, 8, 2):
    for j in range(1, 8, 2):
        if chessboard[i][j] == 'F':
            answer = answer + 1
print(answer)
