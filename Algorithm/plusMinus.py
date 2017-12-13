import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

minus = 0
plus = 0
zero = 0
for num in arr:
    if num > 0:
        plus += 1
    elif num == 0:
        zero += 1
    elif num < 0:
        minus += 1

print plus * 1.0 / n
print minus * 1.0 / n
print zero * 1.0 / n