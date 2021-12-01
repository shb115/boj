import sys

play = sys.stdin.readline()

a = '1 2 3 4 5 6 7 8\n'
d = '8 7 6 5 4 3 2 1\n'

if play == a:
    print('ascending')
elif play == d:
    print('descending')
else:
    print('mixed')
