a = int(input())
arr = [0 for i in range(a)]
score_arr = arr

for i in range(a):
    arr[i] = input()
    
for i in range(a):
    score = 0
    total = 0
    for j in range(len(arr[i])):
        if arr[i][j] == 'O':
            score = score + 1
            total = total + score
        else:
            score = 0
    score_arr[i] = total
        
for i in range(a):
    print(score_arr[i])
