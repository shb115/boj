a = int(input())
arr = [0 for i in range(a)]
for i in range(a):
    sum1 = 0
    avg = 0
    total = 0
    arr[i] = list(map(int,input().split()))
    for j in range(arr[i][0]):
        sum1 = sum1 + arr[i][j+1]
    avg = sum1 / arr[i][0]
    for j in range(arr[i][0]):
        if arr[i][j+1] > avg:
            total = total + 1
    print('%.3f' % (total / arr[i][0] * 100) + '%')
