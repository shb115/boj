N = input()
counter = [N.count(str(i)) for i in range(10)]
counter[6] = (counter[6] + counter[9] + 1) // 2
counter[9] = counter[6]
print(max(counter))
