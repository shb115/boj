import sys

def prime(n):
    if n <= 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
        

n = int(sys.stdin.readline())

while n != 0:
    for i in range(3, n // 2 + 1):
        if prime(i) and prime(n - i):
            print(str(n) + ' = ' + str(i) + ' + ' + str(n - i))
            break
    n = int(sys.stdin.readline())
