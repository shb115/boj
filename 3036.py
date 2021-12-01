def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
n = int(input())
r = list(map(int,input().split()))
for i in range(1, n):
    print(str(r[0]//gcd(r[0], r[i])) + '/' + str(r[i]//gcd(r[0], r[i])))
