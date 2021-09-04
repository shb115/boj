n, m = map(int,input().split())

board_list = [0 for i in range(n)]
chess_list = ['' for i in range((n-7)*(m-7))]
check_list = [0 for i in range((n-7)*(m-7))]

chessboard1 = 'WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW'
chessboard2 = 'BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB'

for i in range(n):
    board_list[i] = input()

s = 0
for i in range(n-7):
    for j in range(m-7):
        for k in range(8):
              chess_list[s] = chess_list[s] + board_list[i + k][j:8+j]
        s = s + 1

for i in range(len(chess_list)):
    count1 = 0
    count2 = 0
    for j in range(64):
        if chess_list[i][j] != chessboard1[j]:
            count1 = count1 + 1
        if chess_list[i][j] != chessboard2[j]:
            count2 = count2 + 1
    check_list[i] = min(count1,count2)

print(min(check_list))
