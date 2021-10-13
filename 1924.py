x, y = map(int, input().split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
today = sum(month[:x - 1]) + y - 1
day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
print(day[today % 7])
