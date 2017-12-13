import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    A = [a0, a1, a2]
    B = [b0, b1, b2]
    pA = 0
    pB = 0

    for i in range(0, len(A), 1):
        if A[i] > B[i]:
            pA += 1
        elif A[i] < B[i]:
            pB += 1
    return str(pA) + "" + str(pB)


a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))