L, P = map(int, input().split())
article = list(map(int, input().split()))
ans = []
for i in range(5):
    ans.append(str(article[i] - (L * P)))

print(' '.join(ans))
