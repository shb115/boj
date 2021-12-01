def primetest(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        d = 0
        if n % 2 == 0:
            return 0
        else:
            for i in range(3,int(n**0.5)+1,2):
                if n % i == 0:
                    d = 1
                    break
            if d == 1:
                return 0
            else:
                return 1

for i in range(int(input())):
    a = int(input())
    b = a/2
    while 1:
        if primetest(b):
            if primetest(a-b):
                print(int(b),int(a-b))
                break
            else:
                if b % 2 == 0:
                    b = b - 1
                else:
                    b = b - 2
        else:
            if b % 2 == 0:
                b = b - 1
            else:
                b = b - 2
