List = list(map(int, input().split()))
original = [1, 1, 2, 2, 2, 8]
answer = []
for i in range(6):
    answer.append(str(original[i] - List[i]))
print(' '.join(answer))
