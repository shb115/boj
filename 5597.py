hw = {int(input()) for _ in range(28)}
stu = {i for i in range(1, 31)}
nothw = stu - hw
nothw = sorted(list(nothw))
for i in nothw:
    print(i)
