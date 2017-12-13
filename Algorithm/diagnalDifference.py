import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

sum_main = 0
sum_sec = 0

for i in range(0, n, 1):
    sum_main += a[i][i]
    sum_sec += a[i][n - i - 1]

print abs(sum_main - sum_sec)