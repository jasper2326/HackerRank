import sys

arr = map(int, raw_input().strip().split(' '))

sort = sorted(arr)
sum = 0
for num in sort:
    sum += num

min = sum - sort[-1]
max = sum - sort[0]

print str(min) + ' ' + str(max)