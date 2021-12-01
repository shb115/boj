def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def combination(n,r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))

n, m = map(int,input().split())
card_list = list(map(int,input().split()))

sum_list = [0 for i in range(combination(n,3))]

s = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum_list[s] = card_list[i] + card_list[j] + card_list[k]
            s = s + 1

maximum = 0
for i in range(len(sum_list)):
    if sum_list[i] <= m:
        if sum_list[i] >= maximum:
            maximum = sum_list[i]
            
print(maximum)
