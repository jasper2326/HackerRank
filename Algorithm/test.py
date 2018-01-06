import re

n = int(input())
tags = []
for i in range(n):
    text = input()
    match = re.findall(r'<(\w+)', text)
    for item in match:
        if item not in tags:
            tags.append(item)

print(';'.join(sorted(set(tags))))