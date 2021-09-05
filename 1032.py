N = int(input())
filename = [input() for _ in range(N)]
answer = list(filename[0])
length = len(answer)
for i in range(length):
    for j in range(N):
        if filename[j][i] != answer[i]:
            answer[i] = '?'
            break
print(''.join(answer))
