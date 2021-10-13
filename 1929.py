m, n = map(int,input().split())

if m % 2 == 0:
    a = [i for i in range(m+1,n+1,2)]
else:
    a = [i for i in range(m,n+1,2)]

a = set(a)
a = a - {1}

for i in range(3,int(n**0.5)+1,2):
    b = [j for j in range(2*i,n+1,i)]
    a = a - set(b)

if m <= 2:
    a = a | {2}

a = sorted(list(a))

for i in range(len(a)):
    print(a[i])
