def add(a, b):
    while b != 0:
        carry = a ^ b
        b = (a & b) << 1
        a = carry
    return a

#print(add(111, 899))


def sub(a, b):
    subtrahend = add(~b, 1)
    sub = add(a, subtrahend)
    return sub

print(sub(199, 99))