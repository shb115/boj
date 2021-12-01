a = int(input())
b = [0 for i in range(a)]
for i in range(a):
    b[i] = input()
for i in range(a):    
    for j in range(2,len(b[i])):
        print(b[i][j]*int(b[i][0]),end='')
    print('')
