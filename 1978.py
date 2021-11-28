def primetest(a):
    d = 0
    if a == 1:
        return 0
    else:
        for i in range(1,int(a**(1/2)) + 1):
            if a % i == 0:
                d = d + 1
        if d == 1:
            return 1
        else:
            return 0
    
n = int(input())
a = list(map(int,input().split()))
total = 0

for i in range(n):
    total = total + primetest(a[i])
    
print(total)
