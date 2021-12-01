a = int(input())
b = int(input())
c = int(input())
num = a * b * c
arr = str(num)
arr1 = '0123456789'
for i in range(10):
    print(arr.count(arr1[i]))
