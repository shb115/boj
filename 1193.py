x = int(input())

i = 0
while x > 0:
    i = i + 1
    x = x - i    
x = x + i

if i % 2 == 1:
    print(str(i + 1 - x) + '/' + str(x))
else:
    print(str(x) + '/' + str(i + 1 - x))
