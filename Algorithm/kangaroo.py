import sys


def kangaroo(x1, v1, x2, v2):
    # Complete this function
    speedDiff = v1 - v2
    distDiff = x1 - x2
    if speedDiff * distDiff < 0:
        if distDiff % speedDiff == 0:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
