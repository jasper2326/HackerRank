import sys

def simpleArraySum(n, ar):
    # Complete this function
    sum = 0
    for num in ar:
        sum += num
    return sum

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)