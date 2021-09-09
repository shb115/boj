A, B = input().split()
len_A, len_B = len(A), len(B)
distance = []
for i in range(len_B - len_A + 1):
    d = 0
    for j in range(len_A):
        if A[j] != B[j + i]:
            d = d + 1
    distance.append(d)
print(min(distance))
