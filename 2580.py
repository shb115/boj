sudoku = [list(map(int,input().split())) for i in range(9)]
zeros = [(i,j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def possible(i, j):
    s = [1,2,3,4,5,6,7,8,9]
    for k in range(9):
        if sudoku[i][k] in s:
            s.remove(sudoku[i][k])
        if sudoku[k][j] in s:
            s.remove(sudoku[k][j])
    for p in range((i//3)*3, ((i//3)+1)*3):
        for q in range((j//3)*3, ((j//3)+1)*3):
            if sudoku[p][q] in s:
                s.remove(sudoku[p][q])
    return s

flag = False
def dfs(x):
    global flag
    if flag:
        return
    if x == len(zeros):
        for row in sudoku:
            print(*row)
            flag = True
        return
    else:
        (i,j) = zeros[x]
        s = possible(i,j)
        for k in s:
            sudoku[i][j] = k
            dfs(x + 1)
            sudoku[i][j] = 0

dfs(0)
