xp, yp = 3, 9
fx, fy = 5, 1
a, b = 7, 20

grid = ['%%%%%%%%%%%%%%%%%%%%',
        '%--------------%---%',
        '%-%%-%%-%%-%%-%%-%-%',
        '%--------P-------%-%',
        '%%%%%%%%%%%%%%%%%%-%',
        '%.-----------------%',
        '%%%%%%%%%%%%%%%%%%%%']


stack = [(xp, yp)]
path = [(xp, yp)]

while stack:
    cp = stack.pop(-1)
    if cp[0] == fx and cp[1] == fy:
        break

    elif grid[cp[0] - 1][cp[1]] == '-':
        stack.append((cp[0] - 1, cp[1]))
        path.append((cp[0] - 1, cp[1]))

    elif grid[cp[0]][cp[1] - 1] == '-':
        stack.append((cp[0], cp[1] - 1))
        path.append((cp[0], cp[1] - 1))

    elif grid[cp[0]][cp[1] + 1] == '-':
        stack.append((cp[0], cp[1] + 1))
        path.append((cp[0], cp[1] + 1))

    elif grid[cp[0] + 1][cp[1]] == '-':
        stack.append((cp[0] + 1, cp[1]))
        path.append((cp[0] + 1, cp[1]))