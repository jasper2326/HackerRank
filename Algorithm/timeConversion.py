import sys


def timeConversion(s):
    # Complete this function
    result = str(s[:-2])

    arr = result.split(":")
    if 'P' in s:
        arr[0] = str((int(arr[0]) + 12) % 24)

    elif 'A' in s:
        arr[0] = str(int(arr[0]) % 24)
    return ":".join(arr)


s = raw_input().strip()
result = timeConversion(s)
print(result)