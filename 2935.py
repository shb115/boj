List = [input() for _ in range(3)]
if List[1] == '+':
    print(int(List[0]) + int(List[2]))
else:
    print(int(List[0]) * int(List[2]))
