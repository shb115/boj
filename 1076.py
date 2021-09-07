color = [input() for _ in range(3)]
value = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
print((value.index(color[0]) * 10 + value.index(color[1])) * (10 ** value.index(color[2])))
